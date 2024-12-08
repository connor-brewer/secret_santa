
# This was for my Secret Santa 2024 I had with my friends
# It just takes in a list of names and randomly assigns a secret santa recipient for each player
# Multiple cycles are possible
# However no self-cycles are possible (i.e. you can't give yourself a present)


import numpy as np
import random as rand
import os
# from IPython.display import clear_output



def clear_console():
    """Clears the console."""
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)





print("Ex.) \"Connor JohnLennon, michael Steve2\"")
print("Enter the list of names:")
list_names = input()
list_names = list_names.replace(",", "")
list_names = list_names.replace("\"", "")
list_names = list_names.split(" ")

# print("(The default value is \"MANY\")")
# print("Enter \"ONE\" for one cycle or \"MANY\" for many cycles:")
# inpval = input()
# one_mode = False
# if inpval == "ONE" or inpval == "one":
#     one_mode = True





if "#" in list_names:
    list_names.remove("#")  # this is just to easily copy paste examples from the top
temp = []
for name in list_names:
    if name.strip():
        temp.append(name)
list_names = temp
list_names = list(set(list_names))
list_names.sort()
print("List:", list_names)

print("Reveal Info? Y/N")
print("Enter Your Choice:")
inpyval = input()
inpyval = inpyval.lower()
reveal_info = False
if inpyval == "yes" or inpyval == "y":
    reveal_info = True
    


clear_console()
# clear_output()



receiver_dict = {}  #input a name, it will tell you who they are giving a gift to, the receiver
giver_dict = {}  #input a name, it will tell you who they are receiving a gift from, the giver


def cycle_length(name):
    global receiver_dict
#     global giver_dict      #don't really need it here
    length = 0
    curr_name = name
    start_of_cycle = name
    while(True):
        if curr_name in receiver_dict:
            curr_name = receiver_dict[curr_name]
            length += 1
            if curr_name == start_of_cycle:
                break
        else:
            break
    return length


def are_connected(name1, name2):
    global receiver_dict
#     global giver_dict      #don't really need it here
    curr_name = name1
    start_of_cycle = name1
    while(True):
        if curr_name in receiver_dict:
            if curr_name == name2:
                return True
            curr_name = receiver_dict[curr_name]
            if curr_name == start_of_cycle:
                break
        else:
            break
    return False

list_of_pot_givers = list(np.arange(len(list_names)))
list_of_pot_receivers = list(np.arange(len(list_names)))

# if one_mode == True
for i in range(len(list_names)):
    name = list_names[i]
    

    
    
    if (len(list_of_pot_givers) == 2): # if there are two potential people have not yet given
        mema = list_names[list_of_pot_givers[0]]
        memb = list_names[list_of_pot_givers[1]]
    
        
        
        if (not list_of_pot_givers[0] in list_of_pot_receivers) and (list_of_pot_givers[1] in list_of_pot_receivers): #mema is not pot rec   memb is pot rec
            # mema gives to memb
            receiver_dict[mema] = memb
            giver_dict[memb] = mema
            list_of_pot_receivers.remove(list_of_pot_givers[1])    # remove(memb) 
            list_of_pot_givers.remove(list_of_pot_givers[0])       # remove(mema)
            
            # now memb will give to pot_receiver
            final_rec = list_names[list_of_pot_receivers[0]]
            receiver_dict[memb] = final_rec
            giver_dict[final_rec] = memb
            list_of_pot_receivers.clear()    # remove(final_rec) 
            list_of_pot_givers.clear()       # remove(memb)
            break

        elif (not list_of_pot_givers[1] in list_of_pot_receivers) and (list_of_pot_givers[0] in list_of_pot_receivers):
            # memb gives to mema
            receiver_dict[memb] = mema
            giver_dict[mema] = memb
            list_of_pot_receivers.remove(list_of_pot_givers[0])    # remove(mema) 
            list_of_pot_givers.remove(list_of_pot_givers[1])       # remove(memb)
            
            # now mema will give to pot_receiver
            final_rec = list_names[list_of_pot_receivers[0]]
            receiver_dict[mema] = final_rec
            giver_dict[final_rec] = mema
            list_of_pot_receivers.clear()    # remove(final_rec) 
            list_of_pot_givers.clear()       # remove(mema)
            break
            
        elif (list_of_pot_givers[1] in list_of_pot_receivers) and (list_of_pot_givers[0] in list_of_pot_receivers):
            # they cycle together   they give to each other
            # mema gives to memb
            receiver_dict[mema] = memb
            giver_dict[memb] = mema
            # then memb gives to mema
            receiver_dict[memb] = mema
            giver_dict[mema] = memb
            list_of_pot_receivers.clear()    # remove(mema and memb) 
            list_of_pot_givers.clear()       # remove(memb and mema)
            break
        #else, do nothing, we're good to keep going
            
    
    idx = rand.choice(list_of_pot_receivers)

    if (idx == i) and not (len(list_of_pot_receivers) == 1):
            templist = list_of_pot_receivers.copy()
            templist.remove(idx)
            idx = rand.choice(templist)


    receiver = list_names[idx]
    list_of_pot_receivers.remove(idx)
    list_of_pot_givers.remove(i)

    receiver_dict[name] = receiver
    giver_dict[receiver] = name      #reciever is receiving a gift from name
    



    
