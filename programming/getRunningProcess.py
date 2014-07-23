'''
let say data is :
time message  pid
1000 starting 1
1001 starting 2
1002 finishing 2
1003 starting 3
1004 finishing 1
1010 finishing 4
'''

'''
returnDictForProcess will return the dictionary with key/value pair for each process example:
{
    '1': {
        'state': [
            'starting',
            'finishing'
        ],
        'pid': '1',
        'time': '1000'
    },
    '3': {
        'state': [
            'starting'
        ],
        'pid': '3',
        'time': '1003'
    },
    '2': {
        'state': [
            'starting',
            'finishing'
        ],
        'pid': '2',
        'time': '1001'
    },
    '4': {
        'state': [
            'finishing'
        ],
        'pid': '4',
        'time': '1010'
    }
}
'''

def returnDictForProcess(filename):
	processDict = {}
	f = open(filename,'r')
	process = f.readlines()[1:]
	f.close()
	for line in process:
		myline = line.split()
		eachProcess = {'state':[myline[1]], 'time':myline[0],'pid':myline[2]}		
		if processDict.has_key(myline[2]):
			processDict[myline[2]]['state'].append(myline[1])
		else:
			processDict[myline[2]] = eachProcess
	return processDict

'''
printAllRunningProcess prints only the running process, this will lookup in state list for each pid and if finishing for
	that process does not exits then it turns out to be still running process.
'''

def printAllRunningProcess(filename):
	processes = returnDictForProcess(filename)
	template = "{0:8} {1:10} {2:15}"
	print template.format("TIME" , "PID" , "STATE")
	#print processes
	for pid in processes:
		if 'finishing' not in processes[pid]['state']:
			print template.format(processes[pid]['time'], processes[pid]['pid'], str(processes[pid]['state']))

printAllRunningProcess("process.txt")