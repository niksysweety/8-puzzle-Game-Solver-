## code starts here for BFS search#######

## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1)) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1)) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1)) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.

# defining the bfs function
def bfs(initial,goal):
       queue = []
       queue.append(generate_node(initial,None,0,0)) # generating the initial node and putting in queue
       dictionary = {}  # creating a hash table (dictionary) to keep track of the visited nodes
       dictionary [tuple(initial)] = 'gray'  # nodes visited  will be marked gray.
       count = 1
       visitedcount = 0  # counting the number of visited nodes
       nodelistlength = 0
      # print (" States Visit Order:")
       while True:
          u = queue.pop(0) # popping the first element from the queue
          visitedcount = visitedcount+1
          if (len(queue) > nodelistlength):
              nodelistlength = len(queue)
       #   print ("\n", end = "")
       #   for i in range(9):             # prinitng the state of the node being tested for goal node. Stopped printing as it was increasing the o/p file size
        #    if (i%3==0):                 # It will cause a delay in run as well. It be uncommented to find the nodes which are visited.
         #       print ("\n", end =""),
          #  print (u.state[i], end = "  ")         
          if u.state == goal:                   # testing for goal node
              path_moves = path_finder(u,initial)   # if found, search the path
              return (path_moves,count,u.depth,visitedcount,nodelistlength)   # returning the number of moves, count of the nodes being generated
          else:  
              Possible_nodes = Possiblemoves(u)    # generating the all the possible child nodes of a given node
              for node in Possible_nodes:                    
                    if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited, then adding in the open queue 
                       count = count + 1 
                       dictionary[tuple(node.state)]= 'gray'
                       queue.append(node)   # adding the generated node in the queue

#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth):   # initializing funtion of class taking state, parent , move, depth 
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth

def generate_node (state,parent,move,depth):          # returning a node being generated
      return NODE(state,parent,move,depth)

