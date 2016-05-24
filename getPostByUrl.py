import pymysql.cursors
from timer import Timer
from random import randint
import config

def getPostByUrl():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns / 100
    print("=================================== Post By Url Query ====================================")
    print("SELECT obj FROM wp_posts WHERE url = 'url';")
    for run in range(totalRuns):
        postId = randint(1, config.totalPosts)
        query = "SELECT url FROM wp_posts WHERE id = {}".format(postId)
        cursor.execute(query)
        url = cursor.fetchone()[0]
        query = "SELECT text, id FROM wp_posts WHERE url = '{}'".format(url)
        timer.restart()
        cursor.execute(query)
        meanTime += timer.get_seconds()
        percent = (run / totalRuns) * 100
        if (run % percentConfig) == 0:
            print("Completed: {:.0f} %                ".format(percent), end = '\r')
    print("Completed 100 %")
    print("Mean query execution time : {:.10f} seconds".format(meanTime / totalRuns))
    connection.close()
    print("")
    print("Example Query")
    print(query)
    print("")
    return meanTime / totalRuns