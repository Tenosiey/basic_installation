import os
import basic

basic_done = input("Wurde das basic.py Script bereits ausgeführt?")

if basic_done == "n":
    basic.basic_tools()
elif basic_done == "y":
    print("Dann nicht...")
else:
    print("Was willst du denn von mir?!")