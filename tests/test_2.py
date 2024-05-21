import requests
import json

def predict(dict_features):    
    # Send input data to prediction API
    req_post = requests.post(   url     = 'http://13.92.86.145:5678/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = json.dumps({'inputs': dict_features}) )
    # Get predicted value from API
    dict_predicted = json.loads(req_post.text)

def test_prediction():    
    for in_1, in_2, out_i in [
                        (.2, .2, 1),
                        (.3, .3, 1),
                        (.4, .4, 1) ] :
        dict_features_i  = {'umap_x':[str(in_A)],'umap_y':[str(in_B)]}
        dict_predicted_i = predict(dict_features)
        dict_expected_i  = {'predictions':[out_i]}
        print('input features  :', dict_features)
        print('output predicted:', dict_predicted)
        print('output expected :', dict_expected)

        # Compare predicted & expected values
        assert dict_predicted == dict_expected

