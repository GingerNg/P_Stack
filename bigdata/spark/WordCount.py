# coding=utf-8
import logging
from operator import add

from pyspark import SparkContext

""" 
@version: 
@software: PyCharm 
@file: test_python_word_count.py 
"""

logging.basicConfig(format='%(message)s', level=logging.INFO)

test_file_name = "/home/XX/words"
out_file_name = "/home/XXX/spark-out"  # spark-out is a fold

# Word Count
sc = SparkContext("local", "Simple App")
# text_file rdd object
text_file = sc.textFile(test_file_name)
# counts
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile(out_file_name)