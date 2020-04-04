import os
import getpass

os.system("tput setaf 1")
print("\t\t\t WELCOMW TO MY TUI")
os.system("tput setaf 7")
print("\t\t\t -----------------------")

passwd=getpass.getpass("enter your passward")
apass="lw"

if passwd!=apass:
	print("auth incorrect")
	exit()



print("where do you ant to perform your job local/remote")
location=input()

if location =="remote":
        remoteIp=input("enter your IP : ")



while True:
        print("""
        PRESS 1: TO SEE DATE
        PRESS 2: TO CHECK CAL
        PRESS 3: CONG WEB SERVER
        PRESS 4: TO CREATE USER
        PRESS 5: TO CHECK PACKAGE AVAILABLE
        PRESS 6: TO CHECK SERVER CONFIGRATION
        PRESS 7 TO EXIT
        """)
        print("enter your choice :",end="")
        ch=input()
        print(ch)
        if location =="local":
            if int(ch) ==1:
                os.system("date")
            elif int(ch) ==2:
                os.system("cal")
            elif int(ch)==3:
                os.system("yum install httpd")
            elif int(ch)==4:
                print("add user name : ",end =' ')
                create_user=input()
                os.system("useradd {}".format(create_user))
            elif int(ch) == 5:
                 print("write a package name lets see if its available: ", end="")
                 pack_name = input()
                 os.system("dnf install {}".format(pack_name))
            elif int(ch) == 6:
                os.system("systemctl restart httpd")
            elif int(ch)==7:
                exit()
            else:
                print("invalid")
        input("enter to continue")
        os.system("clear")
        if location == "remote":
            if int(ch) == 1:
                os.system("ssh {0} date".format(remoteIp))
            elif int(ch) == 2:
                os.system("ssh {0} cal".format(remoteIp))
            elif int(ch) == 3:
                os.system("ssh {0} yum install httpd".format(remoteIp))
            elif int(ch) == 4:
                print("can you give me name for user: ",end="")
                create_user = input()
                os.system("ssh {0} useradd {1}".format(remoteIp,create_user))
            elif int(ch) == 5:
                print("write a package name lets see if its available: ", end="")
                pack_name = input()
                os.system("ssh {0} dnf install {1}".format(remoteIp,pack_name))
            elif int(ch) == 6:
                os.system("ssh {0}systemctl restart httpd".format(remoteIp))
            elif int(ch) == 7:
                exit()
        else:
            print("option not found")

