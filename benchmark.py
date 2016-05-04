from singleQuery import singleQuery
from collectionQuery import collectionQuery
from singleJoinQuery import singleJoinQuery
from multipleJoinsQueryTypeA import multipleJoinsQueryTypeA
from multipleJoinsQueryTypeB import multipleJoinsQueryTypeB
from timer import Timer
import json

def benchmark(benchmarkConfig):
    timer = Timer()
    print("======================================= {} ==========================================".format(benchmarkConfig))
    timeSingle = singleQuery()
    timeCollection =  collectionQuery()
    timeSingleJoin = singleJoinQuery()
    timeMultipleJoinA = multipleJoinsQueryTypeA()
    timeMultipleJoinB = multipleJoinsQueryTypeB()
    print("=================================== {} COMPLETED ====================================".format(benchmarkConfig))
    print("Total Time : {}".format(timer.get_time_hhmmss()))
    json_data = {}
    try:
        with open('benchmark.json') as json_file:
            json_data = json.load(json_file)
    except Exception as err:
        print(err)
    result = json_data
    result.update({benchmarkConfig:{'single': timeSingle, 'collection': timeCollection, 'singleJoin': timeSingleJoin, 'multipleJoinA': timeMultipleJoinA, 'multipleJoinB': timeMultipleJoinB}})
    with open ('benchmark.json', 'w') as outfile:
        json.dump(result, outfile)