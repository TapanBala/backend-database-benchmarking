from faker import Faker
from random import randint

fake = Faker()

dbConfig = {
    'user'   : 'root',
    'host'   : 'localhost',
    'db'     : 'test',
    'charset': 'latin1'
}

postTypes = [
    ('normal'),
    ('ecommerce'),
    ('slideshow'),
    ('video'),
    ('duplicate'),
    ('branded_club'),
    ('brand_article'),
    ('brand_article_video'),
    ('longform'),
    ('reposted_slideshow')
]

singleQueryConfig = (
    ("id",        "=", randint(1,60000)                                                                    ),
    ("ES",        "=", randint(0,1)                                                             ),
    ("US",        "=", randint(0,1)                                                             ),
    ("MX",        "=", randint(0,1)                                                             ),
    ("CO",        "=", randint(0,1)                                                             ),
    ("special",   "=", randint(0,1)                                                             ),
    ("type",      "=", postTypes[randint(0,9)]                                                  ),
    ("published", "=", "{}".format(fake.date_time_between(start_date = "-6y", end_date = "now"))),
    ("published", ">", "{}".format(fake.date_time_between(start_date = "-6y", end_date = "now"))),
    ("published", "<", "{}".format(fake.date_time_between(start_date = "-6y", end_date = "now")))
)

countries = [
    ("ES"),
    ("US"),
    ("MX"),
    ("CO")
]

clauseConfig = [
    ("="),
    (">"),
    ("<"),
    (">="),
    ("<=")
]

postProperties = [
    ("id"),
    ("text"),
    ("published"),
    ("url")
]

limit = randint(10, 5000)
queryRange = randint(1, 5000)
selectProperty = postProperties[randint(0,3)]
tableName = "wp_posts"
collectionQueryConfig = []

def process():
    for iterations in range(10):
        collectionQueryConfig.append((
            (countries[randint(0,1)], "=",                        randint(0,1)                                                             ),
            (countries[randint(2,3)], "=",                        randint(0,1)                                                             ),
            ("type",                  "=",                        postTypes[randint(0,9)]                                                  ),
            ("published",             clauseConfig[randint(0,4)], "{}".format(fake.date_time_between(start_date = "-6y", end_date = "now"))),
            ("special",               "=",                        randint(0,1)                                                             )          
        ))

process()