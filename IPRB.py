k=24; m=21; n=26;
T=k+m+n
p2=T*(T-1)/2.0
m2=m*(m-1)/2.0
n2=n*(n-1)/2.0
p_rec=n2/p2+m2/p2*0.25+n*m/p2*0.5
p_dor=1-p_rec
print p_dor
