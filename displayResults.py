import json

def displayResults():    
    with open('benchmark.json') as json_file:
        json_data = json.load(json_file)
    result = json_data;
    output = """                                                Mean Query Execution Time

    _________________________________________________________________________________________________________________________
    |Configurations ==> |                   |                   |                   |                   |                   |
    |                   | 1. Only Indexed   | 2. Indexing of    | 3. Indexing of    |                   |                   |
    |Queries            |    PRIMARY KEY    |    published &    |    post2tag table |                   |                   |
    |  ||               |   (AUTO INCREMENT)|    site fields    |   (COMPOSITE KEY) |                   |                   |
    |  VV               |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  1. Single Query  |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  2. Collection    |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |                   |                   |
    |     Query         |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  3. Single Join   |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |                   |                   |
    |     Query         |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  4. Multiple Join |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |                   |                   |
    |     Query (1)     |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  5. Multiple Join |     {:.06f}s     |      {:.06f}s    |      {:.06f}s    |                   |                   |
    |     Query (2)     |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |___________________|___________________|___________________|___________________|___________________|___________________|
    """.format(result['Config1']['single'],result['Config2']['single'],result['Config3']['single'],result['Config1']['collection'],result['Config2']['collection'],result['Config3']['collection'], result['Config1']['singleJoin'],result['Config2']['singleJoin'],result['Config3']['singleJoin'], result['Config1']['multipleJoinA'],result['Config2']['multipleJoinA'],result['Config3']['multipleJoinA'], result['Config1']['multipleJoinB'],result['Config2']['multipleJoinB'],result['Config3']['multipleJoinB'])
    print(output)