import os


if __name__ == "__main__":
    # Update/Upgrade the System

    print("###################################################\n")
    print("Starte das Basic Installation Script!\n")
    print("###################################################")

    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    os.system("sudo apt install neofetch -y")

    print("###################################################")

    # Final steps

    os.system("neofetch")

    print("###################################################")