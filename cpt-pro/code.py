import xlrd
#from lxml import etree as ET
import shlex
import subprocess
import xml.etree.ElementTree as ET
import sys
from mac_trying import get_macaddress
from mac_trying import get_server_type
class exceldata():

    '''
     global x
     server type(gen9 or gen10 should be specified)
     x = input("ENTER THE NUMBER OF DEPLOYMENTS YOU WANT\n")
     it shouldd loop here 
     the success or failures stats should be printed on to console
     def get(self,i):
         #global y
        n=[]
         #loc =input("enter excel file location")
        loc = ('/root/Documents/teste.xlsx')
        ls = xlrd.open_workbook(loc)
        sheet = ls.sheet_by_index(0)
        #for i in range(0,x):
        for j in range(0,4):
             m = sheet.cell_value(i,j)
             setattr(self,"a",m)
             n.append(m)
        return n
     '''
    global x
    global shee
    global loca
    global lsr
    global in_type
    global host_names
    global os_dict
    os_dict={}
    host_names=[]
    print("1.one_os_multiple_nodes")
    print("2.multiple_os_multiple_nodes")
    in_type=input("Select the type of deployment\n")
    
    #x=input("ENTER THE NUMBER OF DEPLOYMENTS YOU WANT\n")
    loca = ('/root/servers.xlsx')
    lsr = xlrd.open_workbook(loca)
         #global sheet
    shee = lsr.sheet_by_index(0)
    def readex(self):
         a=[]
         global b
        
         b=[]
         c=[]
    #x=int(input("enter number"))
         loc = ('/root/servers.xlsx')
         ls = xlrd.open_workbook(loc)
         #global sheet
         sheet = ls.sheet_by_index(0)
    #cn=sheet.ncols
         
         cn =[]
         cn = sheet.col_values(0)
         #print(cn)
         
         bt=[]
         for i in range(0,len(cn)):

             at=sheet.row_values(i)
             bt.append(at)
         #print(bt)
         

         y={}

         for i in range(0,len(cn)):
             xt=get_server_type(bt[i][0],bt[i][1],bt[i][2])
             if xt[-1]=='Plus':
                 y[cn[i]]='GEN10 Plus'
             else:
                 y[cn[i]]=xt[1]
            # print(y)

         #x=input("enter number\n")
         print("Select the servers for deployment one after other")
         ha=1
         ro=[]
         for i in cn: 
             print("{}.{}-[{}]".format(ha,i,y[i]))
             #ha=int(ha)
             ro.append(ha)
             ha=ha+1
        #print(ro)
         my_list = []
             
         for i in range(0, int(x)):

             a=int(input())
             if a in ro:

                my_list.append(a)
             else:
                print("select from the above listed values")
                sys.exit()
         #else:
             #print(my_list)
        
         for i in my_list:
             
             a=sheet.row_values(i-1)
             b.append(a)
         #print(b)
         return b
                   
    def man(self,g,s,e,ma,a,b):
         #print(k) 
         #global m
         #global macaddrs
         #v = input("enter file name for xml"+ str(k))
         '''data=get_macaddress(g,s,e)
         #print(data[1])
         num=0
         numlis_mac=['0']
         for i in range(0,len(data)):
             print(num,'.',data[i])
             #print(h1)
             num+=1
             numlis_mac.append(num)
         mac_inp=int(input())
         if mac_inp in numlis_mac:
             macaddrs=data[mac_inp]
             m = macaddrs
             global m
         '''
         #a=input("ENTER OS BUILD PLAN\n")
         #b=input("ENTER OS PATH PATH \n")
         bm=input("Enter the Boot mode \n")
         hn=input("Enter the Hostname to be assigned to the server\n")
         if "RH8" in a and re.search("_", hn):
            
             hn=hn.replace('_', '')
         if "SLES15" in a and re.search("_", hn):

             hn=hn.replace('_', '')
         if "ESXi" in a and re.search("-|_", hn):
             hn = hn.replace('-','').replace('_','')
            # print(hn)
            # print("esxxx")
         host_names.append(hn)
         os_dict[hn]=a
         root = ET.Element ('CONFIGS') 
         start = ET.SubElement (root, 'CONFIG') 
         iso = ET.SubElement (start, 'OS') 
         iso.text = a 
         iso_path = ET.SubElement (start, 'OS_PATH') 
         iso_path.text = b
         start2 = ET.SubElement (start, 'NODES') 
         start3 = ET.SubElement (start2, 'NODE')
         start4 = ET.SubElement(start3, 'ILO')
         ip = ET.SubElement(start4, 'ILO_IP')
         ip.text = g
         user = ET.SubElement(start4, 'ILO_USERNAME')
         user.text = s
         pwd = ET.SubElement(start4, 'ILO_PASSWORD')
         pwd.text = e
         host_name = ET.SubElement(start3, 'HOST_NAME')
         host_name.text = hn
         mac_address = ET.SubElement(start3, 'MACADDRESS')
         mac_address.text = ma
         sys_pwd = ET.SubElement(start3, 'SYSTEM_PASSWORD')
         sys_pwd.text = "Compaq@123"
         cust_script = ET.SubElement(start3, 'CUSTOM_SCRIPT')
         if a[0] == 'R' or a[0]=='S':
             cust_script.text="/root/custom.sh"
         elif a[0] == "W":
             cust_script.text="/root/custom.bat"
         sys_pwd = ET.SubElement(start3, 'TEAM')
         sys_pwd.text = "CSI-Other"
         sys_pwd = ET.SubElement(start3, 'BOOTMODE')
         sys_pwd.text = bm
         start5 = ET.SubElement(start3, 'SPP')
         install = ET.SubElement(start5, 'INSTALL')
         install.text = "no"
         sys_pwd = ET.SubElement(start5, 'ISO_PATH')
         sys_pwd.text ="http://172.20.57.150/deployment/SPP/SPP2020030.2020_0319.22.iso"
         iso_path = ET.SubElement(start5, 'FLASH_FIRMWARE')
         iso_path.text = "Yes"
         o = ET.tostring(root, encoding='utf8').decode('utf8')
         #print(o)
         filename = "%s.xml" % g
         f1 = open(filename, 'w')
         f1.write(o)
         #print("xml is stored in" ,filename,"file")
         #setattr(self,"b",f1)
         f_list.append(filename)
         return f_list,host_names,os_dict

