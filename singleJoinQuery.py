import pymysql.cursors
from timer import Timer
from random import randint
import config

def singleJoinQuery():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns/100
    print("=================================== Single Join Query ====================================")
    print("SELECT t.name AS tagname FROM post2tag AS pt LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE pt.post_id = `postId`;")
    for run in range(totalRuns):
        postId = randint(1, 60000)
        query = "SELECT t.{} AS {} FROM post2tag AS pt LEFT JOIN wp_tags AS t ON pt.tag_id = t.id WHERE pt.post_id = {}".format('name', 'tagname',postId)
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