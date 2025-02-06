# qGISparsing
Set of data parsing tools ready to plug into qGIS

Prompts
#extractHouseNum
coalesce(extractHouseNum(coalesce("streetname")))

#removeHouseNum
coalesce(removeHouseNum(  "streetname" ,  "housenum" ),  "streetname" )

#extractPredir
coalesce(extractPredir(  "streetname" ))

#removePredir
coalesce(removePredir(  "streetname" , "predir" ),  "streetname" )

#extractSufdir
coalesce(extractSufdir(  "streetname" ))

#removeSufdir
coalesce(removeSufdir( "streetname" ,  "sufdir" ),  "streetname" )

#extractStreettype
coalesce(extractStreetType(  "streetname" ))

#removeStreettype
coalesce(removeStreetType(  "streetname" , "streettype" ),  "streetname" )

removeSpace("fulladdress")
drop("fulladdress")
removeSpace("streetname")
drop("streetname")
loopat("streetname")
dropSplit("fulladdress")
dropSplit("streetname")
