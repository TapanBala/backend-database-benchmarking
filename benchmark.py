from getPostById import getPostById
from getPostByUrl import getPostByUrl
from collectionQuery1 import collectionQuery1
from collectionQuery2 import collectionQuery2
from collectionQuery3 import collectionQuery3
from timer import Timer
import json

def benchmark(benchmarkConfig):
    timer = Timer()
    print("======================================= {} ==========================================".format(benchmarkConfig))
    timePostById = getPostById()
    timePostByUrl = getPostByUrl()
    timeCollection1 = collectionQuery1()
    timeCollection2 = collectionQuery2()
    timeCollection3 = collectionQuery3()
    print("=================================== {} COMPLETED ====================================".format(benchmarkConfig))
    print("Total Time : {}".format(timer.get_time_hhmmss()))
    json_data = {}
    try:
        with open('benchmark.json') as json_file:
            json_data = json.load(json_file)
    except Exception as err:
        print(err)
    result = json_data
    result.update({benchmarkConfig:{'postById': timePostById, 'postByUrl': timePostByUrl, 'collection1': timeCollection1, 'collection2': timeCollection2, 'collection3': timeCollection3}})
    with open ('benchmark.json', 'w') as outfile:
        json.dump(result, outfile, indent = 4)