list1=[]
list2=[]

global f_list
f_list=[]
ob=exceldata()
import re
#print(type(x))
#xe=re.compile('^(?=.*[0-9]$)(?=.*[a-zA-Z])')
#if xe.match(username):
 #   print("getitvmisr")
xe=re.compile('(([a-z]+)([0-9]+))')
pe=re.compile('(([0-9]+)([a-z]+))')
#print(type(x))
de=re.compile('[^a-zA-Z0-9]')
#if(pe.match(username)or xe.match(username))and (xe.match(username)or pe.match(username)):
 #                                                                      print("getitvmis")
while True:
    global x
    
    x=input(f"Enter the number of deployemnts,maximum deployments can be " + str(shee.nrows)+"\n")
    if x.isalpha():
    #print("YOU HAVE ONLY "+ str(shee.nrows)+ "SERVERS")
    #ob=exceldata()
    #sys.exit()
    #ob.readex()
        print("ACCEPTS ONLY INTEGERS")
        #sys.exit()

    elif x.isdigit() and int(x) > shee.nrows:
        print("YOU HAVE ONLY "+ str(shee.nrows) + " SERVERS")
        #sys.exit()
    elif (pe.match(x)or xe.match(x))and (xe.match(x)or pe.match(x)):

        print("ACCEPTS ONLY INTEGERS")
        #sys.exit()
    #ob=exceldata()
    #ob.readex()
    elif de.match(x):
        print("special characters not allowed")
        #sys.exit()
    elif int(x) <= shee.nrows and x.isdigit() and int(x)>0:

     #print("ACCEPTS ONLY INTEGERS")
     #sys.exit()
        ob=exceldata()
        ob.readex()
        break
    elif int(x)== 0:
        print("DEPLOYMENTS SHOULD BE ATLEAST ONE")
        #sys.exit()
    else:
        print("negative integers not accepted")
        #sys.exit()
'''if x.isdigit():

    #ob=exceldata()
    ob.readex()
else:
    print("ACCEPTS ONLY INTEGERS")
    sys.exit()'''