# Main function
def main ():
     #initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     initial_state = [5,6,7,4,0,8,3,2,1] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output_moves,count,depth,visitedcount,nodelistlength] = bfs (initial_state, goal_state) # calling bfs function
     afterrun=datetime.datetime.now().time()   # time after bfs run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after bfs run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for hard Case")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print ("\n")
     print ("Time in the begining before BFS run = ", beforerun)
     print ("Time after BFS run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
     print ("The moves taken in this step : ", end = " ")
     for i in output_moves:
       print  (i , end = " ")
     print ("\n")
     print ("The number of nodes generated", count)
     print ("The number of nodes visited:", visitedcount)
     print ("The maximum length of nodelist during execution:", nodelistlength)
     print ("The depth from initial state at which goal state is found:", depth) 
 



if __name__ == '__main__':
   main()
## BFS search code ends--------------------------------------------------------------------
######### DFS search code starts#######################
## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1)) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1)) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1)) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.

# defining the bfs function
def dfs(initial,goal):
       queue = []
       queue.append(generate_node(initial,None,0,0)) # generating the initial node and putting in queue
       dictionary = {}  # creating a hash table (dictionary) to keep track of the visited nodes
       dictionary [tuple(initial)] = 'gray'  # nodes visited  will be marked gray.
       count = 1
       visitedcount = 0
       nodelistlength = 0
      # print (" States Visit Order:")
       while True:
          u = queue.pop(0) # popping the first element from the queue
          visitedcount = visitedcount+1
          if (len(queue) > nodelistlength):
              nodelistlength = len(queue)
       #   print ("\n", end = "")
       #   for i in range(9):             # prinitng the state of the node being tested for goal node. Stopped printing as it was increasing the o/p file size
        #    if (i%3==0):                 # It will cause a delay in run as well. It be uncommented to find the nodes which are visited.
         #       print ("\n", end =""),
          #  print (u.state[i], end = "  ")         
          if u.state == goal:                   # testing for goal node
              path_moves = path_finder(u,initial)   # if found, search the path
              return (path_moves,count,u.depth,visitedcount,nodelistlength)   # returning the number of moves, count of the nodes being generated
          else:  
              Possible_nodes = Possiblemoves(u)    # generating the all the possible child nodes of a given node
              NonVisited_nodes=[]
              for node in Possible_nodes:                    
                    if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited, then adding in the open queue 
                       count = count + 1 
                       dictionary[tuple(node.state)]= 'gray'
                       NonVisited_nodes.append(node) # Adding the generated nodes in the nonvisited queue
              NonVisited_nodes.extend(queue) #implememting a stack out of queue.
              queue=NonVisited_nodes          # assigning back to queue 

#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth):   # initializing funtion of class taking state, parent , move, depth 
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth

def generate_node (state,parent,move,depth):          # returning a node being generated
      return NODE(state,parent,move,depth)

# Main function
def main ():
     #initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     initial_state = [5,6,7,4,0,8,3,2,1] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output_moves,count,depth,visitedcount,nodelistlength] = dfs (initial_state, goal_state) # calling dfs function
     afterrun=datetime.datetime.now().time()   # time after dfs run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after bfs run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for hard case")
     print ("Input state")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print ("\n")
     print ("Time in the begining before DFS run = ", beforerun)
     print ("Time after DFS run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
    # print ("The moves taken in this step : ", end = " ")
     #for i in output_moves:
    # print  (i , end = " ")
     print ("\n")
     print ("The number of states generated ", count)
     print ("The number of nodes visited:", visitedcount)
     print ("The maximum length of nodelist during execution:", nodelistlength)
     print ("The depth from initial state at which goal state is found:", depth) 
 



if __name__ == '__main__':
   main()

########DFS code ends _____----------------------------------------###
### IDS code starts here
## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1)) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1)) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1)) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.

# defining the bfs function
def ids(initial,goal,depth_limit):
       queue = []
       queue.append(generate_node(initial,None,0,0)) # generating the initial node and putting in queue
       dictionary = {}  # creating a hash table (dictionary) to keep track of the visited nodes
       dictionary [tuple(initial)] = 'gray'  # nodes visited  will be marked gray.
       count = 1
       visitedcount = 0
       nodelistlength = 0
      # print (" States Visit Order:")
       while len(queue)!=0: # search until the queue becomes empty
          u = queue.pop(0) # popping the first element from the queue
          visitedcount = visitedcount + 1
          if (len(queue) > nodelistlength):
              nodelistlength = len(queue)
       #   print ("\n", end = "")
       #   for i in range(9):             # prinitng the state of the node being tested for goal node. Stopped printing as it was increasing the o/p file size
        #    if (i%3==0):                 # It will cause a delay in run as well. It be uncommented to find the nodes which are visited.
         #       print ("\n", end =""),
          #  print (u.state[i], end = "  ")         
          if u.state == goal:                   # testing for goal node
              path_moves = path_finder(u,initial)   # if found, search the path
              return (path_moves,"True",count,visitedcount,nodelistlength)   # returning the number of moves, count of the nodes being generated
          else:
            if u.depth < depth_limit:
              Possible_nodes = Possiblemoves(u)    # generating the all the possible child nodes of a given node
              NonVisited_nodes=[]
              for node in Possible_nodes:                    
                    if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited, then adding in the open queue 
                       count = count + 1 
                       dictionary[tuple(node.state)]= 'gray' # tuple is used to create an immutable type as dictionary requires an immutable type for its key.
                       NonVisited_nodes.append(node) # Adding the generated nodes in the nonvisited queue
              NonVisited_nodes.extend(queue) #implememting a stack out of queue.
              queue=NonVisited_nodes          # assigning back to queue 
       return (0,"False",count,visitedcount,nodelistlength)  # return the false status if 
#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth):   # initializing funtion of class taking state, parent , move, depth 
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth

def generate_node (state,parent,move,depth):          # returning a node being generated
      return NODE(state,parent,move,depth)

# Main function
def main ():
     depth_max_limit = 50;   # defining maximum depth limit of 50.
     #initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     initial_state = [5,6,7,4,0,8,3,2,1] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     print ("Running for Hard case")
     print ("Input State")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     depth = 1
     status = "False"
     CountVisited = 0
     while depth!= depth_max_limit+1:   # running depth function till depth limit or if the goal state is found earlier
      [output_moves,status,count,visitedcount,nodelistlength]= ids (initial_state, goal_state,depth)
      CountVisited = CountVisited + visitedcount
      print ("\n")
      if status=="False":
         print ( "Number of %d nodes generated in ids search with depth = %d" % (count,depth))
         depth= depth+1
      else:
         status = "True"
         break
     if status == 'True':      ## check if the status is true i.e ids was able to search the goal node within max depth limit
      afterrun=datetime.datetime.now().time()   # time after ids run
      timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after ids run
      timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
      print ("\n")
      print ("Time in the begining before IDS run = ", beforerun)
      print ("Time after IDS run got completed = ", datetime.datetime.now().time()) 
      timedelta= timeafterrun-timebeforerun 
      print("Time in seconds taken for run =", timedelta/1000000)
      print ("The moves taken in this step : ", end = " ")
      for i in output_moves:
        print  (i , end = " ")
      print ("\n")
      print ("The number of states generated in the last IDS search", count)
      print ("The number of nodes visited:", CountVisited)
      print ("The maximum length of nodelist during execution:", nodelistlength)
      print ("The depth from initial state at which goal state is found:", depth) 
     else:
        print ("we are not able to find the node. We are so sorry.")



if __name__ == '__main__':
   main()
#########IDS code ends here -------------------------------------------------------------################
#### greddy code starts here#############
## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1)) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1)) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1)) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.

# defining the greedy function
def greedy(initial,goal,heuristic):
       queue = []
       queue.append(generate_node(initial,None,0,0)) # generating the initial node and putting in queue
       dictionary = {}  # creating a hash table (dictionary) to keep track of the visited nodes
       dictionary [tuple(initial)] = 'gray'  # nodes visited  will be marked gray.
       count = 1
       visitedcount = 0
       nodelistlength =0 
      # print (" States Visit Order:")
       while True:
          queue = sorted(queue, key=heuristic) # sorting the queue based on the heuristic value
          u = queue.pop(0) # popping the first element from the queue
          visitedcount = visitedcount+1
          if (len(queue) > nodelistlength):
              nodelistlength = len(queue)
       #   print ("\n", end = "")
       #   for i in range(9):             # prinitng the state of the node being tested for goal node. Stopped printing as it was increasing the o/p file size
        #    if (i%3==0):                 # It will cause a delay in run as well. It be uncommented to find the nodes which are visited.
         #       print ("\n", end =""),
          #  print (u.state[i], end = "  ")         
          if u.state == goal:                   # testing for goal node
              path_moves = path_finder(u,initial)   # if found, search the path
              return (path_moves,count,u.depth,visitedcount,nodelistlength)   # returning the number of moves, count of the nodes being generated
          else:  
              Possible_nodes = Possiblemoves(u)    # generating the all the possible child nodes of a given node
              for node in Possible_nodes:                    
                    if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited, then adding in the open queue 
                          count = count + 1 
                          dictionary[tuple(node.state)]= 'gray'
                          queue.append(node)   # adding the generated node in the queue

#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth):   # initializing funtion of class taking state, parent , move, depth 
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth

def generate_node (state,parent,move,depth):          # returning a node being generated
      return NODE(state,parent,move,depth)
    
# heuristic function based on number of tiles out of place
def heuristic1(node):
    goal = [1,2,3,8,0,4,7,6,5]
    count = 0
    for i in range(9):
        if (node.state[i]!=goal[i]):
            count= count+1
    return (count)

# heuristic function based on the manhattan distance
def heuristic2(node):
    goal = [1,2,3,8,0,4,7,6,5]
    h = 0
    for i in range(3):
         for j in range(3):
             k=(i*3)+j
             p = node.state.index(goal[k])
             h+= abs(i-p//3) + abs(j-p%3)
    return h

# Main function
def main ():
     #initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     initial_state = [5,6,7,4,0,8,3,2,1] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output_moves,count,depth,visitedcount,nodelistlength] = greedy(initial_state, goal_state,heuristic1) # calling function
     afterrun=datetime.datetime.now().time()   # time after  run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after  run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for  case with heursitic based on number of tiles out of place")
     print ("Printing the input state")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print("\n")
     print ("Time in the begining before greedy run = ", beforerun)
     print ("Time after greedy run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
     print ("The moves taken in this step : ", end = " ")
     for i in output_moves:
       print  (i , end = " ")
     print ("\n")
     print ("The number of states generated :", count)
     print ("The number of nodes visited:", visitedcount)
     print ("The maximum length of nodelist during execution:", nodelistlength)
     print ("The depth from initial state at which goal state is found:", depth)
 



if __name__ == '__main__':
   main()
######### ---------greedy code ends here ------------###########
########### ASTAR code starts here-------------------###########
## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node,heuristic):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1,astarfunction(node.depth+1,moveup(node.state),heuristic))) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1,astarfunction(node.depth+1,movedown(node.state),heuristic)))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1,astarfunction(node.depth+1,moveleft(node.state),heuristic))) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1,astarfunction(node.depth+1,moveright(node.state),heuristic))) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.

# defining the astar function
def astar(initial,goal,heuristic):
       queue = []
       queue.append(generate_node(initial,None,0,0,astarfunction(0,initial,heuristic))) # generating the initial node and putting in queue
       dictionary = {}  # creating a hash table (dictionary) to keep track of the visited nodes
       dictionary [tuple(initial)] = 'gray'  # nodes visited  will be marked gray.
       count = 1
       visitedcount = 0
       nodelistlength =0 
      # print (" States Visit Order:")
       while True:
          queue = sorted(queue, key=fvaluecompare) # sorting the queue based on the heuristic+ depth value
          u = queue.pop(0) # popping the first element from the queue
          visitedcount = visitedcount+1
          if (len(queue) > nodelistlength):
              nodelistlength = len(queue)
       #   print ("\n", end = "")
       #   for i in range(9):             # prinitng the state of the node being tested for goal node. Stopped printing as it was increasing the o/p file size
        #    if (i%3==0):                 # It will cause a delay in run as well. It be uncommented to find the nodes which are visited.
         #       print ("\n", end =""),
          #  print (u.state[i], end = "  ")         
          if u.state == goal:                   # testing for goal node
              path_moves = path_finder(u,initial)   # if found, search the path
              return (path_moves,count,u.depth,visitedcount,nodelistlength)   # returning the number of moves, count of the nodes being generated
          else:  
              Possible_nodes = Possiblemoves(u,heuristic)    # generating the all the possible child nodes of a given node
              for node in Possible_nodes:                    
                    if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited, then adding in the open queue 
                          count = count + 1
                          if node.fvalue<u.fvalue:
                              node.update_fvalue(u.fvalue)
                          dictionary[tuple(node.state)]= 'gray'
                          queue.append(node)   # adding the generated node in the queue

#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth,fvalue):   # initializing funtion of class taking state, parent , move, depth 
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth
          self.fvalue = fvalue
      def update_fvalue(self,fvalue):  # function used to update the fvalue of the node
          self.fvalue = fvalue
          
def fvaluecompare(node):    # function returning the fvalue of the node
        return node.fvalue
def generate_node (state,parent,move,depth,fvalue):          # returning a node being generated
      return NODE(state,parent,move,depth,fvalue)

def astarfunction (depth,state,heuristic): 
     return (depth + heuristic(state))
    
# heuristic function based on number of tiles out of place
def heuristic1(state):
    goal = [1,2,3,8,0,4,7,6,5]
    count = 0
    for i in range(9):
        if (state[i]!=goal[i]):
            count= count+1
    return (count)

# heuristic function based on the manhattan distance
def heuristic2(state):
    goal = [1,2,3,8,0,4,7,6,5]
    h = 0
    for i in range(3):
         for j in range(3):
             k=(i*3)+j
             p = state.index(goal[k])
             h+= abs(i-p//3) + abs(j-p%3)
    return h

# Main function
def main ():

     initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     #initial_state = [5,6,7,4,0,8,1,2,3] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output_moves,count,depth,visitedcount,nodelistlength] = astar(initial_state, goal_state,heuristic2) # calling function
     afterrun=datetime.datetime.now().time()   # time after  run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after  run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for hard case with heursitic based on manhattan distance")
     print ("Running for the input state")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print ("\n")
     print ("Time in the begining before run = ", beforerun)
     print ("Time after run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
     print ("The moves taken in this step : ", end = " ")
     print ("The number of states generated:", count)
     print ("The number of nodes visited:", visitedcount)
     print ("The maximum length of nodelist during execution:", nodelistlength)
     print ("The depth from initial state at which goal state is found:", depth) 
 

if __name__ == '__main__':
   main()
##### Astar code ends here ------------------------###################
##### Idastar code starts here-------------------------#########################
## importing the system module in case we want to provide any command line arguement
import sys
## importing datetime module for printing time
import datetime

##------------moveup function definition with input as node state
def moveup(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-3] # In the move up function, since element at the index of 0 in the new state will replace the element at 3 position lower in initial state, 
    next_state[place-3]=0 # Since 0 will move up, so it will occupy the initial_index - 3 position.
    return next_state  # Returning the next state generated 
    
##----------- movedown function definition
def movedown(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place+3] # In the move down function, since element at the index of 0 in the new state will replace the element at 3 position higher in initial state,
    next_state[place+3]=0 # Since 0 will move down, so it will occupy the initial_index + 3 position.
    return next_state  # Returning the next state generated 
 
##------------ moveleft function definition
def moveleft(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place] = next_state[place-1] # In the move left function, since element at the index of 0 in the new state will replace the element at 1 position lower in initial state,
    next_state[place-1]=0 # Since 0 will move left, so it will occupy the initial_index - 1 position.
    return next_state  # Returning the next state generated 
 
##------------ moveright function definition
def moveright(state):
    next_state = state[:]  # creating a copy of next state 
    place=next_state.index(0) # finding the postition of 0 in the next state
    next_state[place]= next_state[place+1] # In the move up function, since element at the index of 0 in the new state will replace the element at 1 position higher in initial state,
    next_state[place+1]=0 # Since 0 will move right, so it will occupy the initial_index + 1 position.
    return next_state  # Returning the next state generated 


# creating possible moves function which will generate the child nodes for all possible moves of a given parent node.
def Possiblemoves(node):
    expanded_nodes = []  # a queue to hold the child nodes being generated.
    place= node.state.index(0) # finding the index of 0 in the parent node state
    if place not in [0,1,2]: # to check whether the up move is possible 
        expanded_nodes.append(generate_node(moveup(node.state),node , "up", node.depth +1)) # appending the node generated due to move up position and calling generate_node 
# to return the node being generated
    if place not in [6,7,8]: # to check whether the down move is possible 
         expanded_nodes.append(generate_node(movedown(node.state),node , "down", node.depth +1 ))  # appending the node generated due to move down position
    if place not in [0,3,6]: # to check whether the left move is possible 
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left", node.depth +1)) # appending the node generated due to move left position 
    if place not in [2,5,8]: # to check whether the right move is possible 
        expanded_nodes.append(generate_node(moveright(node.state),node , "right", node.depth +1)) # appending the node generated due to move right position 
    return expanded_nodes # returning the expanded nodes queue

#  defining a path finder function.
def path_finder(node,initial): # passing the node at which goal state is found.
    moves = []  # defining an empty moves queue.
    var = node   # initializing the variable var with goal node 
    while var.state != initial:  # will keep on running until the initial state is found
          moves.insert(0,var.move) # will insert the node move in the begining so as to traverse the path from begining to end
          var = var.parent # assigning node's parent to the variable var
    return moves # returning the moves queue with all the moves taken to reach goal node from initial state.


def idastar(initial,heuristic):
   goal = [1,2,3,8,0,4,7,6,5]
   queue = []
   count = 0
   queue.append(generate_node(initial,None,0,0))  # generating the initial node and putting in queue
   node = queue.pop(0) # popping out the node from the queue
   limitvalue = heuristic(node) # setting the initial limitvalue to heuristic of root node
   while True:
     dictionary = {}
     [result,status,depth,moves,nodevisitedcount] = depthfirstsearch(node,limitvalue,dictionary,initial,heuristic,count) # perform the depth first search
     count = nodevisitedcount
     if status=="TRUE":         # if the status is true, it means goal node has been found, return the moves.
         return (moves,count,depth)
     limitvalue= result         # set the new limit value 

def depthfirstsearch(node,limitvalue,dictionary,initial,heuristic,count):
   goal = [1,2,3,8,0,4,7,6,5]
   fvalue = node.depth + heuristic(node)
   count = count+1
   if fvalue > limitvalue:    # comparison of the fvalue of child node with g + h value, if it greater then return the fvalue
       return (fvalue,"FALSE",node.depth,"NULL",count)
   if node.state == goal:       # if the goal node has been found
        path_moves = path_finder(node,initial)
        return (1,"TRUE",node.depth,path_moves,count)
   MINVALUE = float("inf")
   Possible_nodes = Possiblemoves(node) # generate all the possible moves
   for node in Possible_nodes:
        if tuple(node.state) not in dictionary:   # checking in the dictionary if the node is not visited 
            dictionary[tuple(node.state)]= 'gray'
            [result,status,depth,moves,count]=depthfirstsearch(node,limitvalue,dictionary,initial,heuristic,count) # again run the dfs search for the successor nodes
            if status=="TRUE":      # goal node has been found
                return (1,"TRUE",depth,moves,count)
            elif result < MINVALUE :   # Find out the min fvalue of all the successor nodes.
               MINVALUE = result
   #if(count==len(Possible_nodes)): # if there is no unvisited children left for node 
   return (MINVALUE,"FALSE",MINVALUE,"NULL",count)
   #else:   # if there is atleast one child present for the given node
    #     return (MINVALUE,"FALSE",depth,moves)

#Defining a class node
class NODE:
      def __init__(self,state,parent,move,depth):   # initializing funtion of class taking state, parent , move, depth, fvalue
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth
  
def generate_node (state,parent,move,depth):          # returning a node being generated
      return NODE(state,parent,move,depth)

#def idastarfunction (depth,state,heuristic):  # astar function returning the fvalue for a given state
 #    return (depth + heuristic(state))
    
    
# heuristic function based on number of tiles out of place
def heuristic1(node):
    goal = [1,2,3,8,0,4,7,6,5]
    count = 0
    for i in range(9):
        if (node.state[i]!=goal[i]):
            count= count+1
    return (count)

# heuristic function based on the manhattan distance
def heuristic(node):
    goal = [1,2,3,8,0,4,7,6,5]
    h = 0
    for i in range(3):
         for j in range(3):
             k=(i*3)+j
             p = node.state.index(goal[k])
             h+= abs(i-p//3) + abs(j-p%3)
    return h

# Main function
def main ():
     #initial_state = [1,3,4,8,6,2,7,0,5]  # initial states easy
     #initial_state = [2,8,1,0,4,3,7,6,5]  # medium initial state
     #initial_state = [5,6,7,4,0,8,1,2,3] # hard initial state
     goal_state = [1,2,3,8,0,4,7,6,5]     # goal state
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output_moves,count,depth] = idastar(initial_state,heuristic1) # calling function
     afterrun=datetime.datetime.now().time()   # time after  run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after  run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for medium case with heursitic based on number of tiles out of place")
     print ("Printing the input state")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print ("\n")
     print ("Time in the begining before run = ", beforerun)
     print ("Time after run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
     print ("The moves taken in this step : ", end = " ")
     for i in output_moves:
       print  (i , end = " ")
     print ("\n")
     print ("\n")
     print ("The number of nodes visited", count)
     print ("The maximum depth of recursion:", depth) 
     for i in output_moves:
       print  (i , end = " ")
     print ("\n")



if __name__ == '__main__':
   main()
### astar code ends here ----------------------#######
###my system was hanging for hard case of IDA*. So made some changes for IDA* to get output---- code for hard case
import sys
import datetime

def moveup(state):
    next_state = state[:]
    place=next_state.index(0)
    next_state[place] = next_state[place-3]
    next_state[place-3]=0
    return next_state
    

def movedown(state):
    next_state = state[:]
    place=next_state.index(0)
    next_state[place] = next_state[place+3]
    next_state[place+3]=0
    return next_state
 

def moveleft(state):
    next_state = state[:]
    place=next_state.index(0)
    next_state[place] = next_state[place-1]
    next_state[place-1]=0
    return next_state
 

def moveright(state):
    next_state = state[:]
    place=next_state.index(0)
    next_state[place]= next_state[place+1]
    next_state[place+1]=0
    return next_state

def Possiblemoves(node):
    expanded_nodes = []
    place= node.state.index(0)
    if place not in [0,1,2]:
        expanded_nodes.append(generate_node(moveup(node.state),node , "up",node.depth+1))
    if place not in [6,7,8]:
         expanded_nodes.append(generate_node(movedown(node.state),node , "down",node.depth+1))
    if place not in [0,3,6]:
         expanded_nodes.append(generate_node(moveleft(node.state),node , "left",node.depth+1))
    if place not in [2,5,8]:
        expanded_nodes.append(generate_node(moveright(node.state),node , "right",node.depth+1))
    return expanded_nodes


def path_finder(node,initial):
   # initial = [5,6,7,4,0,8,3,2,1]
    moves = []
    var = node
    while var.state != initial:
          moves.insert(0,var.move)
          var = var.parent
    return moves

def idastar(initial):
   queue = []
   queue.append(generate_node(initial,None,0,0))
   node = queue.pop(0)
   limitvalue = heuristic1(node)
   while True:
     dictionary = {}
     [result,depth,moves] = depthfirstsearch(node,limitvalue,dictionary,initial)
     if result==1:
         return ("TRUE",depth,moves)
     limitvalue= result
 
 
def depthfirstsearch(node,limitvalue,dictionary,initial):
   goal = [1,2,3,8,0,4,7,6,5]
   fvalue = node.depth + heuristic1(node)
   if fvalue > limitvalue:
       return (fvalue, node.depth,"NULL")
   if node.state == goal:
       path_moves = path_finder(node,initial)
       return (1,node.depth,path_moves)
   MINVALUE = float("inf")
   Possible_nodes = Possiblemoves(node)
   count = 0
   for node in Possible_nodes:
        if tuple(node.state) not in dictionary:
            dictionary[tuple(node.state)]= 'gray'
            [result,depth,moves]=depthfirstsearch(node,limitvalue,dictionary,initial)
            if result==1:
                return (1,depth,moves)
            elif result < MINVALUE :
               MINVALUE = result
        else:
            count = count+1
   if(count==len(Possible_nodes)):
       return (MINVALUE,MINVALUE,"NULL")
   else:
       return (MINVALUE,depth,moves)

class NODE:
      def __init__(self,state,parent,move,depth):
          self.state = state
          self.parent = parent
          self.move = move
          self.depth = depth

def generate_node (state,parent,move,depth):
      return NODE(state,parent,move,depth)

def astarfunction (node):
     return (node.depth + heuristic2(node))


# heuristic function based on number of tiles out of place
def heuristic1(node):
    goal = [1,2,3,8,0,4,7,6,5]
    count = 0
    for i in range(9):
        if (node.state[i]!=goal[i]):
            count= count+1
    return (count)


def heuristic2(node):
    goal = [1,2,3,8,0,4,7,6,5]
    h = 0
    for i in range(3):
         for j in range(3):
             k=(i*3)+j
             p = node.state.index(goal[k])
             h+= abs(i-p//3) + abs(j-p%3)
    return h
              

  
    
def main ():
     initial_state = [5,6,7,4,0,8,3,2,1]
     goal_state = [1,2,3,8,0,4,7,6,5]
     
     beforerun = datetime.datetime.now().time()   # time before run
     timebeforerun1= beforerun.hour*3600 + beforerun.minute*60+ beforerun.second  # time in seconds
     timebeforerun = timebeforerun1*1000000 + beforerun.microsecond # time in microseconds 
     [output,depth,moves]= idastar(initial_state) # calling function
     afterrun=datetime.datetime.now().time()   # time after  run
     timeafterrun1 = afterrun.hour*3600 + afterrun.minute*60+ afterrun.second  # time in seconds after  run
     timeafterrun = timeafterrun1*1000000 + afterrun.microsecond
     print ("\n")
     print ("Running for medium case with heursitic based on number of tiles out of place")
     print ("Printing the input state")
     for i in range(9):            
         if (i%3==0):                 
            print ("\n", end =""),
         print (initial_state[i], end = "  ")
     print ("\n")
     print ("Time in the begining before run = ", beforerun)
     print ("Time after run got completed = ", datetime.datetime.now().time()) 
     timedelta= timeafterrun-timebeforerun 
     print("Time in seconds taken for run =", timedelta/1000000)
     print("\n")
     for m in moves:
           print  (m, end = "")
     print ("\n")
     print ("depth = %d" %depth,' ')
     print (output)
if __name__ == '__main__':
   main()
###### all the code ends here----------------------###########
