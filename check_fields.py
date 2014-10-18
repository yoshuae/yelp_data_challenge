# compile json parsing function
execfile('../parse_json.py')
execfile('../parse_user.py')
execfile('../network_troll.py')

# data is loaded in pwd
users=parse_user('user.json')
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

# some basic exploratory analysis
stars=[users[x]['average_stars'] for x in range(len(users))]
#population average number of stars ~3.7
pop_avg_stars=sum(stars)/len(stars)

num_friends=[len(users[x]['friends']) for x in range(len(users))]
#population average number of ratings ~7.56
pop_avg_friends=sum(num_friends)*1.0/len(num_friends)

num_fans=[users[x]['fans'] for x in range(len(users))]
# population average number of fans ~1.67
pop_avg_fans=sum(num_fans)*1.0/len(num_fans)
temp_users=parse_user('user.json')
# reach of each user
reach=find_reach(temp_users)  # return list with counts, not dict with key user_id
# build pandas df of user info pass to csv for analysis with R
import pandas as pd
users=parse_json('user.json') # reinitialize so we can access by number key rather than user_id
user_name=[users[x]['name'] for x in range(len(users))]
df=pd.DataFrame(data=user_name,columns=['name'])

df['avg_stars']=[users[x]['average_stars'] for x in range(len(users)) ]
df['review_count']=[users[x]['review_count'] for x in range(len(users)) ]
df['yelping_since']=[users[x]['yelping_since'] for x in range(len(users)) ]
df['num_friends']=[len(users[x]['friends']) for x in range(len(users))] # just number of immediate friends
df['fans']=[users[x]['review_count'] for x in range(len(users))]
df['funny_votes']=[users[x]['votes']['funny'] for x in range(len(users))]
df['useful_votes']=[users[x]['votes']['useful'] for x in range(len(users))]
df['cool_votes']=[users[x]['votes']['cool'] for x in range(len(users))]
df['user_id']=[users[x]['user_id'] for x in range(len(users))]
df['user_reach']=[reach[x] for x in df['user_id']]    #number of friends + their friends 

df=df.drop('user_id',1) # drop extra column

# write to csv and do analysis in R :) 
df.to_csv('parsed_to_df.csv',index=False,encoding='utf8')










