import pymysql.cursors
from timer import Timer
import queryBuilder

dbConfig = {
    'user'   : 'root',
    'host'   : 'localhost',
    'db'     : 'test',
    'charset': 'latin1'
}

selectObject = "ES"

tableName = "wp_posts"

queryConfig = (
    ("id", 15466),
    ("ES", 1),
    ("US", 1),
    ("MX", 0),
    ("CO", 0),
    ("special", 0),
    ("published", "2011-11-08 04:19:18"),
    ("publishedGreaterThan", "2011-11-08 04:19:18"),
    ("publishedLessThan", "2011-11-08 04:19:18")
)

whereClauses0 = (
    ("ES",        "=", 1                    ),
    ("US",        "=", 1                    ),
    ("type",      "=", "video"              ),
    ("published", ">", "2011-11-08 04:19:18"),
    ("special",   "=", 1                    )
)

whereClauses1 = (
    ("ES",        "=", 0                    ),
    ("US",        "=", 0                    ),
    ("type",      "=", "slideshow"          ),
    ("published", "<", "2011-11-08 04:19:18"),
    ("special",   "=", 1                    )
)

whereClauses2 = (
    ("ES",        "=", 1                    ),
    ("US",        "=", 0                    ),
    ("type",      "=", "ecommerce"          ),
    ("published", ">", "2013-11-08 04:19:18"),
    ("special",   "=", 0                    )
)

whereClauses3 = (
    ("ES",        "=", 0                    ),
    ("US",        "=", 1                    ),
    ("type",      "=", "brand_article_video"),
    ("published", "<", "2015-11-08 04:19:18"),
    ("special",   "=", 1                    )
)

limit = 100
offset = 1345

def singleQueryProcess():
    connection = pymysql.connect(**dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    # rowsTraversed = None
    for clauses in queryConfig:
        query = queryBuilder.single(selectObject, tableName, clauses[0], clauses[1])
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
    connection = pymysql.connect(**dbConfig)
    cursor = connection.cursor()
    timer = Timer()
    # rowsTraversed = None
    meanTime = 0
    query = queryBuilder.collection(selectObject, tableName, whereClauses, limit, offset)
    print("Executing query =====> {}".format(query))
    for executions in range(1, 6):
        timer.restart()
        cursor.execute(query)
        meanTime += timer.get_seconds()
    print("Mean query execution time : {:.5f} seconds ".format(meanTime / 5))
    # cursor.execute("desc " + query)
    # rowsTraversed = cursor.fetchone()[8]
    # print("Rows Traversed : {}".format(rowsTraversed))
    # print("=====================================================")
    connection.close()

singleQueryProcess()

collectionQueryProcess(whereClauses0)
collectionQueryProcess(whereClauses1)
collectionQueryProcess(whereClauses2)
collectionQueryProcess(whereClauses3)