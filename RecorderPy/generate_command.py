from os import listdir
from os.path import isfile, join
import re
import pyperclip

mypath = r"C:\Users\Jaskaran\gesture\data\clean"
bvhlist = []
wavlist = []
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:

    match1 = re.search("\.bvh$", file)

    if match1:
        bvhlist.append(file)

    match2 = re.search("\.wav$", file)

    if match2:
        wavlist.append(file)

print("\nBVH files :\n")
i=0
j=0
for file in bvhlist:
    print("  ",i+1,"  |  ",file)
    print("-----------------------------------------")
    i+=1
val = int(input("\nSelect the file"))
bvh = bvhlist[val-1]


print("\nWAV files:\n")

for file in wavlist:
    print("  ",j+1,"  |  ", file)
    print("-----------------------------------------")
    j+=1
val = int(input("\nSelect the file"))
wav = wavlist[val-1]

command = 'python ./generate.py -o "../data/outputs/v1/options.json" -s "../data/clean/'+bvh+'" -a "../data/clean/'+wav+'"'

print(command)

pyperclip.copy(command)
pyperclip.paste()


