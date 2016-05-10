import pymysql.cursors
import config

def dropIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag DROP PRIMARY KEY"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX url_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX site_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX time_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX rank_index on wp_posts"
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

def indexSite():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX site_index on wp_posts (site)"
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

def indexRank():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX rank_index on wp_posts (rank)"
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