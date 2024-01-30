# Start with the first two generations, every pair of rabbits produces k rabbit pairs
i=2
n,k = [int(x) for x in input('Please input n and k, separated by white space ').split()]
a=[1,1]
# Start a loop
while i<n:
# the total pair of rabbits equals the sum of, a[-2]*k, the number of newborn rabbits produced from mature rabbits two generations back, and a[-1], the number of rabbits directly from previous generation.
    x=a[-2]*k+a[-1]
    a.append(x)
    i=i+1
print(a[-1])