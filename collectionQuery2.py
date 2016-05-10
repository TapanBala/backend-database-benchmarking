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
    print("SELECT p.id AS postId, p.text AS postText, p.published AS datePublished FROM wp_tags AS t LEFT JOIN post2tag AS pt ON t.id = pt.tag_id AND t.name = 'tagName' LEFT JOIN wp_posts AS p ON pt.post_id = p.id WHERE p.country = 1 AND p.rank < `postRank` AND p.site = `site` ORDER BY rank ASC LIMIT 20;")
    for run in range(totalRuns):
        tagName = tags[randint(0, config.totalTags - 1)]
        postRank = randint(1, config.totalPosts)
        site = config.siteConfig[randint(0, 9)]
        country = config.countries[randint(0, 3)]
        query = "SELECT p.id AS postId, p.text AS postText, p.published AS datePublished FROM wp_tags AS t LEFT JOIN post2tag AS pt ON t.id = pt.tag_id AND t.name = '{}' LEFT JOIN wp_posts AS p ON pt.post_id = p.id WHERE p.{} = 1 AND p.rank < {} AND p.site = '{}' ORDER BY rank ASC LIMIT {}".format(tagName, country, postRank, site, limit)
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