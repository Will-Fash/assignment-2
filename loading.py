#!/usr/bin/env python3
from elasticsearch import Elasticsearch 
from elasticsearch import helpers
from elasticsearch_dsl.connections import connections
import csv

filename = 'SA.csv'


es = Elasticsearch(hosts=["http://13.58.129.201:9200"], timeout=5000) # Define a default Elasticsearch client

with open(filename, "r", encoding="utf8") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='it', doc_type='my-type')
