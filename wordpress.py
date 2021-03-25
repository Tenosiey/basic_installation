import os
import basic
import webserver

basic_tools_done = input("Wurde das basic.py Script bereits ausgeführt?\ny/n\n")
webserver_done = input("Wurde das webserver.py Script bereits ausgeführt?\ny/n\n")

def wordpress_install():
    print("Installiere Wordpress!")

    os.system("sudo apt install php -y")
    os.system("sudo apt install php-mysql -y")
    os.system("sudo apt install php-xml -y")
    os.system("sudo apt install mariadb-server -y")

if __name__ == "__main__":
    if basic_tools_done == "n" and webserver_done == "n":
        basic.basic_tools_install()
        webserver.webserver_install()
        wordpress_install()

    
    elif basic_tools_done == "y" and webserver_done == "n":
        webserver.webserver_install()
        wordpress_install()

    elif basic_tools_done == "y" and webserver_done == "y":
        wordpress_install()

    else:
        print("Was willst du denn von mir?!\nLern mal tippen du Spast...")