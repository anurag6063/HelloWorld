import cx_Oracle
import json
con = cx_Oracle.connect('docsafe/docsafe@nonprod-scan.ash.broadcom.net:1535/LRCSPTST')
cur = con.cursor()
userid='11371'
#cur.execute('select C.userid, A.documentid, A.box_file_id from DC_DOCUMENTS_BOX A left join dc_documents B on A.documentid = B.documentid left join dc_permissions C on B.DOCFILEID = to_char(C.documentid) where A.Box_file_id=121533667637')
cur.execute('select A.box_file_id from DC_DOCUMENTS_BOX A left join dc_documents B on A.documentid = B.documentid left join dc_permissions C on B.DOCFILEID = to_char(C.documentid) where C.USERID='+userid)
print(userid);

#my_json_string = json.dumps({'userid':  userid , "key2": "Value2"})
#print(my_json_string)

response_json={};
response_json["userids"]=userid;
docids=[];
for result in cur:
    print('from DB '+result)
    docids.append({"doc": result})
    print('current Doc Id '+docids)
    
response_json["docids"]=docids
#print (json.dumps(response_json, indent=2))
with open('abc.json', 'w') as outfile:
  json.dump(response_json,outfile)
cur.close()
con.close() 
