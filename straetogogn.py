import requests
import xmltodict
import json
import os
import dotenv

dotenv.load_dotenv()

straeto_url = os.getenv('STRAETO_URL')

res = requests.get(straeto_url)
dict_data = xmltodict.parse(res.content)

print(dict_data['busstate']['bus'][0]['@route'])

def parse_csv(inp):
    # print(inp)
    outp = []
    headers = inp[0].split(',')
    for row in inp[1:]:
        outp.append({k:v for k,v in zip(headers,row)})


with open('straeto_data/stops.txt','r') as f:
    stops_data = parse_csv(f.readlines())

with open('out.json','w') as f:
    f.write(json.dumps(dict_data,indent=2))


# print(stops_data)
