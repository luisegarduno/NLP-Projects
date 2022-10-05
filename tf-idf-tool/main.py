import sys
import time
import os.path
import subprocess
import numpy as np
import pandas as pd

# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

title = '''
          88888888888 .d888    8888888     888  .d888      888                     888
              888    d88P"       888       888 d88P"       888                     888
              888    888         888       888 888         888                     888
              888    888888      888   .d88888 888888      888888 .d88b.   .d88b.  888
              888    888         888  d88" 888 888         888   d88""88b d88""88b 888
              888    888  888888 888  888  888 888         888   888  888 888  888 888
              888    888         888  Y88b 888 888         Y88b. Y88..88P Y88..88P 888
              888    888       8888888 "Y88888 888          "Y888 "Y88P"   "Y88P"  888

                             ~ Website : https://gardunos.tech
'''

# Clear screen + show title
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title + "\n")
    print("\t\t-----------------------------------------------------------------\n\n")

# Print current strings/sentences
def showDict(docs):
    clr()
    print("\n====================================================\n")
    print("Entered strings/sentences:")
    doc_num = 1
    for i in docs:
        print("- [d{}] ".format(doc_num) + i)
        doc_num += 1
    print("\n====================================================\n\n")

clr()

docs = []
sent = input("Please enter a sentence/string: ")
docs.append(sent)
showDict(docs)

init_res = "y"
while init_res.lower() != "n" and init_res.lower() == "y":
    init_res = input("\t--> Add another sentence? (y/n): ")

    if init_res.lower() == "y":
        showDict(docs)
        sent = input("Please enter a sentence/string: ")
        docs.append(sent)

    if init_res.lower() != "y" and init_res.lower() != "n":
        print("Invalid input, please try again")
        clr()

showDict(docs)
