import requests
import xmltodict
import json
import os
import dotenv
import glob

dotenv.load_dotenv()

# straeto_url = os.getenv('STRAETO_URL')

# res = requests.get(straeto_url)

xml_dir = 'xml_data/2025/04/04'
all_xml_files = os.listdir(xml_dir)
# print(all_xml_files)

for file in all_xml_files:
    with open(os.path.join(xml_dir,file), 'r') as  f:
        xml = f.read()
    dict_data = xmltodict.parse(xml)
    for bus in dict_data['busstate']['bus']:
        if bus['@route'] == '14' and bus['@stop'] == '90000022':
            print(bus)

print(dict_data['busstate']['bus'][0]['@route'])

# with open('out.json','w') as f:
#     f.write(json.dumps(dict_data,indent=2))


# # print(stops_data)
