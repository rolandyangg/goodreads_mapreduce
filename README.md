# goodreads_mapreduce

Pyspark scripts that use the Apache Spark engine to utilize the MapReduce framework to analyze data on reviewers and book data from the GoodReads service.

The dataset these computations are performed on is too large to do with a simple script and single job, so we use MapReduce to help us.

titlePairs.py simply emits key pairs of books that appear together in pairs user reviews. 

bookPairs.py uses Spark and MapReduce to aggregate these key pairs and perform computations on them, returning the frequency that such pairs appear together. We then later sort it.