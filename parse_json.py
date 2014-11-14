# this function inputs a json file where each line is a json record and outputs a python data structure which is a dict of dicts
# the first level will index by numeric indices and the second level ( each json's info ) by the json fields

# examples jdata[200]['fans'] or jdata[300].keys()

def parse_json(file):
	import json
	file=open(file)
	jdata={}
	i=0
	for line in file:
		jdata[i]={}
		jdata[i]=json.loads(line)
		i+=1
	return(jdata)

#import json
#def parse_json(path):
#    return [json.loads(line) for line in open(path)]