#print(x)
'''
if x.isdigit():
    for i in range(0,int(x)):
         obj=exceldata()
         list1.append(obj.get(i))
else:
    print("enter numerical values")
    sys.exit()
    obj1=exceldata()
    x=input()
    if x.isdigit():
        for i in range(0,int(x)):
             obj=exceldata()

         #list1.append(obj.get(i))

             list1.append(obj.get(i))

print(list1)'''
#data=get_macaddress(b[0][0], b[0][1],b[0][2])
#print(data)
#print(list1[0][0])
#for m in range(0,int(y))
#global macaddrs
if in_type == "1":
    ai=input("Enter os build plan\n")
    bi=input("Enter os Path\n")

    for k in range(0,int(x)):
        #print(k)

     #ob=exceldata()

        data=get_macaddress(b[k][0], b[k][1],b[k][2])
         #print(data[1])
        num=1
        numlis_mac=[]
        print("Please select the Mac Address to deploy OS")
        for i in range(0,len(data)):

            #print(num,'.',data[i])
             #print(h1)
            #num+=1
            print("{}.{}".format(num,data[i]))
            numlis_mac.append(num)
            num+=1
        #print("Please select the Mac Address to deploy OS")
        mac_inp=int(input())
        if mac_inp in numlis_mac:
        #print(mac_inp+1) 
        
            macc=data[mac_inp-1]
        #macaddrs.append(data[mac_inp])
        #print(macaddrs)
   #     m = macaddrs
             #global m

        ob.man(b[k][0], b[k][1],b[k][2],macc,ai,bi)
if in_type=="2":

    for k in range(0,int(x)):

        ai=input("Enter os build plan\n")
        bi=input("Enter os path\n")
        data=get_macaddress(b[k][0], b[k][1],b[k][2])
         #print(data[1])
        num=1
        numlis_mac=[]
        print("Please select the Mac Address to deploy OS")
        for i in range(0,len(data)):

            #print(num,'.',data[i-1])
             #print(h1)
            print("{}.{}".format(num,data[i]))
            
            numlis_mac.append(num)
            num+=1
        #print("Please select the Mac Address to deploy OS")
        mac_inp=int(input())
        if mac_inp in numlis_mac:
            #global maccc
            #print("hello")
        #print(mac_inp+1)
            mma=data[mac_inp-1]
        #macaddrs.append(data[mac_inp])
        #print(macaddrs)
   #     m = macaddrs
             #global m
       # print(maccc)
        ob.man(b[k][0], b[k][1],b[k][2],mma,ai,bi)

#print(f_list)
from subprocess import Popen, PIPE
import os
xp=os.popen('pwd').read().split('\n')
#f_list=["file1","file2"]
#print(x[0])
y=xp[0]
#print(type(y))
#print(y)
#p1=[y + dire for dire in f_list]

p = ["/"  + dire for dire in f_list]
p1=[y+dire for dire in p]
p1=["-f " + dire for dire in p1]

#p = ['-f /root/' + dire for dire in f_list]
#p = ['-f/'+ dire for dire in f_list]
def mmk(n):
     return n  +  " " '-cy'
res=map(mmk,p1)
files_list=list(res)
#print(files_list)
from datetime import datetime
d1=datetime.now()
d2=d1.strftime("%d-%H:%M")
of='output_'
of1='.txt'
of2=of+d2+of1
q=open(of2,"w")
e=open("errorout.txt","w")
print("DEPLOYMENT STARTED")
from subprocess import Popen, PIPE
import subprocess
import os
cmds_list = [['cpt', file_name] for file_name in files_list]
procs = [Popen(cmd,bufsize=0,stdout=q, stderr=e) for cmd in cmds_list]
for proc in procs:
    #proc.communicate()
    stdout, stderr = proc.communicate()
    #stdout = procs.stdout.read()
    #print(stdout)
    proc.wait()
os.system("rm errorout.txt")
os.popen("cd /opt/l2deploy/logs/")
#x=['rh8','rh78-normal','mmk']
for i in host_names:

    dat_file="/opt/l2deploy/logs/OverallStatusReport_"+i+".dat"
    xy=os.path.isfile(str(dat_file))
    if xy:
       # print("ok!!")

        p=subprocess.check_output(f'cat {dat_file}' , shell =True).decode("utf-8").strip()
        if 'SUCCESS' in p:
            print("Deployment on",i, "host with",os_dict[i],"os is success!!")
        else:
            print("Deployment on",i ,"host with",os_dict[i], "os got failed!!")
    else:
        print("Deployment on" ,i,"host with",os_dict[i], "os is failed")
pr=y+'/'+of2
print("Please check the",pr,"file for the console output.")
