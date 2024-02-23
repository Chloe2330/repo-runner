#!/usr/bin/env python3
import os
import sys
import subprocess
import csv 

if (__name__ != "__main__"):
    exit(1)

if len(sys.argv) != 2:
    print("Please enter a valid input.")
    exit(1)

if sys.argv[1] == "--help":
    print("This script will download all the repositories in a csv file.")
    print("Usage: read_csv.py [csv file name]")
    print("Example: ./read_csv.py sample.csv")
    exit(0)

os.chdir(os.path.dirname(__file__))
file_name = sys.argv[1]
file_path = os.path.join(os.getcwd(), file_name)

repos = []

# Open the csv file and read its contents
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    for row in csv_reader:
        # Each 'row' variable represents a dictionary where keys are column names
        repos.append(row["URL"])

for url in repos:
    command = ['git', 'clone', url]
    try:
        # Clone each repository 
        subprocess.run(command, check=True)
        print(f"Repository cloned successfully: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository {url}: {e}")
