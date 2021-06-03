lst = []
for i in range(1,11):
    lst.append(i)
lst.insert(11,11)
print(lst)
lst1 = [1,2,3,4,5,6,7,8,9,10]
a = set(lst)
b = set(lst1)
if a==b:
    print('1')
else:
    print('0')
list1 = list(lst)
print(list1)
list1 = list((10,20,40,50,30,9))
list1.sort()
print('The sorted elements in a list are:')
print(list1)
list1.reverse()
print('The reversed elements in a list are:')
print(list1)
list1.remove(9)
print('The updated elements in list1 are:')
print(list1)
list1.pop(2)
print('The popped element in a specified position is ')
print(list1)
