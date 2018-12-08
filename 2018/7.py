from collections import defaultdict

with open('7.in') as f:
    instructions = f.readlines()
    instructions = [(inst.split()[1], inst.split()[-3]) for inst in instructions]


dependencies = defaultdict(list)

done = list()
steps = set()
for inst in instructions:
    dependencies[inst[1]].append(inst[0])
    steps.add(inst[1])
    steps.add(inst[0])


# 
# Step J must be finished before step C can begin.
# dependencies[C] = [J]

# dependencies of C is a list of things that has to happen first


for step in steps:
    if step not in dependencies:
        dependencies[step] = []


original_dependencies = {key:list(values) for key,values in dependencies.items()}



while(True):

    try:
        nexteval = sorted([key for key in dependencies if len(dependencies[key]) == 0])[0]

        done.append(nexteval)
        del dependencies[nexteval]

        for key in dependencies:
            if nexteval in dependencies[key]:
                dependencies[key].remove(nexteval)
    except:
        break

# Part I
print(''.join(done))

workers = [('_',0)] * 5
second = 0
dependencies = original_dependencies

while(True):
    # assign each free worker a job
    # do a second of work



    for i in range(0,len(workers)):
        if workers[i][1] == 0:
            
            nextjob = sorted([key for key in dependencies if len(dependencies[key]) == 0])

            if len(nextjob) > 0:
                nextjob = nextjob[0]
                workers[i] = (nextjob, ord(nextjob) - ord('A') + 60)
                del dependencies[nextjob]





            else:
                nextjob = None
        else:
            workers[i] = (workers[i][0],workers[i][1] - 1)

    for i in range(0,len(workers)):
        if workers[i][1] == 0:
            prevjob = workers[i][0]
            if prevjob != '_':
                for key in dependencies:
                    if prevjob in dependencies[key]:
                        dependencies[key].remove(prevjob)

            workers[i] = ('_',0)



    

    second += 1


    if sum([_[1] for _ in workers]) == 0 and len(dependencies) == 0:
        break





print(second)
