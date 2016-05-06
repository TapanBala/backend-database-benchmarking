import pymysql.cursors
from timer import Timer
from random import randint
from faker import Faker
import config

def postsByTagsQuery():
    fake = Faker()
    totalRuns = config.executions
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    limit = 20
    percentConfig = totalRuns / 100
    print("================================== Posts by Tags Query ===================================")
    print("SELECT p.id AS postId, p.text AS postText FROM post2tag AS pt LEFT JOIN wp_posts AS p ON pt.post_id = p.id AND p.country = 1 AND p.published < 'timestamp' WHERE pt.tag_id = `tagId` LIMIT 20;")
    for run in range(totalRuns):
        tagId = randint(1, config.totalTags)
        published = fake.date_time_between(start_date = "-6y", end_date = "now")
        country = config.countries[randint(0, 3)]
        query = "SELECT p.{} AS {}, p.{} AS {} FROM post2tag AS pt LEFT JOIN wp_posts AS p ON pt.post_id = p.id AND p.{} = 1 AND p.published < '{}' WHERE pt.tag_id = {} LIMIT {}".format('id', 'postId', 'text', 'postText', country, published, tagId, limit)
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