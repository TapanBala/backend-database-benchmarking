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
    print(" SELECT text_id AS id, p_text AS text, p_published AS published FROM tag_query3 LEFT JOIN text ON text_id = text.id WHERE p_country = 1 p_type = 'postType' AND p_rank < `postRank` AND p_site = 'site' ORDER BY p_rank DESC LIMIT 20;")
    for run in range(totalRuns):
        postType = config.postTypes[randint(0, 9)]
        postRank = randint(1, config.totalPosts - 1)
        country = config.countries[randint(0, 3)]
        site = config.siteConfig[randint(0, 19)]
        query = "SELECT text_id AS id, p_text AS text, p_published AS published FROM tag_query3 LEFT JOIN text ON text_id = text.id WHERE p_{} = 1 AND p_type = '{}' AND p_rank < {} AND p_site = '{}' ORDER BY p_rank DESC LIMIT {}".format(country, postType, postRank, site, limit)
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