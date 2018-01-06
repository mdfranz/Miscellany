#!/usr/bin/python

import requests, json, csv, os

api_key = os.environ['DD_APIKEY']
application_key = os.environ['DD_APPKEY']

url = "https://app.datadoghq.com/reports/v2/overview?api_key="+api_key+"&application_key="+application_key+"&window=3h&metrics=avg%3Asystem.cpu.idle%2Cavg%3Aaws.ec2.cpuutilization%2Cavg%3Avsphere.cpu.usage%2Cavg%3Aazure.vm.processor_total_pct_user_time%2Cavg%3Asystem.cpu.iowait%2Cavg%3Asystem.load.norm.15&with_apps=true&with_sources=true&with_aliases=true&with_meta=true&with_mute_status=true&with_tags=true"
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.get(url,headers=headers)

if r.status_code == 200:
	data = r.json()

	for hosts in data["rows"]:
		if "platform" in hosts["meta"].keys():
			if hosts["meta"]["platform"] == "linux2":
				gohai = json.loads(hosts["meta"]['gohai'])
				print gohai['platform']['hostname'] + " | " + gohai['platform']['kernel_release'] + " | " +  gohai['platform']['kernel_version']

