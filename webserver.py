import os
import basic

basic_tools_done = input("Wurde das basic.py Script bereits ausgeführt?\ny/n\n")

def webserver_install():
    print("Installiere den Webserver!")

    os.system("sudo apt install apache2 -y")

if basic_tools_done == "n":
    basic.basic_tools_install()
    webserver_install()

elif basic_tools_done == "y":
    print("Dann nicht...")
    webserver_install()

else:
    print("Was willst du denn von mir?!\nLern mal tippen du Spast...")