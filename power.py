import requests, json, sys, re, time, warnings
from datetime import datetime

# time
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

warnings.filterwarnings("ignore")
stringTomatch = 'username_idrac:'
matchedLine_username = ''
with open('login_account','r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine_username = line
                break

stringTomatch = 'password_idrac:'
matchedLine_password = ''
with open('login_account','r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine_password = line
                break
    
with open('host_list', 'r') as file:
    idrac_ip=file.readlines()
    print(idrac_ip)

try:
    #idrac_ip = sys.argv[1]
    #idrac_username = sys.argv[2]
    #idrac_password = sys.argv[3]

    idrac_username = matchedLine_username
    idrac_password = matchedLine_password

except:
    print("- FAIL: You must pass in script name along with iDRAC IP / iDRAC username / iDRAC password. Example: \"script_name.py 192.168.0.120 root calvin\"")
    sys.exit()

for index in idrac_ip:
    print(index)
    response = requests.get('https://%s/redfish/v1/Chassis/System.Embedded.1/Power' % index,verify=False,auth=(base64.b64decode("idrac_username".decode("utf-8")), base64.b64decode("idrac_password".decode("utf-8")))
    data = response.json()
#print("\n-  %s\n" % data[u'PowerControl'])
    print("- Consumed Power :\n")
    print('Time stamp: %(time)s - Server IP: %(ip)s -   Power: %(power)s Watts' %{"time": date_time,"ip": index,"power": data[u'PowerControl'][0][u'PowerConsumedWatts']})