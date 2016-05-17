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
    print("SELECT p.id, p.text FROM wp_tags AS t LEFT JOIN post2tag AS pt ON t.id = pt.tag_id AND t.name = 'tagName' LEFT JOIN wp_posts AS p ON pt.post_id = p.id WHERE p.site = 'site' AND p.country = 1 AND p.published < 'timestamp' WHERE pt.tag_id = `tagId` ORDER BY published DESC LIMIT 20;")
    for run in range(totalRuns):
        tagName = tags[randint(0, config.totalTags - 1)]
        published = fake.date_time_between(start_date = "-6y", end_date = "now")
        country = config.countries[randint(0, 3)]
        site = config.siteConfig[randint(0, 19)]
        query = "SELECT p.id, p.text FROM wp_tags AS t LEFT JOIN post2tag AS pt ON t.id = pt.tag_id AND t.name = '{}' LEFT JOIN wp_posts AS p ON pt.post_id = p.id WHERE p.site = '{}' AND p.{} = 1 AND p.published < '{}' ORDER BY published DESC LIMIT {}".format(tagName, site, country, published, limit)
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