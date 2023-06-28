n=36; k=4; a=[1,1]; i=2;
while i<n:
    x=a[-2]*k+a[-1]
    a.append(x)
    i=i+1
print a[-1]
