import requests
import os
import dotenv
import datetime


import hashlib
import subprocess

import time


dotenv.load_dotenv()

straeto_url = os.getenv('STRAETO_URL')



def log_file_hash_to_repo(xml_file_absolute_path, xml_file_relative_filename, repo_path, log_filename="straeto_hashes.csv"):
    # 1. Compute SHA-256 hash
    with open(xml_file_absolute_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()


    # 3. Append to hash log
    log_path = os.path.join(repo_path, log_filename)
    with open(log_path, "a") as log:
        log.write(f"{xml_file_relative_filename},{file_hash}\n")

    # 4. Git commit the updated log
    subprocess.run(["git", "add", log_filename], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", f"Log hash for {xml_file_relative_filename}"], cwd=repo_path)
    # Optional:
    # subprocess.run(["git", "push"], cwd=repo_path)

def fetch_newest_xml_data():
    res = requests.get(straeto_url)
    fetched_timestamp = datetime.datetime.now()

    if fetched_timestamp.hour < 4:
        service_date = (fetched_timestamp - datetime.timedelta(days=1)).date()
    else:
        service_date = fetched_timestamp.date()

    year = service_date.strftime("%Y")
    month = service_date.strftime("%m")
    day = service_date.strftime("%d")



    xml_data_path = 'xml_data'

    folder_path = f"{xml_data_path}/{year}/{month}/{day}"
    file_path = f'straeto_rauntimagogn_{fetched_timestamp.strftime("%Y-%m-%d_%H-%M-%S")}.xml'
    os.makedirs(folder_path,exist_ok=True)

    with open(os.path.join(folder_path, file_path), 'wb') as f:
        f.write(res.content)

    log_file_hash_to_repo(xml_file_absolute_path=os.path.abspath(os.path.join(folder_path,file_path)),xml_file_relative_filename=file_path,repo_path='/Users/odinndagur/Code/2025/straeto_rauntimagogn_hashes/')


while True:
    fetch_newest_xml_data()
    time.sleep(5)