# a class representing a member of secret santa game
class Member:         
    def __init__(self, name, receiver, giver):     #    receiver: who is receiving name's gift      giver: who is giving name their gift    
        self.name = name
        self.receiver = receiver
        self.giver = giver
# m = Member("Connor", "ReceiverName", "GiverName")

members = []
for name in list_names:
    receiver_name = receiver_dict[name]
    giver_name = giver_dict[name]
    m = Member(name, receiver_name, giver_name)
    members.append(m)

    
def secret_santa(name): #takes in a name and gives them their secret santa
    if not name in receiver_dict:
#         print("Error: Invalid Name")
        return None
    return receiver_dict[name]
    
    
def list_cycles(rect_dict):
    next_name = ""
    non_visited_keys = list(rect_dict.keys())
    list_of_cycles = [[]]
    while (non_visited_keys):
        idv_list = []
        start_name = non_visited_keys[0]
        curr_name = start_name
        while (True):
            idv_list.append(curr_name)
            non_visited_keys.remove(curr_name)
            next_name = rect_dict[curr_name]
            curr_name = next_name
            if curr_name == start_name:
                break
        list_of_cycles.append(idv_list)
    del list_of_cycles[0]
    return list_of_cycles    
    
    
def print_info():
    print("")
    print("Members:")
    for m in members:
        print("")
        print("Member Name:", m.name)
        print("     ", m.name, "is giving a gift to", m.receiver)
        print("     ", m.name, "is receiving a gift from", m.giver)




    print("")
    print("")
    print("")
    vall = list_cycles(receiver_dict)
    for element in vall:
        for h in range(len(element)):
            print(element[h], end=" -> ")
        print(element[0])
    print("")
    print("")



    print("")
    print("Members (just gifter information):")
    for m in members:
        print("")
        print("Member Name:", m.name)
        print("     ", m.name, "will give a gift to", m.receiver)
    print("")
    print("")
    print("")
    print("")
    print("")
    return
    
   
    
if reveal_info:
    print_info()




while (True):
    print("Input name to receive your Secret Santa (Case Sensitive, EXIT to exit, INFO for info)")
    print("List of Names:", list_names)
    print("Enter Name:")
    valuee = input()
    clear_console()
    # clear_output()
    valuee = valuee.replace(" ", "")
    bunger = secret_santa(valuee)
    print("")
    if (valuee.lower() == "exit" or valuee.lower() == "clear" or valuee == ""):
        break
    elif (valuee.lower() == "info"):
        print_info()
    elif bunger == None:
        print("Error: Invalid Name")
        print("")
    else:
        print("Your Secret Santa is", bunger)
        print("")
   


# Shaggy Velma Fred Scooby Daphne
# JohnLennon, GeorgeHarrison, RingoStarr, PaulMcCartney
# Albert Brendan Connor Diana Ebenezer Frank George Harold Ivan James Katie Linda Mary Nathan Owen Pedro Quincy Randy Steve Terrance Ulysses Vivian Willow Xavier Yusuf Zachary
