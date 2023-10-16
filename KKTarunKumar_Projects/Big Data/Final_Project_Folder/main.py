import socket
import time
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row,SQLContext,SparkSession
import pandas as pd
import pyspark.sql.types as tp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import json
import requests

if __name__ == '__main__' : 
	conf = SparkConf()
	conf.setMaster("local[2]")
	conf.setAppName("TwitterSentimentalAnalysis")

	sc = SparkContext.getOrCreate(conf=conf)
	sc.setLogLevel("WARN")
	spark = SparkSession(sc)
	ssc = StreamingContext(sc,1)
	ssc.checkpoint("checkpoint_TwitterApp")
	sql_context = SQLContext(sc)
	ssc = StreamingContext(sc,1)
	
	tweetlines = ssc.socketTextStream('localhost',6100)
	try:
		tweetlines.pprint()
	except:
		print("Data unavailable")

	ssc.start()
	ssc.awaitTermination(1000)