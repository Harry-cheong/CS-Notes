import sys 
import os 
import logging
import json 
import string 
import random 
from datetime import datetime

# File Path 
CONFIG_PATH = r"config.txt"
BIN_PATH = r"bin"
FILELOGS_PATH = r"bin\fileLogs.txt"

# Config 
with open(CONFIG_PATH, "r") as configFile:
    
    myText = configFile.readlines()
    IN_PATH = myText[0][myText[0].find("=") + 2 : ].strip()
    if not os.path.exists(IN_PATH):
        IN_PATH = ''
    
    global chapterTemplate, chapterTemplateLen
    chapterTemplate = myText[1][myText[1].find("=") + 2:].strip()
    chapterTemplateLen = len(chapterTemplate)
    if chapterTemplateLen % 2 != 0:
        chapterTemplate += " "
        chapterTemplateLen += 1

    # print(IN_PATH, chapterTemplate)

# Info 
info = """
[Commands]
    1. cd [~newPath~] : changes targetted file 

    2. format [~mode~] [~line~]: formats the targetted file

    3. var : returns a list of all the versions in the bin 

    4. revert [~var~] : reverts the targetted file to the specified var
    * if unspecified, reverts to previous version 
    WARNING: Revert cannot be undone 

    5. bin [~command~]
        a. -list : lists all items in the bin
        b. -clear : removes all items in the bin 

    6. logs : views all activity of the Formatter 

    7. gen : generate content page for text file

    8. publish [~author~]: stores text file inside the published folder 

    9. exit() : ends session
"""

# Functions  
def checkForArgs(array, length):
    if not len(array) == length:
        print(f"Missing args for \"{array[0]}\"")
        return False
    return True

def parsePath(pathName):
    return pathName.replace("\'", "")

def cd(newPath):
    global IN_PATH
    IN_PATH = parsePath(newPath.strip())
    if not os.path.exists(IN_PATH):
        IN_PATH = ''
        print(f"{newPath} not Found.")

def logFile(fileContents):
    var = random.choice(string.ascii_letters) + str(random.randint(10, 20)) + random.choice(string.ascii_letters)

    time = datetime.now().strftime("[%y-%m-%d] %H%M%S")

    filePath = os.path.join(BIN_PATH, f"{time}.txt")
    print(f"<{filePath}> binned")
    
    with open(filePath, "w") as binFile:
        binFile.write("".join(fileContents))
    
    # Logging 
    # with open(FILELOGS_PATH, "r") as jsonFile:

    #     jsonObj = json.load(jsonFile)

def changeLineInFile(line, newText):
    with open(IN_PATH, 'r') as inFile:
        fileContents = inFile.readlines()
    # print(fileContents)

    logFile(fileContents)
    fileContents[line - 1] = newText + "\n"

    with open(IN_PATH, 'w') as inFile:
        # print("\n".join(fileContents))
        inFile.write("".join(fileContents))

def format():
    
    # Finding mode 
    print("=======================================")
    # print("[ Mode 1: Chapter oR Mode 2: Chapter Topic ]")
    sys.stdout.write("[ Mode 1: Chapter oR Mode 2: Chapter Topic ] : Mode ")
    mode = int(input())
    # print(mode)
    if (mode > 2) or (mode < 0):
        print("Invalid Mode")
        return

    # Finding line 
    sys.stdout.write("Line: ")
    line = int(input())

    if mode == 1:

        print("== Chapter Mode ==")
        sys.stdout.write("Chapter Name: ")
        chapterName = input()
        chapterName = " " + chapterName + " "

        global chapterTemplateLen, chapterTemplate
        nameLen = len(chapterName)
        customTemplate = chapterTemplate[:chapterTemplateLen - nameLen]
        halfLen = int(len(customTemplate) / 2)

        if nameLen % 2 == 0: 
            chapterString = customTemplate[:halfLen] + chapterName + customTemplate[halfLen:]
        
        else:
            chapterString = customTemplate[:halfLen] + chapterName + customTemplate[halfLen + 1:]
        chapterString = chapterTemplate + '\n' + chapterString

        changeLineInFile(line, chapterString)
    
    elif mode == 2:

        print("== Topic Mode ==")
        # Finding out Difficulty Level 
        sys.stdout.write("Difficulty Level: ")
        difficulty = int(input())
        difficultyString = "🌟" * difficulty

        # Finding out topicName 
        sys.stdout.write("Topic Name: ")
        topicName = input()

        topicString = f"| {topicName} |"

        changeLineInFile(line, topicString)

def listdir(dir):
    print("=======================================")
    for item in os.listdir(dir):
        print(item)

def executeCmds(commands): 
    # 1. cd
    if commands[0] == "cd":
        if not checkForArgs(commands, 2):
            return
        cd(commands[1])
        # print(IN_PATH)
    
    # 2. help
    if commands[0] == "help":
        sys.stdout.write(info)
    
    # 3. var
    if commands[0] == "var":
        pass

    # 4. format 
    if commands[0] == "f":
        format()
    
    # 5. bin 
    if commands[0] == "bin":
        listdir(BIN_PATH)

    
while True:
    sys.stdout.write(f"<{IN_PATH}> ")
    command = input().strip()

    # Parsing commands 
    commands = command.split("[")
    for (i, cmd) in enumerate(commands): commands[i] = cmd.strip().replace("]","")
    # print(commands)
    
    executeCmds(commands)
    
    # 6. exit()
    if commands[0] == "exit()":
        break

    print()

# Config File 
with open(CONFIG_PATH, "w") as configFile: 
    configContents = [
        f"Path = {IN_PATH}",
        f"Chapter Template = {chapterTemplate}",
        f"binSize = 20"
    ]
    configFile.write("\n".join(configContents))

