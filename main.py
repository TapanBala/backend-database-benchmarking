import indexBuilder
from benchmark import benchmark
from displayResults import displayResults
from displayUseCases import displayUseCases

def configIndexAutoIncrement():
    indexBuilder.dropIndex()
    benchmark('Config1')

def configIndexUrl():
    indexBuilder.indexUrl()
    benchmark('Config2')

def configIndexPosts():
    indexBuilder.dropUrlIndex()
    indexBuilder.indexTagQuery("tag_query1")
    indexBuilder.indexTagQuery("tag_query2")
    indexBuilder.indexTagQuery("tag_query3")
    benchmark('Config3')

def configIndexPost2Tag():
    indexBuilder.dropTagQueryIndex("tag_query1")
    indexBuilder.dropTagQueryIndex("tag_query2")
    indexBuilder.dropTagQueryIndex("tag_query3")
    indexBuilder.indexPost2Tag()
    benchmark('Config4')

def configIndexAll():
    indexBuilder.indexUrl()
    indexBuilder.indexTagQuery("tag_query1")
    indexBuilder.indexTagQuery("tag_query2")
    indexBuilder.indexTagQuery("tag_query3")
    benchmark('Config5')

def process():
    print("=============================== BENCHMARK SUITE COMMENCING ===============================")
    configIndexAutoIncrement()
    configIndexUrl()
    configIndexPosts()
    configIndexPost2Tag()
    configIndexAll()
    print("================================= BENCHMARKING COMPLETED =================================\n\n\n\n\n")
    print("================================== BENCHMARKING RESULTS ==================================")
    displayResults()
    displayUseCases()
    
process()