from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

def fetch_job_data():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.jobejee.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.jobejee.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'page': '0',
        'size': '10',
    }

    json_data = {
        'funcArea': None,
        'industry': None,
        'jobType': None,
        'exp': None,
        'location': 'Kathmandu',
        'searchKey': 'Manager',
    }

    response = requests.post('https://api.v1.jobejee.com/v2/jobSearch', params=params, headers=headers, json=json_data)
    jobs = response.json()

    job_list = []

    for job in jobs['data']:
        job_details = {
            'Title': job.get('title'),
            'Company Name': job.get('company_name'),
            'Location': job.get('location'),
            'Experience Min': job.get('exp_min'),
            'Experience Max': job.get('exp_max'),
            'Key Skills': job.get('key_skills'),
            'Published On': job.get('publish_on'),
            'Expiry Date': job.get('job_expiry'),
            'Views': job.get('views'),
        }
        job_list.append(job_details)

    return job_list

@app.route('/')
def index():
    job_data = fetch_job_data()
    return render_template('index.html', jobs=job_data)

if __name__ == '__main__':
    app.run(debug=True)
