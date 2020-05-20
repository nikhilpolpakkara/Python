#Created by: Nikhil Polpakkara
#%%
#Python from scratch - practice
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
# this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i
    
def number_of_friends(user):
    """how many friends does _user_ have?"""
    a = len(user['friends'])
    b = user['name']
    return len(user["friends"]) # length of friend_ids list

total_connections = sum(number_of_friends(user) for user in users)

list_ = []
for user in users:
    a = len(user['friends'])
    b = user['name']
    c = (a,b)
    list_.append(c)
    list_.sort()
"""    
2 : Hero
3 : Dunn
3 : Sue
3 : Chi
2 : Thor
3 : Clive
2 : Hicks
2 : Devin
3 : Kate
1 : Kleinl
"""
#%%
def friends_of_friend(user):
# "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"] # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_ friends
#%%
#Mutual friends algorithm
from collections import Counter # not loaded by default
def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]
def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])
def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"] # for each of my friends
                   for foaf in friend["friends"] # count *their* friends
                   if not_the_same(user, foaf) # who aren't me
                   and not_friends(user, foaf)) # and aren't my friends
print(friends_of_friend_ids(users[0]))
#%%
#Interests
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
"""
This works, but it has to examine the whole list of interests for every search. If we
have a lot of users and interests (or if we just want to do a lot of searches), we’re probably
better off building an index from interests to users
"""

from collections import defaultdict
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest) 

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])
#%%
#Most number of interests
    words_and_counts = Counter(word
                               for user, interest in interests
                               for word in interest.lower().split())
    for word, count in words_and_counts.most_common():
        if count > 1:
            print(word, count)
#%%
#salaries of employees
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

def average(x,list_):
    sum_= 0
    for thing in list_:
        sum_=sum_+thing[x]
    average_ = sum_/len(list_)
    return average_

average(1,salaries_and_tenures)
#%%
# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)    
    
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
#Then group together the salaries corresponding to each bucket:
# keys are tenure buckets, values are lists of salaries for that bucket

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

#And finally compute the average salary for each group:
# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {tenure_bucket : sum(salaries) / len(salaries)
                            for tenure_bucket, salaries in salary_by_tenure_bucket.items()}
#%%
