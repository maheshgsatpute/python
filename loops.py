# loops 
#range (startindex , endindex , stepsize)
# startindex is by default 0
# endindex is not include
# stepsize is by default +1 

#print 1 to 10
for x in range(11):
    print(x)

for x in range(1,11):
    print(x)

#print table of 2

for x in range(2,21,2):
    print(x)

#print table of 2
        
for x in range(1,11):
    print(x*2)

#print table of 5

for x in range(5,51,5):
    print(x)            

for x in range(1,11):
    print(x*5)    

#print 0 to 10 in reversed order
for x in range(10,-1,-1):
    print(x)    

#print 1 to 10 in reversed
for x in range(10,0,-1):
    print(x)

#print table of 2 in reversed order
for x in range(20,1,-2):
    print(x)

#print table of 5 in reversed order
for x in range(50,4,-5):
    print(x)             

#break , continue
# break is used to take exit from the loop
 
#print 1 to 10 ====>7 exit
for x in range(11):
    if(x==7):
        break
    print(x) 

for x in range(11):
    print(x)                  # here it will print 7 as well because it print the number first and then check the condition
    if(x==7):
        break           


#print table of 2 and exit on 16
for x in range(2,21,2):
    if(x==16):
     break
    print(x)    

#print table of 2 and exit on 17
for x in range(2,21,2):
    if(x==17):
        break               # it will never break as 17 will not come in table of 2
    print(x)    


#continue

#print 0 to 10===> 7 skip
for x in range(11):
    if(x==7):
        continue
    print(x)

#print table of 2 and skip 16
for x in range(2,21,2):
    if(x==16):
        continue
    print(x)    

#print table of 5 and skip 30
for x in range(5,51,5):
    if(x==30):
        continue
    print(x) 

#print 1 to 10 in reversed and skip 5
for x in range(10,0,-1):
    if(x==5):
        continue
    print(x)

#print table of 5 in reversed and skip 45
for x in range(50,0,-5):
    if(x==45):
        continue
    print(x)           
