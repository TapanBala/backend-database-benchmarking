import pymysql.cursors
from timer import Timer
from random import randint
import config

def multipleJoinsQueryTypeA():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    percentConfig = totalRuns / 100
    timer = Timer()
    meanTime = 0
    print("=============================== Multiple Join Query Type A ===============================")
    print(" SELECT p.id AS postid, p.text AS posttext, t.name AS tagname FROM wp_posts AS p LEFT JOIN post2tag AS pt ON p.id = pt.post_id LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE p.id = `postId`;")
    for run in range(totalRuns):
        postId = randint(1, config.totalPosts)
        query = "SELECT p.{} AS {}, t.{} AS {} FROM wp_posts AS p LEFT JOIN post2tag AS pt ON p.id = pt.post_id LEFT Join wp_tags AS t ON pt.tag_id = t.id WHERE p.id = {}".format('text', 'posttext', 'name', 'tagname', postId)
        timer.restart()
        cursor.execute(query)
        meanTime += timer.get_seconds()
        percent = (run / totalRuns) * 100
        if (run % percentConfig) == 0:
            print("Completed: {:.0f} %                ".format(percent), end='\r')
    print("Completed 100 %")
    print("Mean query execution time : {:.10f} seconds".format(meanTime / totalRuns))
    connection.close()
    return meanTime / totalRuns