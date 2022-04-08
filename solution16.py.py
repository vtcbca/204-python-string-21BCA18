l=[]
def creatlist():
    for i in range(2):
        s=input("Enter string")
        l.append(s)
    return(creatlist)    
def even(l):
    count=0
    for i in l:
        for j in i:
            if(j%2==0):
                print("total string of even {} character:".format(j))
                count+=1
    return(even)
creatlist()
ans=even(l)
print(ans)
       
        
