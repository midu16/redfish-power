#
# Idu Mihai - 2020
#


import sys
import redfish
import base64

# When running remotely connect using the address, account name, 
# and password to send https requests
login_host = "https://192.168.1.100"
login_account = "admin"
login_password = "password"


stringTomatch = 'username_idrac:'
matchedLine = ''
with open('login_account','r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                break

login_account_idrac=matchedLine
#login_account_idrac=base64.b64encode("matchedLine".encode("utf-8"))

stringTomatch = 'password_idrac:'
matchedLine = ''
with open('login_account','r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                break

login_password_idrac=matchedLine
#login_account_idrac=base64.b64encode("matchedLine".encode("utf-8"))

## Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=login_host, username=base64.b64decode("login_account_idrac".decode("utf-8")), \
                          password=base64.b64decode("login_password_idrac".decode("utf-8")), default_prefix='/redfish/v1')

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

# Do a GET on a given path
response_idrac = REDFISH_OBJ.get("/redfish/v1/Chassis/System.Embedded.1/Power", None)

response_ilo = REDFISH_OBJ.get("/redfish/v1/Chassis/1/Power", None)

# Print out the response
sys.stdout.write("%s\n" % response_idrac)

# Logout of the current session
REDFISH_OBJ.logout()