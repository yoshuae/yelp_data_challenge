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
