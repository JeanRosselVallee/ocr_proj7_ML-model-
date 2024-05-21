import requests
def test_conncection():    
    req_post = requests.post(   url     = 'http://13.92.86.145:5678/invocations', 
                                headers = {'Content-Type': 'application/json'}, 
                                data    = '{"inputs": {"umap_x": [".3"], "umap_y": [".3"]}}' )
    assert req_post.ok == True

