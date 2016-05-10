import pymysql.cursors


dbConfig = {
    'user'   : 'root',
    'host'   : 'localhost',
    'db'     : 'test',
    'charset': 'latin1'
}

siteConfig = [
    ('BwUTGoeJcBsRQcAsPNxo'),
    ('umbFWWpoBgyWbfHRBmvY'),
    ('fqVPpMozrPkXjaLXvijA'),
    ('BJlwXHlwfUdKFDlqKQTv'),
    ('DQsBnqOHtCcqxFITcbjq'),
    ('iGcOTClVXTShmthgyims'),
    ('IqnvMHfzXxXfPHgGnlwD'),
    ('CiShLxZUNJcCwuxXaxrG'),
    ('bMHtmgvOABkTqUjcTOBW'),
    ('yhsJPhKikjHEmoBZxMYB')
]

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

countries = [
    ('ES'),
    ('US'),
    ('MX'),
    ('CO')
]

executions = 100

totalPosts = 60000

totalTags = 100000

def getTags(tags):
    connection = pymysql.connect(**dbConfig)
    cursor = connection.cursor()
    query = " SELECT name FROM wp_tags"
    cursor.execute(query)
    results = cursor.fetchall()
    for tag in range(len(results)):
        tags.append(results[tag][0])