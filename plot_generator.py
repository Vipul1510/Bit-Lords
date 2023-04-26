import matplotlib.pyplot as plt
import numpy as np
file1="changed_ipcp"
file2="ipcp"

with open(file1, 'r') as f1:
    data1 = [line.strip().split() for line in f1.readlines()]
    
with open(file2, 'r') as f2:
    data2 = [line.strip().split() for line in f2.readlines()]
    
fig, ax = plt.subplots(figsize=(14, 10.5))
combined_data = []
k=0
mul1=1
mul2=1
for row in data1:
    name=row[0].split('.trace.gz')[0]
    name=name.split('.champsimtrace')[0]
    value1=row[1]
    mul1*=float(value1)
    value2 = data2[k][1]
    mul2*=float(value2)
    k+=1
    combined_data.append((name, float(value1), float(value2)))

# Sort the data by name
combined_data.sort(key=lambda x: x[0])

# Extract the data into separate lists for plotting
names = [x[0] for x in combined_data]
values1 = [x[1] for x in combined_data]
values2 = [x[2] for x in combined_data]

N = len(names)
ind = np.arange(N) 
width = 0.35


bar1 = plt.bar(ind, values1, width, color='r')
bar2 = plt.bar(ind+width, values2, width, color='b')

plt.axhline(y=mul1**(1/len(names)), color='r', linestyle='--')  # Add a horizontal line at y
plt.axhline(y=mul2**(1/len(names)), color='b', linestyle='--')
file1=file1.replace(".txt","")
file2=file2.replace(".txt","")
print(f"Cummulative ipc of {file1}:",mul1**(1/len(names)))
print(f"Cummulative ipc of {file2}:",mul2**(1/len(names)))

plt.xlabel("Traces")
plt.ylabel('IPC') # or IPC or MISS RATE
plt.title("IPC comparison")
plt.xticks(ind+width/2, names)
plt.xticks(rotation=90)
plt.legend((bar1, bar2), (file1, file2))
#plt.ylim(ymin=100000)
#plt.ylim(0, 1.15)
# Adjust top margin
fig.subplots_adjust(top=0.95)
plt.savefig(f"{file1}_{file2}.png")