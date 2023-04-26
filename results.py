import os
import re
import sys

directory = "results_30M"
pattern = r'cumulative IPC:\s*(\d+\.\d+)'

line_number = 28


with open('results.txt', 'w') as f:
    for filename in sorted(os.listdir(directory)):   
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename)) as file1:
                lines = file1.readlines()
                if len(lines)>= line_number:
                    match = re.search(pattern, lines[line_number - 1])
                    if match:
                        cumulative_ipc = match.group(1)
                        print(f"{filename}: {cumulative_ipc}",file=f)
                    else:
                        print(f"{filename}: No matching",file=f)
                else:
                    print(f"{filename}: Results are not complete",file=f)
