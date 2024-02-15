#Match fieldA from FileA to "fieldB" in "FileB"
If the similarity score is >=.9 then add the fieldA,fieldB and similarity score to a new file "result".
If the similarity score is <.9 then 
   Do a match betweeen those records which have similarity score < .9  and fieldC of records in FileC
   If the similarity score is >=.9 then add the fieldA,fieldC and similarity score to file "result".   
