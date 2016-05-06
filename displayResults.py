import json

def displayResults():    
    with open('benchmark.json') as json_file:
        json_data = json.load(json_file)
    result = json_data;
    output = """                                                  Mean Query Execution Time

    _________________________________________________________________________________________________________________________
    |Configurations ==> |                   |                   |                   |                   |                   |
    |                   | 1. Only Indexed   | 2. Indexing of    | 3. Indexing of    | 4. Indexing with  |                   |
    |Queries            |    PRIMARY KEY    |    published &    |    post2tag table |    Config (2 + 3) |                   |
    |  ||               |   (AUTO INCREMENT)|    site fields    |   (COMPOSITE KEY) |                   |                   |
    |  VV               |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  1. Post Query    |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |     {:.06f}s     |                   |
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  2. Collection    |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |     {:.06f}s     |                   |
    |     Query         |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  3. Posts By Tags |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |     {:.06f}s     |                   |
    |     Query         |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  4.               |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  5.               |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |___________________|___________________|___________________|___________________|___________________|___________________|
    """.format(result['Config1']['post'],result['Config2']['post'],result['Config3']['post'],result['Config4']['post'],result['Config1']['collection'],result['Config2']['collection'],result['Config3']['collection'],result['Config4']['collection'], result['Config1']['postsByTags'],result['Config2']['postsByTags'],result['Config3']['postsByTags'],result['Config4']['postsByTags'])
    print(output)