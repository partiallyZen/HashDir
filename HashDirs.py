import os
import hashlib
import csv

hashs=(input("What hash are you looking for?"))

for root, subdirs, files in os.walk('c:/Users/chick/Desktop/School/suspicious_files/suspicious_files/'):
    checksums = []
    for file in files:
        with open(os.path.join(root, file), 'rb') as _file:
            wr = csv.writer(_file, dialect='excel')
            checksums.append([root, file, hashlib.md5(_file.read()).hexdigest()])

for row in checksums:
    if hashs in row:
        print("This hash corresponds to this file: ", row[-2])

