import os

# Install and Upgrade the System

print("###################################################\n")
print("Starte das Main Installation Script!\n")
print("###################################################")

os.system("sudo apt update")
os.system("sudo apt upgrade -y")
os.system("sudo apt install neofetch -y")
os.system("sudo apt install cmatrix -y")

print("###################################################\n")

# Check the User ID

if os.geteuid() == 0:
	print("Du bist root, du Spast!")
else:
	print("Du bist ein low-Bob, du Spast!")

# Create/append a txt/config File

with open("test.txt", "a") as f:
	f.write("nippel\n")
	f.close()

with open("test.config", "a") as f:
	f.write("Anus\n")
	f.close()

# Check if File Contains a string and replace it

reading_file = open("test.txt", "r")
new_file_content = ""

for line in reading_file:
	stripped_line = line.strip()
	new_line = stripped_line.replace("fotze", "stuhl")
	new_file_content += new_line +"\n"
reading_file.close()

writing_file = open("test.txt", "w")
writing_file.write(new_file_content)
writing_file.close()

# End of script

print("done!")

os.system("neofetch")
os.system("cmatrix")
