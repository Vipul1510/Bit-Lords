import matplotlib.pyplot as plt
import numpy as np
import os
filenames=[]

directory = "Evaluations_results"

for filename in sorted(os.listdir(directory)):
    if filename.endswith(".txt"):
        filenames.append(filename)

with open(directory+"/"+filenames[0], 'r') as f1:
    data1 = [line.strip().split() for line in f1.readlines()]
    
with open(directory+"/"+filenames[1], 'r') as f2:
    data2 = [line.strip().split() for line in f2.readlines()]

with open(directory+"/"+filenames[2], 'r') as f3:
    data3 = [line.strip().split() for line in f3.readlines()]

with open(directory+"/"+filenames[3], 'r') as f4:
    data4 = [line.strip().split() for line in f4.readlines()]

with open(directory+"/"+filenames[4], 'r') as f5:
    data5 = [line.strip().split() for line in f5.readlines()]




fig, ax = plt.subplots(figsize=(14, 10.5))
combined_data = []
k=0
mul1=1
mul2=1
mul3=1
mul4=1
mul5=1
for row in data1:
    name=row[0].split('.trace.gz')[0]
    name=name.split('.champsimtrace')[0]
    value1=row[1]
    mul1*=float(value1)
    value2 = data2[k][1]
    mul2*=float(value2)
    value3 = data3[k][1]
    mul3*=float(value3)
    value4 = data4[k][1]
    mul4*=float(value4)
    value5 = data5[k][1]
    mul5*=float(value5)
    k+=1
    combined_data.append((name, float(value1), float(value2),float(value3),float(value4),float(value5)))

# Sort the data by name
combined_data.sort(key=lambda x: x[0])

# Extract the data into separate lists for plotting
names = [x[0] for x in combined_data]
values1 = [x[1] for x in combined_data]
values2 = [x[2] for x in combined_data]
values3 = [x[3] for x in combined_data]
values4 = [x[4] for x in combined_data]
values5 = [x[5] for x in combined_data]

N = len(names)
ind = np.arange(N) 
width = 0.164


bar1 = plt.bar(ind, values1, width, color='r')
bar2 = plt.bar(ind+width, values2, width, color='c')
bar3 = plt.bar(ind+2*width, values3, width, color='y')
bar4 = plt.bar(ind+3*width, values4, width, color='m')
bar5 = plt.bar(ind+4*width, values5, width, color='b')

plt.axhline(y=mul1**(1/len(names)), color='r', linestyle='--')  # Add a horizontal line at y
plt.axhline(y=mul2**(1/len(names)), color='b', linestyle='--')
plt.axhline(y=mul3**(1/len(names)), color='g', linestyle='--')
plt.axhline(y=mul4**(1/len(names)), color='y', linestyle='--')
plt.axhline(y=mul5**(1/len(names)), color='c', linestyle='--')
for i in range(len(filenames)):
    filenames[i]=filenames[i].replace(".txt","").replace(f"_graphs","")

with open('evaluations.txt', 'w') as f:
    print(directory,file=f)
    print(f"Cummulative ipc of {filenames[0]}:",mul1**(1/len(names)),file=f)
    print(f"Cummulative ipc of {filenames[1]}:",mul2**(1/len(names)),file=f)
    print(f"Cummulative ipc of {filenames[2]}:",mul3**(1/len(names)),file=f)
    print(f"Cummulative ipc of {filenames[3]}:",mul4**(1/len(names)),file=f)
    print(f"Cummulative ipc of {filenames[4]}:",mul5**(1/len(names)),file=f)
plt.xlabel("Traces")
plt.ylabel('IPC') # or IPC or MISS RATE
plt.title("IPC comparison")
plt.xticks(ind+(2.5)*width, names)
plt.xticks(rotation=90)
plt.legend((bar1, bar2, bar3, bar4, bar5), (filenames[0], filenames[1], filenames[2],filenames[3],filenames[4]))
#plt.ylim(ymin=100000)
#plt.ylim(0, 1.15)
# Adjust top margin
fig.subplots_adjust(top=0.95)
plt.savefig("Evaluations_results.png")
