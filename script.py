from pathlib import Path
import os
import json

repo_path = Path.cwd()

dict = dict()

for folder in os.listdir(repo_path):
    print (folder)
    if '.py' in folder or 'vs' in folder or '.git' in folder or '.json' in folder: continue

    files = os.listdir(os.path.join(repo_path, folder))
    dict[folder] = []

    for file in files:
        dict[folder].append(file)

print ("\ndictionary content:\n")
print (dict)

f = open(os.path.join(repo_path, 'catalog.json'),'w')
json.dump(dict, f, indent = 2, separators=(',', ":"))