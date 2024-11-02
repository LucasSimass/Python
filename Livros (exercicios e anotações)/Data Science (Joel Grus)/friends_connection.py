
names = [
    "Lucas",
    "Jhon",
    "Cobby",
    "Josh",
    "Belle",
    "Pedro",
    "Alfred",
    "Michael",
    "Pablo",
    "Leonidas",
]

users = [ 
    {"id": i, "name": names[i] } for i in range(10)
] # create an fake data about a lot of id with the range of 0 to 10

friendship_pairs = [(0,1),(2,1),(4,5),(9,5),(2,8),(8,7),(6,3),(8,0),(2,3),(4,7),(1,4),(8,5)] # A list with 12 tuples, each tuple means a friend connection, in the first tumple for example (friendship_pairs[0]) represents the friend connection between the id 0 and the id 1

friendship = {user["id"]: [] for user in users} # A map with the userId as a key and containing a list value type

for i,j in friendship_pairs: 
    # imagine that: friendship_pairs = [(1,2)]
    # so i = 1; j = 2

    friendship[i].append(j) # example: i = 0, j = 1; so {0:[1]}, the i in that case represent the ID and j the friend we wanna add

    friendship[j].append(i) # it´s the name think but in that case we do the opposite j now is the ID and i is the value 

print(friendship)

def number_of_friends(user):
    user_id = user["id"] # collect the user id 
    user_friends = friendship[user_id] # example: friendship[user_id] = {user_id: [friends]}; friends = [1,2,3]
    return len(user_friends)

total_connections = sum(number_of_friends(user) for user in users)

print(total_connections)

print(number_of_friends(users[0]))

user_numbers = len(users) # output: 10

average_friend_connections = total_connections/user_numbers # get the average number of friends connections 

print(average_friend_connections) # output: 2.4

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users] # a list with a tuple that contains the userId and the number of there friends

print(num_friends_by_id)

# the id_and_friends[1] = number_of_friends(user) in the tupla 
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1] ,reverse=True) # we sort by the number of friends 

print(num_friends_by_id) # output: [(8, 4), (1, 3), (2, 3),...]

# def friend_of_friend(user):
#     friend_of_friend = [
#         fof for friend_id in friendship[user["id"]] # find user friends
#             for fof in friendship[friend_id] # find the friends of user friend
#     ]
#     return friend_of_friend

# print(friendship)
# print(friend_of_friend(users[0]))

from collections import Counter

# foaf = friend of a friend
def friend_of_friend(user):
    user_id = user["id"] 
    return Counter(
        foaf_id for friend_id in friendship[user_id]
        for foaf_id in friendship[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendship[user_id] # if the condition is false it will not include the foaf in the counter 
    )

print(friendship)
print(friend_of_friend(users[1])) # output: the friend of our friends


# interest has 20 possible options that the user can chose
interest_options = [

    "Python", "JavaScript", "C++", "Java", "HTML", "CSS", "React", "Angular", "Vue", "Node.js", "Machine Learning", "Deep Learning", "Inteligência Artificial", "Ciência de Dados", "Big Data", "Cybersecurity", "DevOps", "Cloud Computing", "Realidade Virtual", "Realidade Aumentada"
] # a list with some interest that the IDs could have in common
user_interest = [
    (0, 'Node.js'), (0, 'HTML'), (0, 'Realidade Virtual'), (0, 'Python'), (0, 'Angular'), (0, 'Machine Learning'), (0, 'Cybersecurity'),(1, 'Java'), (1, 'Angular'), (1, 'Machine Learning'), (1, 'Realidade Aumentada'), (1, 'Inteligência Artificial'), (1, 'Cybersecurity'), (1, 'Python'),(2, 'Ciência de Dados'), (2, 'CSS'), (2, 'Deep Learning'), (2, 'Cloud Computing'), (2, 'Cybersecurity'), (2, 'C++'), (2, 'DevOps'),(3, 'Deep Learning'), (3, 'React'), (3, 'C++'), (3, 'Realidade Virtual'), (3, 'Java'), (3, 'HTML'), (3, 'Cybersecurity'),(4, 'React'), (4, 'Angular'), (4, 'Java'), (4, 'Node.js'), (4, 'Machine Learning'), (4, 'C++'), (4, 'DevOps'),(5, 'C++'), (5, 'JavaScript'), (5, 'Cloud Computing'), (5, 'Realidade Aumentada'), (5, 'React'), (5, 'Cybersecurity'), (5, 'Java'),(6, 'DevOps'), (6, 'JavaScript'), (6, 'Angular'), (6, 'HTML'), (6, 'Vue'), (6, 'Cybersecurity'), (6, 'Big Data'),(7, 'Realidade Aumentada'), (7, 'CSS'), (7, 'Cloud Computing'), (7, 'Python'), (7, 'Java'), (7, 'C++'), (7, 'HTML'),(8, 'Ciência de Dados'), (8, 'Machine Learning'), (8, 'Cybersecurity'), (8, 'Angular'), (8, 'Big Data'), (8, 'Cloud Computing'), (8, 'DevOps'),(9, 'Vue'), (9, 'Realidade Aumentada'), (9, 'JavaScript'), (9, 'CSS'), (9, 'React'), (9, 'Ciência de Dados'), (9, 'Deep Learning')
]

def interest_connection(target_interest):
    return [user_id for user_id, user_interest in user_interest
        if user_interest == target_interest         
    ] # find the interest 

print(interest_connection(interest_options[0]))

from collections import defaultdict

interest_by_user_ids = defaultdict(list)

for user_id, interest in user_interest:
    interest_by_user_ids[user_id].append(interest) # put it all into a map divide by keys (user_ids), for example {0: ["Java", "C++"...], 1: ["Ruby", "PHP"]...etc}

user_ids_by_interest = defaultdict(list)

for user_id, interest in user_interest:
    user_ids_by_interest[interest].append(user_id) # put it all into a map divide by the key (interest), for example {'Node.js': [0, 4], 'HTML': [0, 3, 6, 7], 'Realidade Virtual': [0, 3]...etc}

print(user_ids_by_interest)
print("-" * 20)
print(interest_by_user_ids)

def common_interest(user):
    return Counter(
        interest_user_id for interest in interest_by_user_ids[user["id"]] # we get all the interest that the user have
        for interest_user_id in user_ids_by_interest[interest] # the user id is a key an check how much interest each user have in common if it´s 0 (dont have any same interest) it will not show up
        if interest_user_id != user["id"] # check if the user it´s not the same user as selected
    )
    pass # users that have common interest with the user selecte

print(common_interest(users[0]))
print(users[0])

# Usefull but i still dont know how it works  
word_and_counts = Counter(
    word for user, interest in user_interest
    for word in interest.lower().split()
)

print(word_and_counts)
