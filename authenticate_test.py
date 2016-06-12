'''
Created on 9 Jun 2016

@author: jdrumgoole
'''

import pymongo
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='loader for MOT data', prog = "pyfastloader")
    parser.add_argument('--database', default="", help='specify the database name')
    parser.add_argument('--collection', default="test", help='specify the collection name')
    parser.add_argument('--host', default="localhost", help='hostname')
    parser.add_argument('--port', default="27017", help='port name', type=int)
    parser.add_argument('--username', default=None, help='username to login to database')
    parser.add_argument('--password', default=None, help='password to login to database')
    parser.add_argument('--ssl', default=False, action="store_true", help='use SSL for connections')
    
    
    args= parser.parse_args()

# uri = "mongodb://user:password@example.com/the_database?authMechanism=SCRAM-SHA-1"
    #mc = pymongo.MongoClient("mongodb://jdrumgoole:jdjkdr775@vosa-shard-00-00-ffp4c.mongodb.net:27017/vosa?authMechanism=SCRAM-SHA-1")
    
    mc = pymongo.MongoClient( host="vosa-shard-00-00-ffp4c.mongodb.net", ssl=True)
    database = mc[ "vosa"]
    result = database.authenticate( "jdrumgoole", "jdjkdr775", mechanism='SCRAM-SHA-1')
    
    if result:
        collection = database[ "results"]
        collection.insert_one(  {"test" : "hello" } )
        x = collection.find_one()
        print( x )
    else:
        print( "auth failed")
    