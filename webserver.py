import os
from pynput.keyboard import Key, Controller
print("###################################################\n")
print("Starte Webserver installation!\n")
print("###################################################")
os.system("sudo -s")
os.system("apt install apache2 php php-mysql php-xml mariadb-server -y")
os.system("mysql_secure_installation")
keyboard = Controller()
keyboard.press(Key.enter)
os.system("raspberry")
keyboard.press(Key.enter)
os.system("raspberry")
keyboard.press(Key.enter)
keyboard.press(Key.enter)
keyboard.press(Key.enter)
keyboard.press(Key.enter)
keyboard.press(Key.enter)
keyboard.press(Key.enter)
os.system("nano /etc/mysql/mariadb.conf.d/50-server.cnf")

#Hier die Raute bei port entfernen und eine Raute bei bind-adress setzen#

os.system("mysql -u root")
os.system("CREATE USER admin@localhost IDENTIFIED BY 'raspberry';")
os.system("GRANT ALL PRIVILEGES ON *.* TO admin@localhost WITH GRANT OPTION;")
os.system("CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;")
os.system("exit")

#Bearbeiten sollte beendet sein.#

os.system("cd /var/www/html/")
os.system("rm index.html")
os.system("wget http://wordpress.org/latest.zip")
os.system("unzip latest.zip")
os.system("rm latest.zip")
os.system("mv wordpress/* .")
os.system("rm -d wordpress/")
os.system("chmod -R 777 /var/www/html")

print("###################################################\n")
print("Fertig, System wird neugestartet!\n")
print("###################################################\n")
time.sleep(5)
os.system("reboot")

if os.geteuid() == 0:
	print("Du bist root, du Spast!")
else:
	print("Du bist ein low-Bob, du Spast!")

with open("test.txt", "a") as f:
     f.write("nippel\n")

with open("test.config", "a") as f:
     f.write("Anus\n")

print("done!")
