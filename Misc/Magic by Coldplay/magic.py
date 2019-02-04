#!/usr/bin/python3
import sys
import signal
import os
import random

# List of files.
file_list = []

# List all files in the folder.
for (root, dirs, files) in os.walk(".", topdown = False):
	for name in dirs:
		current_dir = "./"+name
		for (c_root, c_dirs, c_files) in os.walk(current_dir, topdown = False):
			for file_name in c_files:
				file_list.append(current_dir+"/"+file_name)

file_list = random.sample(file_list, len(file_list))

print("Identify the file type and enter the extension in caps.\n")

# Iterate over all files in file_list.
for k in range(len(file_list)):
	# Open file to read.
	fp = open(file_list[k], 'rb')
	data = fp.read()
	data = data[0:50]
	# Send prompt.
	extension = file_list[k].split('.')
	print(repr(data))
	inp = input(">> ")
	if(inp != extension[2].upper()):
		print("I don't feel so good.")
		sys.exit()

print("evlz{thanos_tapped_you_back_in}ctf\n")
