import pymysql.cursors
from timer import Timer
from random import randint
from faker import Faker
import config

def collectionQuery():
    fake = Faker()
    totalRuns = config.executions
    limit = 100
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    meanTime = 0
    percentConfig = totalRuns/100

    print("==================================== Collection Query ====================================")
    print("SELECT obj FROM wp_posts WHERE ES = 1 AND published < 'timestamp' AND site = 'blogName' LIMIT 20;")

    for run in range(totalRuns):
        ES = randint(0, 1)
        published = fake.date_time_between(start_date = "-6y", end_date = "now")
        site = config.siteConfig[randint(0, 9)]
        query = "SELECT {}, {} FROM wp_posts WHERE ES = {} AND published < '{}' AND site = '{}' LIMIT {}".format('id', 'text', ES, published, site, limit)
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