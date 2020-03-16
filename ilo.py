import sys
import json
import redfish
import hell
import pprint
# When running on the server locally use the following commented values
# HOST = "blobstore://."
# LOGIN_ACCOUNT = "None"
# LOGIN_PASSWORD = "None"

# When running remotely connect using the iLO address, iLO account name,
# and password to send https requests
SYSTEM_URL = "https://172.20.57.139"
LOGIN_ACCOUNT = "admin"
LOGIN_PASSWORD = "admin123"

## Create a REDFISH object
REDFISH_OBJ = redfish.redfish_client(base_url=SYSTEM_URL, username=LOGIN_ACCOUNT,
                                    password=LOGIN_PASSWORD)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

# Do a GET on a given path
#content = REDFISH_OBJ.get("/redfish/v1/Systems/1")
#RESPONSE = REDFISH_OBJ.get("https://172.20.57.139/redfish/v1/")
content = REDFISH_OBJ.get("/redfish/v1/Systems/1/BaseNetworkAdapters/1")


#response = REDFISH_OBJ.put('body', 'hello')

# Print out the response
data = content.dict

#print(json.loads(data))
print(type(data))

#x = json.loads(data)
#print(x)
#with open("d_file.json", "w") as write_file:
 #   json.dump(data, write_file)
pprint.pprint((content.dict))
#print(data["Boot"]["BootSourceOverrideMode"])

#print(data["PhysicalPorts"][0]["MacAddress"])
'''
try:
    if (data["PhysicalPorts"][0]["LinkStatus"] == "LinkUp"):
        print(data["PhysicalPorts"][0]["MacAddress"])
    elif (data["PhysicalPorts"][1]["LinkStatus"] == "LinkUp"):
        print(data["PhysicalPorts"][1]["MacAddress"])
    elif (data["PhysicalPorts"][2]["LinkStatus"] == "LinkUp"):
        print(data["PhysicalPorts"][2]["MacAddress"])
    elif (data["PhysicalPorts"][3]["LinkStatus"] == "LinkUp"):
        print(data["PhysicalPorts"][3]["MacAddress"])
    else:
        print("ok")
except:
    print("k")
'''
# Logout of the current session
REDFISH_OBJ.logout()

List = dir(hell)
print(List)
