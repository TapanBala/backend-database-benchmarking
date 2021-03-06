import pymysql.cursors

dbConfig = {
    'user'     : 'root',
    'host'     : 'localhost',
    'db'       : 'bench',
    'password' : '12345',
    'charset'  : 'latin1'
}

siteConfig = [
    ('BedDVtNwjVuyJviMStOf'),
    ('bRlWPxcyefwOBOXhQBSi'),
    ('CrfGHAEPcaTOblQDrhIR'),
    ('hMsOfgtHHnAkmTfHBXmk'),
    ('KjpkrqhUIuPfJSDmvxrJ'),
    ('PsZHKBevUICySgEicTWw'),
    ('raLVKYBXzdtbnbxdCkEj'),
    ('RlMbEDQmlVeypfpwgzzY'),
    ('rnrqEOtlEawLxyVmPOZr'),
    ('sTbFhWNKCnhboxrLuQBv'),
    ('UaMGFivyPFsIOzxsXszf'),
    ('urFbELVPCkayhBxsMXqS'),
    ('uWezTnKSFVXopubsxBTQ'),
    ('UxjfKViZKqDQbkbtpGtE'),
    ('UYWYDLlxoSdruHmWvizB'),
    ('vxCASAfDoJyBArBKpcqd'),
    ('wjhLBCoOaSiQQfOqhVLl'),
    ('wLwiBeolzmFLeGfdGTKd'),
    ('XgsGyYVEnAackRJxYwKl'),
    ('xlKjaFvrTkVDDiqtHmpA')
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

totalPosts = 1000000

totalTags = 100000

def getTags(tags):
    connection = pymysql.connect(**dbConfig)
    cursor = connection.cursor()
    query = " SELECT name FROM wp_tags"
    cursor.execute(query)
    results = cursor.fetchall()
    for tag in range(len(results)):
        tags.append(results[tag][0])