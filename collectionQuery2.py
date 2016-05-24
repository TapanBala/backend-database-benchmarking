import pymysql.cursors
from timer import Timer
from random import randint
from faker import Faker
import config

def collectionQuery2():
    fake = Faker()
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    limit = 20
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns / 100
    tags = []
    config.getTags(tags)
    print("=================================== Collection Query 2 ===================================")
    print("SELECT text_id AS id, p_text AS text FROM wp_tags AS t LEFT JOIN post2tag ON t.id = tag_id LEFT JOIN tag_query2 ON post_id = text_id LEFT JOIN text ON text_id = text.id WHERE t.name = 'tagName' AND p_site = 'site' AND p_country = 1 AND p_rank < rank ORDER BY p_rank DESC LIMIT 20")
    for run in range(totalRuns):
        tagName = tags[randint(0, config.totalTags - 1)]
        postRank = randint(1, config.totalPosts)
        site = config.siteConfig[randint(0, 19)]
        country = config.countries[randint(0, 3)]
        query = "SELECT text_id AS id, p_text AS text FROM wp_tags AS t LEFT JOIN post2tag ON t.id = tag_id LEFT JOIN tag_query2 ON post_id = text_id LEFT JOIN text ON text_id = text.id WHERE t.name = '{}' AND p_site = '{}' AND p_{} = 1 AND p_rank < {} ORDER BY p_rank DESC LIMIT {}".format(tagName, site, country, postRank, limit)
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
    