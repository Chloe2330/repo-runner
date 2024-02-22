#!/usr/bin/env python3
import subprocess
import sys
import os

if (__name__ != "__main__"):
    exit(1)

if (len(sys.argv) < 2):
    print("Please input an argument")
    exit(1)

if (sys.argv[1] == "--help"):
    print("This script will run commands on every repository in its directory.")
    print("Usage: script.py \"command 1\" \"command 2\" \"command 3\" ...")
    print("Example: ./script.py \"actionlint\" \"ls -a\"")
    exit(0)

# Access the script's directory and get all of its repositories
os.chdir(os.path.dirname(__file__))
repos = []
for item in os.listdir('.'):
    if os.path.exists(item + "/.git/config"):
        repos.append(item)

def run(command, repo):
    temp_file_path = os.path.join(os.getcwd(), "temp.txt")
    with open(temp_file_path, 'w') as file:
        output = subprocess.run(command, shell=True, stdout=file)
        move_files(temp_file_path, repo, command)
        
        # Error code handling
        if output.returncode == 0:
            print("\033[32mNO ERROR\033[00m: \033[33m" + command + "\033[00m on \"\033[36m" + repo + "\033[00m\"")
        else: 
            print("\033[31mERROR\033[00m: \033[33m" + command + "\033[00m on \"\033[36m" + repo + "\033[00m\"")

# Pipe output to text file in results folder 
def move_files(temp, repo, command):
    os.chdir("..")
    folder_name = os.path.join('results', repo)
    os.makedirs(folder_name, exist_ok=True)
    file_name = f"{command.replace(' ', '_')}.txt"
    file_path = os.path.join(folder_name, file_name)
    os.replace(temp, file_path)

# Execute the command on every repository in the folder
for repo in repos:
    os.chdir(repo)
    for i in range(1, len(sys.argv)):
        command = sys.argv[i]
        print("Executing \033[33m" + command + "\033[00m on \"\033[36m" + repo + "\033[00m\"...")
        run(command, repo)
    print()
