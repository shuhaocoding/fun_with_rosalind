'''
calculate the expected number of offspring for each pair of genotypes
AA-AA: 2
AA-Aa: 2
AA-aa: 2
Aa-Aa: 1.5
Aa-aa: 1
aa-aa: 0
E = 2*n1 + 2*n2 + 2*n3 + 1.5*n4 + 1*n5
replace n1-5 with input numbers
'''

E = 2*19095 + 2*19543 + 2*18055 + 1.5*17106 + 1*17275
print(E)

