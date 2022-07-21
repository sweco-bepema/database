from pathlib import Path
import os
import json

repo_path = Path.cwd()

list_elements = []

for folder in os.listdir(repo_path):
    print (folder)
    if '.py' in folder or 'vs' in folder or '.git' in folder or '.json' in folder: continue

    files = os.listdir(os.path.join(repo_path, folder))
    d = dict()
    d['Name'] = folder
    d['Files'] = []
    for file in files:
        d['Files'].append(file)

    list_elements.append(d)

print ("\ndictionary content:\n")
print (list_elements)

f = open(os.path.join(repo_path, 'catalog.json'),'w')
json.dump(list_elements, f, indent = 2, separators=(',', ":"))