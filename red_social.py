# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
   
# Background
# ======
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    network = {}
    if(string_input == ""):
        return network
    conection = []
    games = []
    d  =""
    aux = []
    aux_infinite = []
    aux_lista = []
    aux = string_input.split()
    aux_2 = ""
    aux_3 = []
    z = 0
    for x in aux:
        if(x =="is" or x == "likes"  or x == "to"):
            aux.remove(x)
            
    while z < len(aux):
        aux_3 = aux[z].split(".")
        if(len(aux_3) > 1):
            aux_infinite.append(z)
            aux_lista.append(aux_3[0])
            aux_lista.append(aux_3[1])
            aux_3 =""
            z+=1
        else:
            aux_lista.append(aux[z])
            z+=1
    aux = aux_lista
    mas = [[],[]]
    network[aux[0]] = [[],[]]
    h = ""
    network[aux[0]] = [[],[]]
    x = 0
    y= 0
    j= aux[0]
    while(x<len(aux)):
        y= x
        mas,x = create_data_structure_aux(aux,x,aux[y])
        j = aux[y]
        network[aux[y]] = mas
    return network
    
    
def create_data_structure_aux(aux,z,j):
    mas = [[],[]]
    x = aux[z:].index("connected")+ 1 +z 
    y = aux[z:].index("play") + z
    while(x<y-1):
        if(aux[x] == "to"  ):
            x+=1
        else:
            if(aux[x] == j):
                x+=1
            else:
                a =aux[x]
                if(a[len(a)-1]==","):
                    mas[0].append(a[:len(a)-1])
                    x+=1
                else:
                    mas[0].append(aux[x])
                    x+=1
    
    if("connected" in aux[y:]):
        x = aux[y:].index("connected")+ y -1
    else:
        x = len(aux)
    h=""
    y+=1
    while(y<x):
        v = aux[y] 
        if(v.find(",") != -1):
            h += v[:len(v) - 1]
            if(h=="to"):
                h =""
                y+=1
            else:
                mas[1].append(h)
                h=""
                y+=1
        else:
            h += aux[y]
            h+=" "
            y+=1
    while(h[len(h)-1]==" "):
        h = h[:len(h)-1]
    mas[1].append(h)
    return mas,y                
    
                
                
                
            
# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if not (network.get(user)):
        return None
    else:
        a = network.get(user)
        a= a[0]
        return a

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if not (network.get(user)):
        return None
    else:
        return network.get(user)[1]
  

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if (network.get(user_A) and network.get(user_B) ):
        a = network.get(user_A)
        if(user_B in a[0] ):
            return network
        else:
            a[0].append(user_B)
            network[user_A] = a
            return network
    else:
        return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if(network.get(user)):
        return network
    a = [[],games]
    network[user] = a
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if not (network.get(user)):
        return None
    a = network.get(user)
    a=a[0]
    if(len(a)==0):
        return []
    else:
        x = 0
        c = []
        while(x<len(a)):
            b = network.get(a[x])
            for  y in b[0]:
                if not (y in c):
                    c.append(y)
            x+=1
        a = c
        return a    

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if not (network.get(user_A) and network.get(user_B)):
        return False
    else:
        result = 0
        a = network.get(user_A)
        a = a[0]
        b = network.get(user_B)
        b = b[0]
        for x in a:
            if(x in b):
                result += 1
        return result

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def find_path_to_friend(network, user_A, user_B):
    if not(network.get(user_A) and network.get(user_B)):
        return None
    d =network.get(user_A)
    if(len(d[0])==0):
        return None
    else:
        coleccion1 = [user_A]
        coleccion2 = []
        coleccion3 = [user_A]
        h = find_path_to_friend_aux2(coleccion1,coleccion2,coleccion3,network,user_B)
        return h
def find_path_to_friend_aux2(coleccion1,coleccion2,coleccion3,network,user_B):
    if(len(coleccion1) == 0):
        return None
    else:
        c = network.get(coleccion1[len(coleccion1)-1])
        c = c[0]
        d = True
        if(len(c) == 0):
            coleccion1.pop()
        for x in c:
            if(x == user_B):
                coleccion3.append(x)
                return coleccion3
            if not(x in coleccion2):
                if not(x in coleccion1):
                    coleccion1.append(x)
                    d = False
        if(d):
            if(len(coleccion1) == 0):
                return None
            d = coleccion3.pop()
            print d
            coleccion1.pop()
        coleccion2 += c
        if(len (coleccion1) == 0):
            return find_path_to_friend_aux2(coleccion1,coleccion2,coleccion3,network,user_B)
        j = coleccion1[len(coleccion1)-1]
        if not(j in coleccion3):
                coleccion3.append(j)
        return find_path_to_friend_aux2(coleccion1,coleccion2,coleccion3,network,user_B)

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

#net = create_data_structure(example_input)
#net = create_data_structure("")
#print net
net = create_data_structure(example_input)
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Merkcedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#add_new_user(net, "Alice", [])
#add_new_user(net, "Bob", ["The Movie: the Game"])
#add_new_user(net, "Carol", [])
#add_connection(net, "Alice", "Bob")
#print get_connections(net, "Alice")
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "John")
#print count_common_connections(net, "John", "Mercedes")
print find_path_to_friend(net, "John", "Jennie")
