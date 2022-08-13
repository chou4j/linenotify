# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:20:25 2022

@author: chou4
"""
import requests
import os
from apscheduler.schedulers.blocking import BlockingScheduler

os.chdir('C:\\Python')
#os.chdir('D:\\Python')

Authorization = 'CWB-D668B252-152F-4107-9170-B232D2418CFF'
city = '新北市'
#city = '臺北市'

token = 'MGTpRenD39hIcOOnp3rBNdw5LYHbc7GQMqIg1ANvpDw'
#和張的共同群組

#token = 'qY2TNlwc4foEhTiS7rJrst5b7HG7qcmqRlDeYi2nrUm'
#family的群組

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code



def main():
    requests.packages.urllib3.disable_warnings()
    r = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/W-C0033-001?Authorization="+Authorization+"&format=JSON&locationName="+city, verify=False)
    list_of_dicts = r.json()
    webtext = list_of_dicts['records']['location'][0]['hazardConditions']['hazards']
    
    path = 'weather1t.txt'
    f = open(path, 'r' )
    text = f.read()
    f.close()
    
    
    if webtext == []:
        message = "現在新北市無天氣警特報"
        if message == text :
            print('NO SHOW，新北市無天氣警特報')
        else:
            path = 'weather1t.txt'
            f = open(path, 'w')
            f.write(message)
            f.close()
            print(message)
            lineNotifyMessage(token, message)
    else:
        phenomena = list_of_dicts['records']['location'][0]['hazardConditions']['hazards'][0]['info']['phenomena']
        significance = list_of_dicts['records']['location'][0]['hazardConditions']['hazards'][0]['info']['significance']
        startTime = list_of_dicts['records']['location'][0]['hazardConditions']['hazards'][0]['validTime']['startTime']
        endTime = list_of_dicts['records']['location'][0]['hazardConditions']['hazards'][0]['validTime']['endTime']
        message = "現在新北市為" + phenomena + significance +"發布時間為" + startTime +"至" +endTime
        if message == text :
            print('NO SHOW')
        else:
            path = 'weather1t.txt'
            f = open(path, 'w')
            f.write(message)
            f.close()
            print(message)
            lineNotifyMessage(token, message)
            return

if __name__ == "__main__":
    main()
    scheduler = BlockingScheduler()
    #scheduler = BlockingScheduler(job_defaults=job_defaults)
    # scheduler = BlockingScheduler()
    # scheduler.add_job(main, 'interval', minutes=schedule_interval)
    scheduler.add_job(main, 'interval', seconds=600)
    scheduler.start()
