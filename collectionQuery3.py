import pymysql.cursors
from timer import Timer
from random import randint
import config

def collectionQuery3():
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    percentConfig = totalRuns / 100
    timer = Timer()
    meanTime = 0
    limit = 20
    print("=================================== Collection Query 3 ===================================")
    print(" SELECT id, text, published FROM wp_posts WHERE country = 1 type = 'postType' AND rank < `postRank` AND site = 'site' ORDER BY rank DESC LIMIT 20;")
    for run in range(totalRuns):
        postType = config.postTypes[randint(0, 9)]
        postRank = randint(1, config.totalPosts - 1)
        country = config.countries[randint(0, 3)]
        site = config.siteConfig[randint(0, 9)]
        query = "SELECT id, text, published FROM wp_posts WHERE {} = 1 AND type = '{}' AND rank < {} AND site = '{}' ORDER BY rank DESC LIMIT {}".format(country, postType, postRank, site, limit)
        timer.restart()
        cursor.execute(query)
        meanTime += timer.get_seconds()
        percent = (run / totalRuns) * 100
        if (run % percentConfig) == 0:
            print("Completed: {:.0f} %                ".format(percent), end = '\r')
    print("Completed 100 %")
    print("Mean query execution time : {:.10f} seconds".format(meanTime / totalRuns))
    connection.close()
    return meanTime / totalRuns