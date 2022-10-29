"""we want to solve for 900"""
ts = [100,300,500,700]
ps = [927,878,826,771]
x = 900
h =  (ts[1]-ts[0])
q = (900-ts[0])/h

L = len(ps)

def deltay(i):
    return ps[i+1]-ps[i]

def deltayp(p,i):
    if p==1:
        return deltay(i)
    return pow(deltayp(p-1,i+1),p-1) - pow(deltayp(p-1,i),p-1)
s = ps[0]
tolerance  = 1
fact =  1
for i in range(1,L-1):
    s1 =s 
    fact = fact*i

    delta = deltayp(i,0)
    
    s = s + (q*(delta))/fact
    q = q*(q-1)
    if abs(s1-s)<=tolerance:
        break
    

   
   

print(s)