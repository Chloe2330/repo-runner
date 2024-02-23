#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil

if (__name__ != "__main__"):
    exit(1)

if (len(sys.argv) < 2):
    print("Please input an argument")
    exit(1)

# Usage of script 
if (sys.argv[1] == "--help"):
    print("This script will run commands on every repository in its directory.")
    print("Usage: script.py \"command 1\" \"command 2\" \"command 3\" ...")
    print("Example: ./script.py \"actionlint\" \"ls -a\"")
    exit(0)

# Clear output files 
if (sys.argv[1] == "--clear"):
    print("This script will clear out output text files in the results directory.")
    user_input = input("Do you want to execute this command? (y/n): ").lower()

    # User confirms deletion 
    if user_input == 'y':
        current_folder = os.getcwd()
        results_path = os.path.join(current_folder, "results")

        # Check if results folder exists 
        if os.path.exists(results_path):
            for item in os.listdir(results_path):
                item_path = os.path.join(results_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file: {item_path}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Deleted directory: {item_path}")
        else:
            print("No results to delete.")
    else:
        print("Exiting...")
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

    # Create results folder if it does not exist
    os.makedirs(folder_name, exist_ok=True)

    file_name = f"{command.replace(' ', '_')}.txt"
    file_path = os.path.join(folder_name, file_name)

    # Move output from temp path to results path 
    os.replace(temp, file_path)

# Execute the command on every repository in the folder
for repo in repos:
    os.chdir(repo)
    for i in range(1, len(sys.argv)):
        command = sys.argv[i]
        print("Executing \033[33m" + command + "\033[00m on \"\033[36m" + repo + "\033[00m\"...")
        run(command, repo)
    print()
