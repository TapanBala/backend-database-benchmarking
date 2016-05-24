import pymysql.cursors
from timer import Timer
from random import randint
from faker import Faker
import config

def collectionQuery1():
    fake = Faker()
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    limit = 20
    percentConfig = totalRuns / 100
    tags = []
    config.getTags(tags)
    print("=================================== Collection Query 1 ===================================")
    print("SELECT text_id AS id, p_text AS text FROM wp_tags AS t LEFT JOIN post2tag ON t.id = tag_id LEFT JOIN tag_query1 ON text_id = post_id LEFT JOIN text ON text_id = text.id WHERE t.name = 'tagName' AND p_site = 'site' AND p_country = 1 AND p_published < 'timestamp' ORDER BY p_published DESC LIMIT 20")
    for run in range(totalRuns):
        tagName = tags[randint(0, config.totalTags - 1)]
        published = fake.date_time_between(start_date = "-6y", end_date = "now")
        country = config.countries[randint(0, 3)]
        site = config.siteConfig[randint(0, 19)]
        query = "SELECT text_id AS id, p_text AS text FROM wp_tags AS t LEFT JOIN post2tag ON t.id = tag_id LEFT JOIN tag_query1 ON text_id = post_id LEFT JOIN text ON text_id = text.id WHERE t.name = '{}' AND p_site = '{}' AND p_{} = 1 AND p_published < '{}' ORDER BY p_published DESC LIMIT {}".format(tagName, site, country, published, limit)
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