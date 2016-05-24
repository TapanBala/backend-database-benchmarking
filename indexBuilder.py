import pymysql.cursors
import config

def dropIndex():
    dropUrlIndex()
    dropPost2TagIndex()
    dropTagQueryIndex("tag_query1")
    dropTagQueryIndex("tag_query2")
    dropTagQueryIndex("tag_query3")

def dropUrlIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "DROP INDEX url_index on wp_posts"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def dropPost2TagIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag DROP PRIMARY KEY"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def dropTagQueryIndex(queryTable):
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "DROP INDEX site_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX ES_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX US_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX MX_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX CO_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX time_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX rank_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "DROP INDEX type_index on {}".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)    
    connection.commit()

def indexUrl():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE UNIQUE INDEX url_index on wp_posts (url)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()

def indexTagQuery(queryTable):
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX site_index on {} (p_site)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX ES_index on {} (p_ES)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX US_index on {} (p_US)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX MX_index on {} (p_MX)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX CO_index on {} (p_CO)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX time_index on {} (p_published)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX rank_index on {} (p_rank)".format(queryTable)
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX type_index on {} (p_type)".format(queryTable)
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