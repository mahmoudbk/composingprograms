#lets make a function that counts the number of appearance of a certain value 
#we will use a while loop in this case 

def count(s,value):
    
    l,i,sum = len(s),0,0
    while(i<l):
        if(s[i]==value):
            sum+=1

        i+=1
    return sum


"""
>>> count([6,2,3,2,7,2,2],2)
"""
