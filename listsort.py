list1 = [int(i) for i in input().split()]
list2 = [int(j) for j in input().split()]
list1 += list2
list1.sort()
print(list1)
'''
Output:
45 33 41 -1 32 88
44 30 17 43 10 98
[-1, 10, 17, 30, 32, 33, 41, 43, 44, 45, 88, 98]
