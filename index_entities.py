#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Jun 9, 2020

.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

Index HDT KG labels into ES

To restart indexing:

1. Delete previous index
curl -X DELETE "localhost:9200/freebase201312e"

2. Put mapping (see mapping.json file)
curl -X PUT "localhost:9200/freebase201312e" -H 'Content-Type: application/json' -d'
...

3. Run this script. Check progress via
curl -XGET "localhost:9200/freebase201312e/_count"

'''

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk
from elasticsearch import TransportError

# setup
es = Elasticsearch()
doc_type = 'entities'  # for mapping

import re
import string


# pre-processing
def parse_label(entity_label):
    entity_label = " ".join(re.sub('([a-z])([A-Z])', r'\1 \2', entity_label.rstrip().lstrip()).split())
    words = entity_label.split(' ')
    unique_words = []
    for word in words:
        # strip punctuation
        word = "".join([" " if c in string.punctuation else c for c in word])
        if word:
            word = word.lower()
            if word not in unique_words:
                unique_words.append(word)
    entity_label = " ".join(unique_words)
    return entity_label


# define streaming function
def uris_stream(index_name, file_path, doc_type, ns_filter=None):
    with io.open(file_path, "r", encoding='utf-8') as infile:
        for i, line in enumerate(infile):
            # skip URIs if there is a filter set
            if ns_filter:
                if not line.startswith(ns_filter):
                    continue
            # line example http://rdf.freebase.com/ns/american_football.football_player.games;11;Games
            parse = line.split(';')
            entity_uri = parse[0]
            count = parse[1]
            entity_label = parse[2].strip()
            label_words = parse_label(entity_label)

            data_dict = {'uri': entity_uri, 'label': label_words,
                         'count': count, "id": i+1, 'label_exact': entity_label}

            yield {"_index": index_name,
                   "_type": doc_type,
                   "_source": data_dict
                   }

# index entities
import io
KB = 'freebase201312'  # dbpedia201604 or wikidata201809
file_path = "freebase-rdf-2013-12-01-00-00Entities.txt"
index_name = '%se' % KB  # entities index

# iterate through input file in batches via streaming bulk
print("bulk indexing...")
try:
    for ok, response in streaming_bulk(es, actions=uris_stream(index_name, file_path, doc_type),
                                       chunk_size=100000):
        if not ok:
            # failure inserting
            print (response)
except TransportError as e:
    print(e.info)
    
print("Finished.")
