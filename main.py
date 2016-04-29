import pymysql.cursors
from timer import Timer
import queryBuilder
import config

def singleQueryProcess():
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    # rowsTraversed = None
    for clause in config.singleQueryConfig:
        query = queryBuilder.single(config.selectProperty, config.tableName, clause)
        print("Executing query =====> {}".format(query))
        meanTime = 0
        for executions in range(1, 6):
            timer.restart()
            cursor.execute(query)
            meanTime += timer.get_seconds()
        print("Mean query execution time : {:.5f} seconds".format(meanTime / 5))
        print("")
        # cursor.execute("desc " + query)
        # rowsTraversed = cursor.fetchone()[8]
        # print("Rows Traversed : {}".format(rowsTraversed))
        # print("=====================================================")
    connection.close()

def collectionQueryProcess(whereClauses):
    connection = pymysql.connect(**config.dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    # rowsTraversed = None
    meanTime = 0
    query = queryBuilder.collection(config.selectProperty, config.tableName, whereClauses, config.queryRange, config.limit)
    print("Executing query =====> {}".format(query))
    for executions in range(1, 6):
        timer.restart()
        cursor.execute(query)
        meanTime += timer.get_seconds()
    print("Mean query execution time : {:.5f} seconds ".format(meanTime / 5))
    print("")
    # cursor.execute("desc " + query)
    # rowsTraversed = cursor.fetchone()[8]
    # print("Rows Traversed : {}".format(rowsTraversed))
    # print("=====================================================")
    connection.close()

singleQueryProcess()

for whereClauses in config.collectionQueryConfig:
    collectionQueryProcess(whereClauses)