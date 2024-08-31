# This script is build for Elasticsearch Database
# You can use any database you want

from elasticsearch import Elasticsearch

class ElasticClient:
    def __init__(self, host):
        self.es_client = Elasticsearch(host)
    
    def insert(self, index, body, id, doc_type="doc"):
        self.es_client.index(index=index, doc_type=doc_type, id=id, body=body)
    
    def update(self, index, id, body, doc_type="doc"):
        self.es_client.update(index=index, doc_type=doc_type, id=id, body=body)
    
    def delete(self, index, id):
        self.es_client.delete(index=index, id=id)

    #CHECKOUT
    def search(self, index, query, source_exclude=None, source_include=None):
        return self.es_client.search(index=index, body=query, _source_excludes= source_exclude, _source_includes=source_include)
    
     
        