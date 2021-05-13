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
es = Elasticsearch(['http://localhost:9200'])

app = Flask(__name__)
CORS(app)
#cord = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'secret'
# bind rails like params to request.params
app.before_request(bind_request_params)


@app.route('/fraud/detect', methods=['POST']) #GET requests will be blocked
def detect_fraud():
    req_data = request.get_json()
    print('Request recieved: ',req_data)
    
    

    caseNo = (req_data['caseNum']).strip()
    
    print('{"size":0,"query":{"match":{"case_num":',caseNo,'}},"aggs":{"indivs":{"terms":{"field":"indv_id","size":10}}}}')
    resIndivId = es.search(index="es_fraud_detect_v1", body={"size":0,"query":{"match":{"case_num":caseNo}},"aggs":{"indivs":{"terms":{"field":"indv_id","size":10}}}})
    
  
    counter = 0
    responseList = []
    
   # res[]
    for hit in resIndivId['aggregations']['indivs']['buckets']:
        
        individual = resIndivId['aggregations']['indivs']['buckets'][counter]['key']
        
        print('indiv found: ',resIndivId['aggregations']['indivs']['buckets'][counter]['key'])
        
        print('query: {"size": 1000,"query":{"bool":{"must":[{"match":{"case_num":',caseNo,',}},{"match":{"indv_id":',individual,',}}]}},"sort":[{"policy_year":{"order":"asc"}}]}')
        resPerIndividual = es.search(index="es_fraud_detect_v1", body={"size": 1000,"query":{"bool":{"must":[{"match":{"case_num":caseNo}},{"match":{"indv_id":individual}}]}},"sort":[{"policy_year":{"order":"asc"}}]})
        #print(resPerIndividual)
        
        response = {"first_name": resPerIndividual['hits']['hits'][0]['_source']["first_name"],
               "last_name": resPerIndividual['hits']['hits'][0]['_source']["last_name"],
               "indv_id": resPerIndividual['hits']['hits'][0]['_source']["indv_id"],
               "case_no": resPerIndividual['hits']['hits'][0]['_source']["case_num"],
               "other_income_amt": "PASS",
               "aid_request_sw": "PASS",
               "active_in_case_sw": "PASS",
               "us_citizen_sw": "PASS",
               "residency_state_cd": "PASS",
               "prog_cd": "PASS"}
        # print('dummy response', response, 'counter ', counter)
        
      
        for i in range(len(resPerIndividual['hits']['hits'])-1):
            
            
            hit = resPerIndividual['hits']['hits'][i]
            hit_next = resPerIndividual['hits']['hits'][i+1]
                
            if hit["_source"]["aid_request_sw"] != hit_next["_source"]["aid_request_sw"]:                
                response["aid_request_sw"] = "FAIL"
             
            if hit["_source"]["active_in_case_sw"] != hit_next["_source"]["active_in_case_sw"]:                
                response["active_in_case_sw"] = "FAIL"
            
            if hit["_source"]["us_citizen_sw"] != hit_next["_source"]["us_citizen_sw"]:                
                response["us_citizen_sw"] = "FAIL"
             
            if hit["_source"]["residency_state_cd"] != hit_next["_source"]["residency_state_cd"]:                
                response["residency_state_cd"] = "FAIL"
                
            if hit["_source"]["prog_cd"] != hit_next["_source"]["prog_cd"]:                
                response["prog_cd"] = "FAIL"
                
            current = float(hit["_source"]["other_income_amt"])
            next_one = float(hit_next["_source"]["other_income_amt"])
            
           # print('current', current, ' next', next_one,' per diff: ', abs(current - next_one) / current * 100)
            print('current', current, ' next', next_one,' per difference: ', (next_one - current)  / current)


            if (next_one - current) / current * 100 > 10:
                response["other_income_amt"] = "FAIL"
            
            i = i+1
        counter = counter + 1
            
        responseList.append(response)
            
    return json.dumps(responseList)        
       
# to check if API is up
@app.route('/')
def hello_world():
    return 'Hello! I am up and running'
#def connectToEs(caseNo,indivId):
    

# serve at localhost:5000
app.run(debug=True,host = '0.0.0.0', port = '5000')
