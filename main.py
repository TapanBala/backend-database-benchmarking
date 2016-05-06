import pymysql.cursors
import config
from benchmark import benchmark
from displayResults import displayResults

def dropAllIndex():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag DROP PRIMARY KEY"
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
    connection.commit()

def configIndexAutoIncrement():
    dropAllIndex()
    benchmark('Config1')

def configIndexPosts():
    dropAllIndex()
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "CREATE INDEX site_index on wp_posts (site)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX time_index on wp_posts (published)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()
    benchmark('Config2')

def configIndexPost2Tag():
    dropAllIndex()
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag ADD PRIMARY KEY (post_id, tag_id)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()
    benchmark('Config3')

def configIndexPostsPost2Tag():
    dropAllIndex()
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    try:
        query = "ALTER TABLE post2tag ADD PRIMARY KEY (post_id, tag_id)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX site_index on wp_posts (site)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    try:
        query = "CREATE INDEX time_index on wp_posts (published)"
        cursor.execute(query)
    except Exception as err:
        print(err)
    connection.commit()
    benchmark('Config4')

def process():
    print("=============================== BENCHMARK SUITE COMMENCING ===============================")
    configIndexAutoIncrement()
    configIndexPosts()
    configIndexPost2Tag()
    configIndexPostsPost2Tag()
    print("================================= BENCHMARKING COMPLETED =================================\n\n\n\n\n")
    print("================================== BENCHMARKING RESULTS ==================================")
    displayResults()
    
process()