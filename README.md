# Actionlint Script
## Run actionlint on every repository in the script's directory. 

### **Quick Start**
Clone this repository. 
```bash
git clone https://github.com/Chloe2330/repo-runner.git
``` 

Install `actionlint` [here](https://github.com/rhysd/actionlint) in the same directory. 

Clone the repositories to run actionlint on.

The following reposities were used to produce the output files in the sample results folder: 
```bash
git clone https://github.com/YetiForceCompany/YetiForceCRM.git
git clone https://github.com/vmware/govmomi.git
```

If actionlint does not detect any issues with the workflow configuration file, the ouput text file will be empty.

### **Usage**
`./script.py actionlint` runs actionlint on every repository\
`./script.py --help` prints script usage\
`./script.py --clear` deletes all folders and output files in the results directory

### **Work in Progress**
- Summarize actionlint results in a json 
- Read and clone repositories from a csv file 
- Fix issues with multiple arguments 

Note: This script works with any command (including git commands). 