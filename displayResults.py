import json

def displayResults():    
    with open('benchmark.json') as jsonFile:
        jsonData = json.load(jsonFile)
    result = jsonData;
    output = """
                                                      Mean Query Execution Time

    _________________________________________________________________________________________________________________________
    |Configurations ==> |                   |                   |                   |                   |                   |
    |                   | 1. Only Indexed   | 2. Indexing of    | 3. Indexing of    | 4. Indexing of    | 5. Indexing of    |
    |Queries            |    PRIMARY KEY    |    url field      |    published,     |    post2tag table |    all tables     |
    |  ||               |   (AUTO INCREMENT)|    (wp_posts)     |    site & rank    |   (COMPOSITE KEY) |     (1+2+3+4)     |
    |  VV               |                   |                   |    fields         |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  1. Post By Id    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |
    |                   |        ms         |        ms         |        ms         |        ms         |        ms         |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  2. Post By Url   |        -          |    {:^11.7f}    |        -          |        -          |    {:^11.7f}    |
    |                   |        ms         |        ms         |        ms         |        ms         |        ms         |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  3. Collection    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |
    |       Type 1      |        ms         |        ms         |        ms         |        ms         |        ms         |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  4. Collection    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |
    |       Type 2      |        ms         |        ms         |        ms         |        ms         |        ms         |
    |                   |                   |                   |                   |                   |                   |
    |-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
    |                   |                   |                   |                   |                   |                   |
    |                   |                   |                   |                   |                   |                   |
    |  5. Collection    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |    {:^11.7f}    |
    |       Type 3      |        ms         |        ms         |        ms         |        ms         |        ms         |
    |                   |                   |                   |                   |                   |                   |
    |___________________|___________________|___________________|___________________|___________________|___________________|
    """.format(
        result['Config1']['postById'] * 1000,
        result['Config2']['postById'] * 1000,
        result['Config3']['postById'] * 1000,
        result['Config4']['postById'] * 1000,
        result['Config5']['postById'] * 1000,

        result['Config2']['postByUrl'] * 1000,
        result['Config5']['postByUrl'] * 1000,

        result['Config1']['collection1'] * 1000,
        result['Config2']['collection1'] * 1000,
        result['Config3']['collection1'] * 1000,
        result['Config4']['collection1'] * 1000,
        result['Config5']['collection1'] * 1000,

        result['Config1']['collection2'] * 1000,
        result['Config2']['collection2'] * 1000,
        result['Config3']['collection2'] * 1000,
        result['Config4']['collection2'] * 1000,
        result['Config5']['collection2'] * 1000,

        result['Config1']['collection3'] * 1000,
        result['Config2']['collection3'] * 1000,
        result['Config3']['collection3'] * 1000,
        result['Config4']['collection3'] * 1000,
        result['Config5']['collection3'] * 1000)
    print(output)