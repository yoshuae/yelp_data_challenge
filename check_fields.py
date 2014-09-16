# compile json parsing function
execfile('../parse_json.py')

# data is loaded in pwd
users=parse_json('user.json')
tips=parse_json('tip.json')
reviews=parse_json('review.json')
checkins=parse_json('checkin.json')
business=parse_json('business.json')

# some integrity checks to make sure all of our fields are present 
[len(users[x]) for x in range(len(users))]/len(users)
[len(tips[x]) for x in range(len(tips))]/len(tips)
[len(reviews[x]) for x in range(len(reviews))]/len(reviews)
[len(checkins[x]) for x in range(len(checkins))]/len(checkins)
[len(business[x]) for x in range(len(business))]/len(business)

