from time import sleep
import os
import json
import requests
import socketio
sio = socketio.Client()
sio.connect('http://localhost:5000')


#import pprint
#pp = pprint.PrettyPrinter(indent=4)

with open('main.py', "r") as file:
    code = file.read()

with open('body.json', "r+") as file: 
    data = json.load(file)
    data['code'] = code
    file.seek(0)
    json.dump(data, file, indent=4)

    
    
#might have to look up how to get authorization header (maybe manually from website)
response = requests.post("https://www.codewars.com/api/v1/runner/authorize", headers={"authorization": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVlNWJhMGIzMDE3MTIyMDAyZTRiOTU2MiIsImV4cCI6MTYxNTM4MzM4M30.WSCOGTgS6ocDza4dLlChblRgtzCrN0e4mIEexYoY1Mg"})
authToken = response.json()["token"]


response = requests.post("https://runner.codewars.com/run", headers={"authorization": f"Bearer {authToken}"}, json=data).json()
# print(type(response))
#pp.pprint(response)
sleep(1)
sio.emit('inData', response)



#for key in response:
    #print(key, response[key])

sleep(1)
os._exit(1) # sucide