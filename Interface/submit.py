
import json
import requests
import urllib3






#with open('1AKI_clean.pdb','rb') as payload:
 #   headers = {'content-type': 'application/x-www-form-urlencoded'}
  #  r = requests.post('http://127.0.0.1:5000/editconf',
   #                   data=payload, verify=False, headers=headers)




#body, header = urllib3.encode_multipart_formdata(fields)

response1 =requests.post('http://127.0.0.1:5000/stagecalculation')
#response = requests.post('http://127.0.0.1:5000/editconf', data=body, headers={'Content-Type': header})

idcalc = response1.content.decode()
fields = {
"id" : idcalc,
"-f":"1AKI_processed.gro",
"-o":"1AKI_newbox.gro",
"-c":"True",
"-d":"1.0",
"-bt":"cubic",
"file": ("1AKI_processed.gro", open("1AKI_processed.gro").read()),
}

body, header = urllib3.encode_multipart_formdata(fields)

response = requests.post('http://127.0.0.1:5000/editconf', data=body, headers={'Content-Type': header})

print("response is  " + idcalc)

data = {"id":idcalc}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

response = requests.post('http://127.0.0.1:5000/finishcalculation', data=json.dumps(data), headers=headers)




