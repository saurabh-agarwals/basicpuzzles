'''
items = [2,2,9,3,4,6,8]
find a-b = k
let say k =6 above then output should be 8-2 = 6
'''
from itertools import permutations

def calculateABK(itemList,k):
	items = [2,2,9,3,4,6,8]
	for p in permutations(items, 2):
		 if abs(p[0] - p[1]) == k:
		 	print p

items = [2,2,9,3,4,6,8]
k = 6
calculateABK(items,k)