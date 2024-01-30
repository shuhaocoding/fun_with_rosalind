# n: the number of total generations; each rabbit lives for m months.
n,m = [int(x) for x in input('Please input n and m, separated by white space ').split()]
g=3; total = [1,1]; newborn = [0,1]; dead = [0,0] # g is the number of current generation; generate two lists that store the total number of rabbits / the number of newborn rabbits as two sequences; start with the third generation.

while g<=m:
    current_dead = 0  # no rabbit dies
    current_newborn = total[-2] - dead[-1]
    current_total = total[-1] + current_newborn - current_dead
    dead.append(current_dead); newborn.append(current_newborn); total.append(current_total)
    g+=1

while g<=n:
    current_dead = newborn[-m]
    current_newborn = total[-2] - dead[-1]
    current_total = total[-1] + current_newborn - current_dead
    dead.append(current_dead); newborn.append(current_newborn); total.append(current_total)
    g+=1

print(total[-1])