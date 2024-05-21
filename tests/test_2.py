import requests
import json

def predict(dict_features):    

    print("input features:", dict_features)

    # Send input data to prediction API
    req_post = requests.post(   url     = 'http://13.92.86.145:5678/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )

    # Output
    dict_expected = {"predictions":[1]}
    print("output expected:", dict_expected)

    # Get predicted value from API
    dict_predicted = json.loads(req_post.text)
    print("output predicted:", dict_predicted)

    # Compare predicted & expected values
    assert dict_predicted == dict_expected

def test_prediction():    
    # Inputs
    dict_features = {"umap_x":[".3"],"umap_y":[".3"]}
    dict_predicted = predict(dict_features)
