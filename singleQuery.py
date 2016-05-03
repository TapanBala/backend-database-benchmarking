import pymysql.cursors
from timer import Timer
from random import randint
import config

def singleQuery():
    obj = 'text'
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns/100
    print("====================================== Single Query ======================================")
    print("SELECT obj FROM wp_posts WHERE id = post_id AND site = 'blogName';")
    for run in range(totalRuns):
        postId = randint(1, 60000)
        query = "SELECT {} FROM wp_posts WHERE id = {}".format(obj, postId)
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