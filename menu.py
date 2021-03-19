import os
import getpass
import pyfiglet
import socket
import subprocess as sp

#design
os.system("tput setaf 4")
title = pyfiglet.figlet_format("GROUP-7.1", font = "epic" )
print(title)
os.system("tput setaf 2")
msg = pyfiglet.figlet_format("Welcome You", font = "digital" )
print(msg)

os.system("tput setaf 3")
print("\t\t\t Menu Bar\n\n\n")
os.system("tput setaf 7")
print("\t\t-------------------")


passwd = getpass.getpass(" Enter Your Password : ")

if passwd != "group7":
	print("password is Incorrect...")
	exit()


where = input(" Where you want to run this menu ? (local/remote) : ")
print(where)

def print_msg_box(msg, indent=1, width=None, title=None):
    os.system("tput setaf 2")
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

msg = "press 0 : linux\n" \
      "Press 1 : hadoop\n" \
      "Press 2 : docker\n" \
      "Press 3 : web Server\n" \
      "Press 4 : aws\n"
print_msg_box(msg=msg, indent=2, title='All Services') 

if where == "local":
	os.system("tput setaf 1")
	ch = input("Enter choice (service): ")
	print(ch)

	if int(ch) == 0:
		while True:
			os.system("clear")
			os.system("tput setaf 2")
			msg ="press 0 : To exit\n" \
			     "Press 1 : run date\n" \
			     "Press 2 : run cal\n" \
			     "Press 3 : run ifconfig\n" \
			     "Press 4 : check httpd status\n" \
			     "Press 5 : run httpd \n" \
			     "press 6 : to clear cache\n" \
		       	     "press 7 : To transfer file to other linux system" 
			print_msg_box(msg=msg, indent=2, title='Linux Command:') 
			os.system("tput setaf 1")
			ch=input("choose your option : ")
			os.system("tput setaf 3")
			print(ch)
			if int(ch) == 0:
				exit()
			elif int(ch) == 1:
				os.system("date")


			elif int(ch) == 2:
				os.system("cal")

			elif int(ch) == 3:
				os.system("ifconfig")

			elif int(ch) == 4:
				os.system("systemctl status httpd")
			elif int(ch) == 5:
				os.system("systemctl start httpd")
			elif int(ch) == 6:
				os.system("echo 3 > /proc/sys/vm/drop_caches")
			elif int(ch) == 7:
				ip = input("Enter IP of target system : ")
				user = input("Enter username : ")
				src = input("Enter your source file path : ")
				dest = input("Enter destination folder path where you want to copy : ")
				output =getpass.getstatusoutput("scp {} {}@{}:{}".format(src, user,ip,dest))

			else:
				print("Incorrect Number")
			input("\ncontinue...")

	if int(ch) == 1:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			msg = "Press 1 : Install jdk and Hadoop\n" \
			      "Press 2 : Configure  dataNode\n" \
			      "Press 3 : configure  nameNode\n" \
			      "Press 4 : configure client\n" \
			      "Press 5 : cluster report\n" \
			      "press 6 : check safeMode(nameNode)\n" \
			      "press 7 : disable safemode in namenode " \
			      "press 8 : upload a file into cluster\n" \
			      "press 9 : exit..\n"
			print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
			os.system("tput setaf 1") 
			ch=input("choose your option : ")
			print(ch)
					#Hadoop-installation


			if int(ch) == 1:
				os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")


					#namenode

			elif int(ch) == 2:
				os.system("rm -rf /nn")
				os.system("mkdir /nn")
				f=open("/etc/hadoop/hdfs-site.xml","w")
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
					
				<configuration>
				<property>
				<name>dfs.name.dir</name>
				<value>/nn</value>
				</property>
				</configuration>""")
				f.write(x)
				f.close
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://0.0.0.0:9001</value>
				</property>
				</configuration> 
				""")
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close
				os.system('hadoop namenode -format ')
				os.system('hadoop-daemon.sh start namenode')

					#dataNode

			elif int(ch) == 3:
				os.system("rm -rf /dn")
				os.system("mkdir /dn")
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>dfs.data.dir</name>
				<value>/dn</value>
				</property>
				</configuration>""")
				f=open("/etc/hadoop/hdfs-site.xml","w")
				f.write(x)
				f.close
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.43.102:9001</value>
				</property>
				</configuration> 
				""")
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close
				os.system('hadoop-daemon.sh start datanode')


					#clint

			elif int(ch) == 4:
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.43.102:9001</value>
				</property>
				</configuration> """)
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close

					#other basic commands

			elif int(ch) == 5:
				os.system("hadoop dfsadmin -report | less")

			elif int(ch) == 6:
				os.system("hadoop dfsadmin -safemode get")
			elif int(ch) == 7:
				os.system("hadoop dfsadmin -safemode leave")
			elif int(ch) == 8:
				name = input('Enter File Name :')
				os.system(f"hadoop fs -put {name}/")
			elif int(ch) == 9:
				exit()

			else:
				print("Incorrect Number")
			input("\ncontinue...")

					#docker


	if int(ch) == 2:
		while True:
			os.system("clear")
			os.system("tput setaf 2")
			msg = "press 0 : Verify docker is installed or not\n" \
			      "Press 1 : Install docker\n" \
			      "Press 2 : start Docker\n" \
			      "Press 3 : List all docker images\n" \
			      "Press 4 : pull docker image\n" \
			      "Press 5 : Launch a container with name\n" \
			      "Press 6 : List running docker containers\n" \
			      "press 7 : start a container\n" \
			      "press 8 : to go inside any runing container\n" \
			      "press 9 : stop a container " \
			      "Press 10 : Delete a container\n" \
			      "Press 11: Delete an image\n" \
			      "Press 12: Delete all container\n" \
			      "Press 13: exit..\n" 
			print_msg_box(msg=msg, indent=2, title='Docker Command:')
			os.system("tput setaf 1") 
			ch=input("choose your option : ")
			print(ch)

			if int(ch) == 0:
				os.system("rpm -q docker-ce")

					#docker installation

			elif int(ch) == 1:
				os.system('yum install docker-ce')
			elif int(ch) == 2:
				os.system('systemctl start docker')
			elif int(ch) == 3:
				os.system('docker images -a')
			elif int(ch) == 4:
				OS = input("Enter docker image name :")
				os.system(f'docker pull -i {OS}')
			elif int(ch) == 5:
				NAME = input("Enter imagename and version (OSname:00.00):")
				myName = input("Give a new OS name :")
				os.system(f'docker run -it --name {myName} {NAME}')
			elif int(ch) == 6:
				os.system('docker ps')
			elif int(ch) == 7:
				NAME = input("Enter The OS name :")
				os.system('docker start {NAME}')
			elif int(ch) == 8:
				NAME = input("Enter The OS name :")
				os.system('docker attach {NAME}')
			elif int(ch) == 9:
				NAME = input("Enter The OS name :")
				os.system('docker stop {NAME}')
			elif int(ch) == 10:
				NAME = input("Enter The OS name :")
				os.system('docker rm -f {NAME}')
			elif int(ch) == 11:
				NAME = input("Enter The image name :")
				os.system('docker rmi -f {NAME}')
			elif int(ch) == 12:
				os.system('docker rm `docker ps -a -q` ')
			elif int(ch) == 13:
				exit()

			else:
				print("Incorrect Number")
			input("\ncontinue...")

	if int(ch) == 3:
		while True:
			os.system("clear")
			os.system("tput setaf 2")
			msg = "press 0 : check apache web server is installed or not\n" \
			      "Press 1 : start httpd service\n" \
			      "Press 2 : disable firewall and set enforcing\n" \
			      "Press 3 : restart httpd service\n" \
			      "Press 4 : cconfigure total webserver\n" \
			      "press 5 : exit.. "
			print_msg_box(msg=msg, indent=2, title='HTTPD Commands:')
			os.system("tput setaf 1") 
			ch=input("choose your option : ")
			print(ch)
			if int(ch) == 0:
				os.system("rpm -q httpd")

			elif int(ch) == 1:
				os.system('yum install httpd')
				os.system('systemctl start httpd')
			elif int(ch) == 2:
				os.system('systemctl stop firewalld')
				os.system('setenforce 0')
			elif int(ch) == 3:
				os.system('systemctl restart httpd')
			elif int(ch) == 4:
				Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
				IP=Soc.getsockname()[0]
				T=input("\tEnter your message to preview on web :")
				
				os.system('yum install httpd')
				os.system('cd /var/www/html/')
				os.system('touch web.html')
				os.system(f'echo "{T}" > /var/www/html/web.html')
				os.system('systemctl start httpd')
				os.system('systemctl stop firewalld')
				os.system('setenforce 0')
				os.system(f'firefox http://"{IP}"/web.html')
			elif int(ch) == 5:
				exit()

			else:
				print("Incorrect Number")
			input("\ncontinue...")



elif where == "remote":
	ip = input("Enter remote IP: ")
	print(ip)
	ch = input("Enter choice (service): ")
	print(ch)

	if int(ch) == 0:
		while True:
			os.system("clear")
			os.system("tput setaf 2")
			msg ="press 0 : To exit\n" \
			     "Press 1 : run date\n" \
			     "Press 2 : run cal\n" \
			     "Press 3 : run ifconfig\n" \
			     "Press 4 : check httpd status\n" \
			     "Press 5 : run httpd \n" \
			     "press 6 : to clear cache\n" \
		       	     "press 7 : to change any command name"
			print_msg_box(msg=msg, indent=2, title='Linux Command:') 
			os.system("tput setaf 1")
			ch=input("choose your option : ")
			print(ch)
			if int(ch) == 0:
				os.system("ssh {} ifconfig".format(ip))
			elif int(ch) == 1:
				os.system("ssh {} date".format(ip))
			elif int(ch) == 2:
				os.system("ssh {} cal".format(ip))
			elif int(ch) == 3:
				os.system("ssh {} ls".format(ip))
			elif int(ch) == 4:
				os.system("ssh {} systemctl ststus httpd".format(ip))
			elif int(ch) == 5:
				os.system("ssh {} systemctl start httpd".format(ip))
			elif int(ch) == 6:
				os.system("ssh {} echo 3 > /proc/sys/vm/drop_caches".format(ip))
			else:
				print("Incorrect Number")
			input("\ncontinue...")

					#hadoop

	if int(ch) == 1:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			msg = "press 0 : To exit\n" \
			      "Press 1 : Install jdk and Hadoop\n" \
			      "Press 2 : Configure  dataNode\n" \
			      "Press 3 : configure  nameNode\n" \
			      "Press 4 : configure client\n" \
			      "Press 5 : check the connected datanodes\n" \
			      "press 6 : check safeMode in nameNode\n" \
			      "press 7 : disable safemode in namenode "
			print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
			os.system("tput setaf 1")
			ch=input("choose your option : ")
			print(ch)
					#Hadoop-installation


			if int(ch) == 1:
				os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip))
				os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip))

					#namenode

			elif int(ch) == 2:
				os.system("ssh {} rm -rf /nn".format(ip))
				os.system("ssh {} mkdir /nn".format(ip))
				os.system("ssh {} ".format(ip))
				f=open("/etc/hadoop/hdfs-site.xml","w")
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
					
				<configuration>
				<property>
				<name>dfs.name.dir</name>
				<value>/nn</value>
				</property>
				</configuration>""")
				f.write(x)
				f.close
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://0.0.0.0:9001</value>
				</property>
				</configuration> 
				""")
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close
				os.system("ssh {} hadoop namenode -format".format(ip))
				os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))

					#dataNode

			elif int(ch) == 3:
				os.system("ssh {} rm -rf /nn".format(ip))
				os.system("ssh {} mkdir /nn".format(ip))
				os.system("ssh {} ".format(ip))
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>dfs.data.dir</name>
				<value>/dn</value>
				</property>
				</configuration>""")
				f=open("/etc/hadoop/hdfs-site.xml","w")
				f.write(x)
				f.close
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.43.102:9001</value>
				</property>
				</configuration> 
				""")
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close
				os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))


					#clint

			elif int(ch) == 4:
				os.system("ssh {} ".format(ip))
				x=("""<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
				<!-- Put site-specific property overrides in this file. -->
			
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.43.102:9001</value>
				</property>
				</configuration> """)
				f=open("/etc/hadoop/core-site.xml","w")
				f.write(x)
				f.close

					#other basic commands

			elif int(ch) == 5:
				os.system("ssh {} hadoop dfsadmin -report | less".format(ip))
			elif int(ch) == 6:
				os.system("ssh {} hadoop dfsadmin -safemode get".format(ip))
			elif int(ch) == 7:
				os.system("ssh {} hadoop dfsadmin -safemode leave".format(ip))

			else:
				print("Incorrect Number")
			input("\ncontinue...")

					#docker


	if int(ch) == 2:
		while True:
			os.system("clear")
			os.system("tput setaf 1")
			msg = "press 0 : To verify docker is installed or not\n" \
			      "Press 1 : Install docker-ce and start the service\n" \
			      "Press 2 : check all docker images\n" \
			      "Press 3 : pull a docker image and run\n" \
			      "Press 4 : check running docker containers\n" \
			      "Press 5 : check the connected datanodes\n" \
			      "press 6 : check safeMode in nameNode\n" \
			      "press 7 : disable safemode in namenode "
			print_msg_box(msg=msg, indent=2, title='Docker Command:') 
			os.system("tput setaf 1")
			ch=input("choose your option : ")
			print(ch)
					#Docker-installation


			if int(ch) == 0:
				os.system("ssh {} rpm -q docker-ce".format(ip))

			#docker installation

			elif int(ch) == 1:
				os.system("ssh {} yum install docker-ce".format(ip))
				os.system("ssh {} systemctl start docker".format(ip))
			elif int(ch) == 2:
				os.system("ssh {} docker images -a".format(ip))
			elif int(ch) == 3:
				os.system("ssh {} ".format(ip))
				OS = input("Enter docker image name :")
				os.system(f'docker load -i {OS}')
				NAME = input("Enter imagename and version :")
				os.system(f'docker run -it {NAME}')
			elif int(ch) == 4:
				os.system("ssh {} docker ps".format(ip))

			else:
				print("Incorrect Number")
			input("\ncontinue...")



else:
	print("login is not supported....")

input("\nplease Enter to Continue....")





















