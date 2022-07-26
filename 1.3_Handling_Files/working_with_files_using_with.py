# In linux, the ulimit -n command  tells us how many files opened simultaneously can your handle

n_files = 10
files = []

#create n_files
for i in range(n_files):
        with open(f'/home/fellyka/Desktop/Desktop/sample{i}.txt', 'w') as f:
           files.append(f)


