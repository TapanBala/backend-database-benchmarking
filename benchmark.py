from postQuery import postQuery
from collectionQuery import collectionQuery
from postsByTagsQuery import postsByTagsQuery
# from multipleJoinsQueryTypeA import multipleJoinsQueryTypeA
# from multipleJoinsQueryTypeB import multipleJoinsQueryTypeB
from timer import Timer
import json

def benchmark(benchmarkConfig):
    timer = Timer()
    print("======================================= {} ==========================================".format(benchmarkConfig))
    timePost = postQuery()
    timeCollection =  collectionQuery()
    timePostsByTags = postsByTagsQuery()
    # timeMultipleJoinA = multipleJoinsQueryTypeA()
    # timeMultipleJoinB = multipleJoinsQueryTypeB()
    print("=================================== {} COMPLETED ====================================".format(benchmarkConfig))
    print("Total Time : {}".format(timer.get_time_hhmmss()))
    json_data = {}
    try:
        with open('benchmark.json') as json_file:
            json_data = json.load(json_file)
    except Exception as err:
        print(err)
    result = json_data
    result.update({benchmarkConfig:{'post': timePost, 'collection': timeCollection, 'postsByTags': timePostsByTags}})
    # result.update({benchmarkConfig:{'post': timePost, 'collection': timeCollection, 'postsByTags': timePostsByTags, 'multipleJoinA': timeMultipleJoinA, 'multipleJoinB': timeMultipleJoinB}})
    with open ('benchmark.json', 'w') as outfile:
        json.dump(result, outfile)