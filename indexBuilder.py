import pymysql.cursors
import config

def dropIndex():
    dropPost2Tag()
    dropTimeIndex()
    dropRankIndex()
    dropSiteRankIndex()

def dropPost2TagIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag DROP PRIMARY KEY"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def dropTimeIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "DROP INDEX time_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def dropRankIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "DROP INDEX rank_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def dropSiteRankIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "DROP INDEX compk_siterank on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def indexUrl():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX url_index on wp_posts (url)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def indexTime():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX time_index on wp_posts (published)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def indexPost2Tag():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag ADD PRIMARY KEY (post_id, tag_id)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def indexSiteRank():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE wp_posts ADD CONSTRAINT compk_siterank UNIQUE (site, rank)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()    