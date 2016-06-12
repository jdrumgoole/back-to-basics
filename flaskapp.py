'''
Created on 24 May 2016

@author: jdrumgoole
'''

import pymongo
from flask import Flask, request
app = Flask(__name__)
mc = pymongo.MongoClient()
db = mc[ "blog"]
usersCollection = db["users"]
articlesCollection = db[ 'articles']

@app.route("/")
def index():
    return "Home page"


@app.route( '/user/<username>')
def getUser( username ):
    user = usersCollection.find_one( { "username" : username })
    
    if user :
        return ( "User: %s " % user )
    else:
        return ( "No such user: %s" % username )
     
@app.route( '/article/<int:articleID>')
def getArticle( articleID ):
    article = articlesCollection.find_one( { "_id" :  articleID })
    
    if article :
        return ( "Article: %s " % article )
    else:
        return ( "No such article: %s" % articleID )
    
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return "username: %s" % request.form[ "username"]
    else:
        return "not a post request"

if __name__ == "__main__":
    app.run( debug=True)