# this function inputs a json file where each line is a json record and outputs a python data structure which is a dict of dicts
# the first level will index by numeric indices and the second level ( each json's info ) by the json fields

# examples jdata[200]['fans'] or jdata[300].keys()

def parse_user(file):
	import json
	file=open(file)
	jdata={}
	i=0
	for line in file:
		temp=json.loads(line)
		jdata[temp['user_id']]={}
		jdata[temp['user_id']]=temp
		i+=1
	return(jdata)

#def parse_user(path):
#    return [json.loads(line)['user_id'] for line in open(path)]
