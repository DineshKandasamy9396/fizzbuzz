def get_interface():
 global Auth_token
 Auth_token= (ticket.response.json()["response"]["serviceTicket"]) 
 print(Auth_token)

 controller='sandboxapic.cisco.com'
 #controller='devnetapi.cisco.com/sandbox/apic_em'

 # put the ip address or dns of your apic-em controller in this url
 url = "https://" + controller + "/api/v1/network-device/"

 #the username and password to access the APIC-EM Controller
 """ payload = {"username":"devnetuser","password":"Cisco123!"}"""

 #Content type must be included in the header
 header = {"content-type": "application/json","X-Auth-Token":Auth_token}

 #Performs a POST on the specified url to get the service ticket
 response= requests.get(url, headers=header, verify=False)

 #convert response to json format
 r_json=response.json()

 print(r_json["response"])

def get_network_count():

 controller='sandboxapic.cisco.com'
 #controller='devnetapi.cisco.com/sandbox/apic_em'

 # put the ip address or dns of your apic-em controller in this url
 url = "https://" + controller + "/api/v1/network-device/count"

 #the username and password to access the APIC-EM Controller
 """ payload = {"username":"devnetuser","password":"Cisco123!"}"""

 #Content type must be included in the header
 header = {"content-type": "application/json","X-Auth-Token":Auth_tok$

 #Performs a POST on the specified url to get the service ticket
 response= requests.get(url, headers=header, verify=False)

 #convert response to json format
 r_json=response.json()
 
 print(r_json)

ticket = __import__("create-ticket")
import requests
import json
get_interface()
get_network_count()

