n=96; m=16; a=[1,1]; i=2; j=m; k=m+2
while i<m:
    x=a[-2]+a[-1]
    a.append(x)
    i=i+1
while j<m+2:
    x=a[-2]+a[-1]-1
    a.append(x)
    j=j+1
while k<n:
    x=a[-2]+a[-1]-(a[-m]-a[-m-2])
    a.append(x)
    k=k+1
print(a[-1])
