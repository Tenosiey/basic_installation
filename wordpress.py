import os
import basic
import webserver

def wordpress_install():
    print("Installiere Wordpress!")

    os.system("sudo apt install php -y")
    os.system("sudo apt install php-mysql -y")
    os.system("sudo apt install php-xml -y")
    os.system("sudo apt install mariadb-server -y")

if __name__ == "__main__":
    basic_tools_done = input("Wurde das basic.py Script bereits ausgeführt?\ny/n\n")
    webserver_done = input("Wurde das webserver.py Script bereits ausgeführt?\ny/n\n")

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
        print("Junge? The fuq hast du gemacht?")