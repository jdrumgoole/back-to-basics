'''
Created on 18 May 2016

@author: jdrumgoole
'''

import base64
import bson
from bson.binary import Binary

imgData = None

with  open( "mongodb-logo.jpg" , "rb" ) as imgFile :
    imgData = imgFile.read()

bsonImage = base64.standard_b64encode( imgData )

newImgData = base64.standard_b64decode( bsonImage )

with open( "base64.jpg", "wb" ) as imgFile :
    imgFile.write( newImgData )

with  open( "mongodb-logo.jpg" , "rb" ) as imgFile :
    imgData = imgFile.read()

bsonImage = Binary( imgData )

newImgData = bytearray().decode( "base64" )

with open( "binary.jpg", "wb" ) as imgFile :
    imgFile.write( newImgData )