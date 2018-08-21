import sys
from colorama import init
from termcolor import colored
import json
import os

username = "admin"
password = "Lak@1993"

init()
 
#answer = input(colored('This is going to disable all your alerts. Do you still want to continue?', 'white', 'on_red'))
action = str(raw_input(colored('What do you want?' + ' (enable/disable): ', 'white', 'on_red'))).lower().strip()
answer = str(raw_input(colored('This is going to %s all your alerts. Do you still want to continue?' + ' (yes/no): ', 'white', 'on_red') % action)).lower().strip()

#print action

if action == "disable" and answer == "yes":
    os.remove("alerts.json")
    f = open("alerts.json", "w+")
    os.system('curl -k -u "admin:Lak@1993" https://localhost:8089/servicesNS/-/search/saved/searches?"output_mode=json" >> alerts.json')
        
    alerts = []

    with open('alerts.json') as json_data:
        data = json.load(json_data)

    f.close()

    for item in data["entry"]:
        alerts.append(item["id"])     
        
    for i in range(len(alerts)):
        if "Kolla" in alerts[i]:
            alerts[i] += "/disable"
            kolla = alerts[i]
            os.system('curl -k -u "admin:Lak@1993" -d output_mode=json >> test.json %s' % kolla)
            print(colored("%s has been disabled", 'white', 'on_green') % alerts[i])
elif action == "enable" and answer == "yes":
    os.remove("alerts.json")
    f = open("alerts.json", "w+")
    os.system('curl -k -u "admin:Lak@1993" https://localhost:8089/servicesNS/-/search/saved/searches?"output_mode=json" >> alerts.json')

    alerts = []

    with open('alerts.json') as json_data:
        data = json.load(json_data)

    f.close()

    for item in data["entry"]:
        alerts.append(item["id"])

    for i in range(len(alerts)):
        if "Kolla" in alerts[i]:
            alerts[i] += "/enable"
            kolla = alerts[i]
            os.system('curl -k -u "admin:Lak@1993" -d output_mode=json >> test.json %s' % kolla)
            print(colored("%s has been enabled", 'white', 'on_green') % alerts[i])
elif action == "enable" and answer == "no":
    print(colored("No alert has been enabled", 'white', 'on_green'))
elif action == "disable" and answer == "no":
    print(colored("No alert has been disabled", 'white', 'on_green'))
else:
    print(colored("Please enter enable or disable first and then enter yes or no.", 'white', 'on_red'))
