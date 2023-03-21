from flask import Flask, request
import json
import  pprint
import requests
token = "6a4515364e8584e466f6b2071231aefa0f283726"
link_input = input("enter your url: ")
data = {
    "group_guid": "Bmc7bJDLA8n",
    "domain": "bit.ly",
    "long_url": f"{link_input}"
}
f_json = open("v4.json")

json_load = json.load(f_json)
x = requests.post(url=f"https://api-ssl.bitly.com/v4/shorten",data=json.dumps(data),headers={"Authorization": f"Bearer {token}"})
pprint.pprint(x.json())
f_json.close()