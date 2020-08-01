import sys
import json
import redfish
#import hell
import pprint
# When running on the server locally use the following commented values
# HOST = "blobstore://."
# LOGIN_ACCOUNT = "None"
# LOGIN_PASSWORD = "None"

# When running remotely connect using the iLO address, iLO account name,
# and password to send https requests
def get_macaddress(a,b,c):

    SYSTEM_URL = "https://"+a
    LOGIN_ACCOUNT = b
    LOGIN_PASSWORD = c

## Create a REDFISH object
    REDFISH_OBJ = redfish.redfish_client(base_url=SYSTEM_URL, username=LOGIN_ACCOUNT,
                                    password=LOGIN_PASSWORD)

# Login into the server and create a session
    REDFISH_OBJ.login(auth="session")

# Do a GET on a given path
    content_ilotype = REDFISH_OBJ.get("/redfish/v1/Systems/1")
    x_ilotype=content_ilotype.dict
    y_ilotype=x_ilotype["Model"].split(" ")[-1]

#RESPONSE = REDFISH_OBJ.get("https://172.20.57.139/redfish/v1/")
    content_gen10 = REDFISH_OBJ.get("/redfish/v1/Systems/1/BaseNetworkAdapters")
    content_gen9= REDFISH_OBJ.get("/redfish/v1/Systems/1/NetworkAdapters")

#response = REDFISH_OBJ.put('body', 'hello')
    data_g9=content_gen9.dict
#print(data_g10)
#x_g9=data_g9['Members@odata.count']
#print(x_g9)
#x_g9=x_g9+1
#print(x_g10)
    #macaddrs=[]
# Print out the response
    data_g10 = content_gen10.dict
#print(data_g10)
#x_g10=data_g10['Members@odata.count']
#print(x_g10)
#x_g10=x_g10+1
#print(x_g10)

#print(json.loads(data))
#print(type(data))
    lst_mac=[]
#x = json.loads(data)
#print(x)
#with open("d_file.json", "w") as write_file:
 #   json.dump(data, write_file)
#pprint.pprint((content.dict))
#print(data["Boot"]["BootSourceOverrideMode"])
    if y_ilotype== "Gen10":

        contentg10 = REDFISH_OBJ.get("/redfish/v1/Systems/1/BaseNetworkAdapters/1")
        c2=contentg10.dict
        x_g10=data_g10['Members@odata.count']
#print(x_g10)
        x_g10=x_g10+1

        for i in range(1,x_g10):
            content1_g10 = REDFISH_OBJ.get("/redfish/v1/Systems/1/BaseNetworkAdapters/%d"%i)
            c2_g10=content1_g10.dict
   # print(c2)
            for j in range(0,len(c2_g10['PhysicalPorts'])):

                #print(c2_g10["PhysicalPorts"][j]["MacAddress"])
                c3=c2_g10["PhysicalPorts"][j]["MacAddress"]
                lst_mac.append(c3)
    elif y_ilotype=="Gen9":
        contentg9 = REDFISH_OBJ.get("/redfish/v1/Systems/1/NetworkAdapters/1")
        c2=contentg9.dictx_g9=data_g9['Members@odata.count']
#print(x_g9)
        x_g9=data_g9['Members@odata.count']
        x_g9=x_g9+1

        for i in range(1,x_g9):
            content1_g9 = REDFISH_OBJ.get("/redfish/v1/Systems/1/NetworkAdapters/%d"%i)
            c2_g9=content1_g9.dict
   # print(c2)
            for j in range(0,len(c2_g9['PhysicalPorts'])):

                #print(c2_g9["PhysicalPorts"][j]["MacAddress"])
                c1=c2_g9["PhysicalPorts"][j]["MacAddress"]
                lst_mac.append(c1)
# Logout of the current session
    return lst_mac
    REDFISH_OBJ.logout()
#get_macaddress("172.20.57.187","admin","admin123")
#print(d)

