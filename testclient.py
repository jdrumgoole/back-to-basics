'''
Created on 18 May 2016

@author: jdrumgoole
'''
import requests

r = requests.get( "http://localhost:5000/cms/articles")

r = requests.put( "http://localhost:5000/cms/users", { "username" : "jdrumgoole" , "password" : "top secret"} )