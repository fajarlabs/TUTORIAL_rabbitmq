#!/usr/bin/python
import os
import sys

print("Clear data...")
os.system("rm /tmp/store.log")

total_spawn = sys.argv[1]

print("Start spawn...")
for i in range(1,int(total_spawn)):
    os.system("echo '1.12.16.12345."+str(i)+"' >> /tmp/store.log")

print("Spawn finish...")
