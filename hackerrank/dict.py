n=int(input())
d= {}
s=0
for i in range(n):
    keys=input('e keys')
    values=int(input('e values'))
    d[keys]=values
    s=s+i
    a= values/n
print('{:.2f}'.format(a))