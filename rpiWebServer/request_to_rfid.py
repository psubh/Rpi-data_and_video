import requests

url = "10.10.20.135:3000/rfid"

data = '{"rfid":"1012998082138"}'

r = requests.post(url,data=data)

print(r.text)