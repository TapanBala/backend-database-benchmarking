import pymysql.cursors
from timer import Timer
from random import randint
import config

def postQuery():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns / 100
    print("======================================= Post Query =======================================")
    print("SELECT obj FROM wp_posts WHERE id = post_id;")
    print("SELECT t.name FROM wp_posts AS p LEFT JOIN post2tag AS pt ON p.id = pt.post_id LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE p.id = 'postId'")
    for run in range(totalRuns):
        postId = randint(1, config.totalPosts)
        queryPost = "SELECT {} FROM wp_posts WHERE id = {}".format('text', postId)
        queryTag = "SELECT t.{} FROM wp_posts AS p LEFT JOIN post2tag AS pt ON p.id = pt.post_id LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE p.id = {}".format("name", postId)
        timer.restart()
        cursor.execute(queryPost)
        cursor.execute(queryTag)
        meanTime += timer.get_seconds()
        percent = (run / totalRuns) * 100
        if (run % percentConfig) == 0:
            print("Completed: {:.0f} %                ".format(percent), end = '\r')
    print("Completed 100 %")
    print("Mean query execution time : {:.10f} seconds".format(meanTime / totalRuns))
    connection.close()
    return meanTime / totalRuns