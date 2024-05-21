import requests
import json

def result():    
    dict_features = {"umap_x":[".3"],"umap_y":[".3"]}
    req_post = requests.post(   url     = 'http://localhost:5678/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )
    dict_prediction = json.loads(req_post.text)     #{"predictions":[1]}
    assert dict_prediction == {"predictions":[1]}

