# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 22:16:09 2019

@author: anuryadav
"""

from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params
from datetime import datetime
from elasticsearch import Elasticsearch
import json
from flask_cors import CORS

# needs changes
es = Elasticsearch(['http://135.36.0.89:9201'])

app = Flask(__name__)
CORS(app)
#cord = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'secret'
# bind rails like params to request.params
app.before_request(bind_request_params)


@app.route('/fraud/detect', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    print('Request recieved: ',req_data)
    
    

    caseNo = req_data['caseNum']
    
   #boolean_test = req_data['boolean_test']
   
    #response = connectToEs(caseNo,indivId)
    
    print('values caught from request', caseNo)
    
    if 'indiv_id' in req_data:
        indivId = req_data['indiv_id']
        print('query: {"bool":{"must":[{"match":{"indv_id":',indivId,'}},{"match":{"case_num":',caseNo,'}}]}}}')
        res = es.search(index="es_fraud_detect_v3", body={"size": 100,"query":{"bool":{"must":[{"match":{"indv_id":indivId}},{"match":{"case_num":caseNo}}]}}})
    else:
        print('query  {"size": 100,"query":{"bool":{"must":[{"match":{"case_num":',caseNo,'}}]}}} ')
        res = es.search(index="es_fraud_detect_v3", body={"size": 100,"query":{"bool":{"must":[{"match":{"case_num":caseNo}}]}}})

    # c 501102254 ; i 138160
    print("Got %d Hits:" % res['hits']['total'])
    totalHits = res['hits']['total']
    print("response from es", res)
    # fraud can be detected only if no of hits are more than 1 else its marked as non fraud.
   # if totalHits > 1:
    counter = 0
    responseList = []
   # res[]
    for hit in res['hits']['hits']:
        
        
        # commom for all
        res = {"first_name": hit["_source"]["first_name"],
               "last_name": hit["_source"]["last_name"],
               "indv_id": hit["_source"]["indv_id"],
               "case_no": hit["_source"]["case_num"],
               "other_income_amt": "PASS",
               "aid_request_sw": "PASS",
               "active_in_case_sw": "PASS",
               "us_citizen_sw": "PASS",
               "residency_state_cd": "PASS",
               "prog_cd": "PASS"}
        
        print("%(first_name)s %(last_name)s:  %(aid_request_sw)s: %(active_in_case_sw)s  %(us_citizen_sw)s: %(residency_state_cd)s %(prog_cd)s: %(other_income_amt)s" % hit["_source"])
        
        if counter != 0:
            # need all the param to be not null
            
            if hit["_source"]["aid_request_sw"] != hit_first["_source"]["aid_request_sw"]:                
                res["aid_request_sw"] = "FAIL"
             
            if hit["_source"]["active_in_case_sw"] != hit_first["_source"]["active_in_case_sw"]:                
                res["active_in_case_sw"] = "FAIL"
                
            if hit["_source"]["other_income_amt"] != hit_first["_source"]["other_income_amt"]:                
                res["other_income_amt"] = "FAIL"
            
            if hit["_source"]["us_citizen_sw"] != hit_first["_source"]["us_citizen_sw"]:                
                res["us_citizen_sw"] = "FAIL"
             
            if hit["_source"]["residency_state_cd"] != hit_first["_source"]["residency_state_cd"]:                
                res["residency_state_cd"] = "FAIL"
                
            if hit["_source"]["prog_cd"] != hit_first["_source"]["prog_cd"]:                
                res["prog_cd"] = "FAIL"
                
            responseList.append(res)
            hit_first = hit
        
            counter = counter + 1
        else:
            counter = counter + 1
            hit_first = hit
            
            responseList.append(res)
    #else:
     #   response = json.dumps({"first_name": "Passed by 1" })
        
    return json.dumps(responseList)

# to check if API is up
@app.route('/')
def hello_world():
    return 'Hello! I am up and running'
#def connectToEs(caseNo,indivId):
    

# serve at localhost:5000
app.run(debug=True)