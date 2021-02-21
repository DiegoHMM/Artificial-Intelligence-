from definitions import Agent
from scipy.spatial import distance
import collections
import numpy as np

class RandAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors: 
            # Select random neighbor
            visit = viable_neighbors[np.random.randint(0,len(viable_neighbors))]
            
            # Append neighbor to the path and add it to the frontier
            self.frontier = [path + [visit]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])




class DFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop() #retirei o caminho da fronteira 
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)
            
        viable_neighbors =  self.percepts['neighbors']
        # Add visited node 

        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        #viable_neighbors =  self.percepts['neighbors']
        if viable_neighbors:
            # If the agent is not stuck
            for neighbor in viable_neighbors:
                insertFrontier = True
                for aux in self.visited:
                    if (neighbor == aux).all():
                        insertFrontier = False
                if insertFrontier == True:
                    self.frontier = [path + [neighbor]] + self.frontier#adiciona novos caminhos na fronteira


    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])


class BBAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env,bound=100):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        self.cost = [0]
        self.bound = bound
        self.best_path = []
        
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        cost = self.cost.pop(0)
        

        #heuristica
        if cost + distance.euclidean(path[-1],self.percepts['target']) <self.bound:
            # Visit the last node in the path
            action = {'visit_position': path[-1], 'path': path} 
            # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
            self.percepts = self.env.signal(action)

            # Add visited node 
            self.visited.append(path[-1])


            if (self.percepts['current_position'] == self.percepts['target']).all():
                self.best_path = path
                self.bound = cost 

            # From the list of viable neighbors given by the environment
            # Select a random neighbor that has not been visited yet
            
            viable_neighbors =  self.percepts['neighbors']

            # If the agent is not stuck
            if viable_neighbors: 
                for n in viable_neighbors:
                    # Append neighbor to the path and add it to the frontier
                    self.frontier = [path + [n]] + self.frontier
                    self.cost = [cost + distance.euclidean(path[-1],n)] + self.cost

    def run(self):
        """Keeps the agent acting until it finds the target
        """
        

        # Run agent
        while self.frontier:
            self.act()
        print(self.percepts['current_position'])


        for i in range(1000):
            action = {'visit_position': self.best_path[-1], 'path': self.best_path} 
            # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
            self.percepts = self.env.signal(action)


class GreedyAgent(Agent):
    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        
        #heuristica
        
        for neighbor in viable_neighbors:
            insertFrontier = True
            for aux in self.visited:
                if (neighbor == aux).all():
                    insertFrontier = False
            if insertFrontier == True:
                self.frontier = [path + [neighbor]] + self.frontier#adiciona novos caminhos na fronteira

        

        if viable_neighbors: 
            menor = distance.euclidean(viable_neighbors[-1],self.percepts['target'])
            visit = viable_neighbors[-1]
            neighbor_dict = {menor : visit}

            for n in viable_neighbors:
                neighbor_dict[distance.euclidean(n,self.percepts['target'])] = n

            neighbor_dict = collections.OrderedDict(sorted(neighbor_dict.items())) #Ordena meu dict
            index_no_viavel = 0
            values = list(neighbor_dict.values()) #transforma meu dict em lista


            for aux in self.visited:
                if (values[index_no_viavel] == aux).all(): # poda de ciclo
                    if (index_no_viavel + 1) < len(values):
                        index_no_viavel = index_no_viavel + 1
                    
                else:
                    visit = values[index_no_viavel]
            
            # Append neighbor to the path and add it to the frontier
            self.frontier = [path + [visit]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])



class BFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop() #retirei o caminho da fronteira 
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)
            
        viable_neighbors =  self.percepts['neighbors']
        # Add visited node 

        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        #viable_neighbors =  self.percepts['neighbors']
        if viable_neighbors:
            # If the agent is not stuck
            for neighbor in viable_neighbors:
                insertFrontier = True
                for aux in self.visited:
                    if (neighbor == aux).all():
                        insertFrontier = False
                if insertFrontier == True:
                    self.frontier = [path + [neighbor]] + self.frontier#adiciona novos caminhos na fronteira


    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

    
class AStarAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.
        Args:
            env: A reference to an environment.
        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self, env)

        # Get initial percepts
        self.percepts = env.initial_percepts()

        # Initializes the frontier with the initial postion
        self.frontier = [[self.percepts['current_position']]]

        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)

        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path}
        self.actionFinally = {'visit_position': path[-1], 'path': path}
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet

        viable_neighbors = self.percepts['neighbors']

        if viable_neighbors:
            distances = []
            for neighbor in viable_neighbors:
                distances.append(distance.euclidean(
                    neighbor, self.percepts['target']))

            for neighbor in viable_neighbors:
                n_max = max(distances)
                n_pos = distances.index(n_max)
                if(n_max <= distance.euclidean(path[-1], self.percepts['target']) + 0.5):
                    insertFrontier = True

                    for cycle in path:
                        if(viable_neighbors[n_pos] == cycle).all():
                            insertFrontier = False
                            break

                    for aux in self.visited:
                        if (viable_neighbors[n_pos] == aux).all():
                            insertFrontier = False
                            break

                    if insertFrontier:
                        self.frontier = [
                            path + [viable_neighbors[n_pos]]] + self.frontier
                distances[n_pos] = -9999999

    def run(self):
        """Keeps the agent acting until it finds the target
        """
        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
            print(self.percepts['current_position'])
        for i in range(1000):
            self.percepts = self.env.signal(self.actionFinally)