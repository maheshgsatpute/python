
#slicing and list comprehension

#slicing
#       0  1  2  3  4
num = [10,20,30,40,50]

print(num[1:])

#syntax 
#list-name[startIndex:endIndex(notIncluded):stepSize]
#startIndex ==> default 0
#endIndex (notIncluded) ==> end of list
#stepSize ==> default 1

#slicing from bigining
print(num[:4])

#slicing till end
print(num[2:])

#print list
print(num[:])

#       0  1  2  3  4
num = [10,20,30,40,50]

#print list in reveres
print(num[::-1])

#list Comprehension - list Comprehension provides a short, fast, clean way to create lists.

num= [1,2,3,4,5,6]
squared =[x*x for x in num]
print(squared)

#syntax
#[expression for items in iterable ]


#create list of 0 to 10
numbers =[x for x in range(11) ]
print(numbers)

#create list of 1 to 10
numbers1 =[y for y in range(1,11)]
print(numbers1)


#find even numbers
nums =[11,45,66,78,77,43,4,7,10,12]
even =[x for x in nums if x % 2==0]
#      expression  forloop   condition
print(even)

odd =[x for x in nums if x % 2!=0]
print(odd)

# convert ecaname in to upper case 

names =["dipanshu","tanish","nitin","neel"]

upper_names =[x.upper() for x in names]
print(upper_names)

#[1,2], [3,4] ==> [1,3],[1,4],[2,3],[2,4]

pairs =[(x,y) for x in [1,2] for y in [3,4]]
print(pairs)

a= ["a","b","c"]
b= [1,2,3]

new_pairs =[(x,y) for x in(a) for y in(b)]
print(new_pairs)

# x="a"   y=1,2,3
# x="b"   y=1,2,3
# x="c"   y=1,2,3

#          0     1     2   
#         0 1   0 1   0 1  
listA = [[1,2],[3,4],[5,6]]
print(listA[1])
print(listA[0][0])
print(listA[2][0])






