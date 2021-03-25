import os
import basic

basic_done = input("Wurde das basic.py Script bereits ausgeführt?")

if basic_done == "y":
    basic.basic_tools()
elif basic_done == "n":
    print("Dann nicht...")