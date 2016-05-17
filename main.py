import indexBuilder
from benchmark import benchmark
# from displayResults import displayResults
from displayFormattedResults import displayFormattedResults
from displayUseCases import displayUseCases

def configIndexAutoIncrement():
    indexBuilder.dropIndex()
    benchmark('Config1')

def configIndexUrl():
    indexBuilder.dropIndex()
    indexBuilder.indexUrl()
    benchmark('Config2')

def configIndexPosts():
    indexBuilder.dropIndex()
    indexBuilder.indexSiteRank()
    indexBuilder.indexTime()
    benchmark('Config3')

def configIndexPost2Tag():
    indexBuilder.dropIndex()
    indexBuilder.indexPost2Tag()
    benchmark('Config4')

def configIndexAll():
    indexBuilder.dropIndex()
    indexBuilder.indexUrl()
    indexBuilder.indexSiteRank()
    indexBuilder.indexTime()
    indexBuilder.indexPost2Tag()
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