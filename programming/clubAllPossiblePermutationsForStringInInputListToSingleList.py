'''
inputList = ['cerg', 'sample', 'cegr', 'cgre', 'cger', 'samlep', 'samepl', 'samelp', 'sapmle', 'saurabh', 'hbaruas']
outPutList = [['cerg', 'cegr', 'cgre', 'cger'], ['sample','samlep', 'samepl', 'samelp', 'sapmle'], ['saurabh', 'hbaruas']]
'''

from itertools import permutations
outPutList = []
def clubAllPossiblePermutationsForStringInInputListToSingleList(inputList):
	possiblePerms = []
	possiblePermsDict = {}
	for name  in inputList:
		possiblePerms = [''.join(p) for p in permutations(name)]
		nameList = []	
		for item in inputList:			
			if item in possiblePerms:
				nameList.append(item)
		outPutList.append(nameList)
		for i in nameList:
			while i in inputList:
				inputList.remove(i)
	return outPutList

inputList = ['cerg', 'sample', 'cegr', 'cgre', 'cger', 'samlep', 'sampl', 'samelp', 'sapmle', 'saurabh', 'hbaruas','saurabh']
myoutput = clubAllPossiblePermutationsForStringInInputListInSingleList(inputList)
print myoutput







