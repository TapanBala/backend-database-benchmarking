import pymysql.cursors
from timer import Timer
from random import randint
import config

def multipleJoinsQueryTypeB():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    percentConfig = totalRuns/100
    timer = Timer()
    meanTime = 0
    print("=============================== Multiple Join Query Type B ===============================")
    print("SELECT t.name AS tagname FROM post2tag AS pt LEFT JOIN wp_posts AS p ON pt.post_id = p.id LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE p.site = 'blogName';")
    for run in range(totalRuns):
        postId = randint(1, 60000)
        site = config.siteConfig[randint(0, 9)]
        query = "SELECT t.{} AS {} FROM post2tag AS pt LEFT JOIN wp_posts AS p ON pt.post_id = p.id LEFT Join wp_tags AS t ON pt.tag_id = t.id WHERE p.site = '{}'".format('name', 'tagname', site)
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