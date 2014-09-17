# for each user count the number of users within two degrees of seperation
# i.e. the extent of your friends + 'friends of friends' 
# users jdata object
# takes a long time to run, still thinking about faster graph algorithms/python data structures

def find_reach(jdata_user):
	reach={}
# for each users friends , build a list of the friends of friends, unroll it, and count distinct using the python set operator. 	
	for user in jdata_user.keys():
		temp=[jdata_user[x]['friends'] for x in jdata_user[user]['friends']]
		temp.extend(jdata_user[user]['friends'])
		temp2=[item for sublist in temp for item in sublist]
		reach[user]=len(set(temp2))
# return dict with key=users and value=number of second degree connections
	return(reach)








