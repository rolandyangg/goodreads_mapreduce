from pyspark import SparkContext
sc = SparkContext("local", "BookPairs")

lines = sc.textFile("/home/cs143/data/goodreads.dat")

def map_helper(line):
    ids = [int(x) for x in line.split(":")[1].split(",")]
    return [(ids[i], ids[j]) for i in range(len(ids)) for j in range(i + 1, len(ids))]

book_pairs = lines.flatMap(map_helper).map(lambda pair: (pair, 1))

book_pairs_freq = book_pairs.reduceByKey(lambda a, b: a + b)

filtered_pairs = book_pairs_freq.filter(lambda a: a[1] > 20)

filtered_pairs.saveAsTextFile("/home/cs143/output1")