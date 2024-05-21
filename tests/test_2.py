import requests
import json

def test_prediction():    
    dict_features = {"umap_x":[".3"],"umap_y":[".3"]}
    req_post = requests.post(   url     = 'http://http://13.92.86.145:5678/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )
    dict_prediction = json.loads(req_post.text)
    assert dict_prediction == {"predictions":[1]}

