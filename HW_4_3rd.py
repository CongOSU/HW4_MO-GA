import math
import sys
import random
import json

class Location():
    def __init__(self,xloc,yloc,service, lowTime,highTime,ID):
        self.ID = ID
        self.xloc = xloc
        self.yloc = yloc
        self.service = service
        self.lowTime = lowTime
        self.highTime = highTime

#locations and time windows global

'''
Loc0 = Location(0, 0, 2, 0, 100000000, 0)
Loc1 = Location(10, 12, 2, 2, 20, 1)
Loc2 = Location(-5, 15, 4, 2, 200, 1)
Loc3 = Location(25, -1, 5, 15, 4000, 1)
Loc4 = Location(5, 5, 3, 0, 10, 1)
Loc5 = Location(26, 4, 1, 2, 1, 1)
Loc6 = Location(-18, -9, 1, 2, 1, 1)
Loc7 = Location(10, 11, 6, 2, 1, 1)
Loc8 = Location(15, -5, 7, 2, 1, 1)
Loc9 = Location(28, 28, 2, 2, 1, 1)
Loc10 = Location(-28, 18, 1, 2, 1, 1)
'''


def initializePop():

    initialPop_1 = []
    initialPop_2 = []
    initialPop_1.append(random.sample(range(1, 11), 10))
    print(initialPop_1)
    initialPop_2.append(random.sample(range(1, 11), 10))
    print(initialPop_2)

    trucksID_1 = []
    trucksID_2 = []
    while len(trucksID_1) < 10:
        trucksID_1.append(random.randint(1,4))
    print(trucksID_1)
    while len(trucksID_2) < 10:
        trucksID_2.append(random.randint(1,4))
    print(trucksID_2)
    
    initial_1=[]
    initial_2=[]
    initial_1.append(initialPop_1)
    initial_2.append(initialPop_2)
    initial_1.append(trucksID_1)
    initial_2.append(trucksID_2)
    return initialPop_1, initialPop_2, trucksID_1, trucksID_2, initial_1, initial_2

'''
def selRoulette(individuals, k):
    s_inds = sorted(individuals, key=attrgetter("fitness"), reverse=True)
    sum_fits = sum(ind.fitness.values[0] for ind in individuals)
    chosen = []
    for i in xrange(k):
        u = random.random() * sum_fits
        sum_ = 0
        for ind in s_inds:
            sum_ += ind.fitness.values[0]
            if sum_ > u:
                chosen.append(ind)
                break
    return chosen

def ind2route(individual, instance):
    # individual is a list, instance is a objected dict
    route = []
    deportDueTime =  instance['deport']['due_time']
    # Initialize a sub-route
    subRoute = []
    elapsedTime = 0
    lastCustomerID = 0
    for customerID in individual:
        # Update elapsed time
        serviceTime = instance['customer_%d' % customerID]['service_time']
        returnTime = instance['distance_matrix'][customerID][0]
        updatedElapsedTime = elapsedTime + instance['distance_matrix'][lastCustomerID][customerID] + serviceTime + returnTime
        # Validate vehicle load and elapsed time
        if (updatedElapsedTime <= deportDueTime):
            # Add to current sub-route
            subRoute.append(customerID)
            elapsedTime = updatedElapsedTime - returnTime
        else:
            # Save current sub-route
            route.append(subRoute)
            # Initialize a new sub-route and add to it
            subRoute = [customerID]
            elapsedTime = instance['distance_matrix'][0][customerID] + serviceTime
        # Update last customer ID
        lastCustomerID = customerID
    if subRoute != []:
        # Save current sub-route before return if not empty
        route.append(subRoute)
    return route
'''

def _repeated(element, collection):
    c = 0
    for e in collection:
        if e == element:
            c += 1
    return c > 1
 
def _swap(data_a, data_b, cross_points):
    c1, c2 = cross_points
    new_a = data_a[:c1] + data_b[c1:c2] + data_a[c2:]
    new_b = data_b[:c1] + data_a[c1:c2] + data_b[c2:]
    return new_a, new_b
 
 
def _map(swapped, cross_points):
    n = len(swapped[0])
    c1, c2 = cross_points
    s1, s2 = swapped
    map_ = s1[c1:c2], s2[c1:c2]
    for i_chromosome in range(n):
        if not c1 < i_chromosome < c2:
            for i_son in range(2):
                while _repeated(swapped[i_son][i_chromosome], swapped[i_son]):
                    map_index = map_[i_son].index(swapped[i_son][i_chromosome])
                    swapped[i_son][i_chromosome] = map_[1-i_son][map_index]
    return s1, s2
 
 
def PMXcrossover(parent_a, parent_b):
    A = initializePop()
    parent_a = A[4]
    parent_b = A[5]
    n = len(parent_a)
    cross_points = sorted([random.randint(0, n) for _ in range(2)])
    swapped = _swap(parent_a, parent_b, cross_points)
    mapped = _map(swapped, cross_points)
 
    return mapped


#ind1 = random.sample(range(1,11), 10)
ind1 = [7, 6, 3, 5, 2, 1, 4, 9, 10, 8]
#ind2 = random.sample(range(1,11), 10)
ind2 = [9, 10, 6, 1, 8, 4, 3, 5, 2, 7]
new = PMXcrossover(ind1, ind2)
print(new)

'''

def mutation(individual):
    start, stop = sorted(random.sample(range(len(individual)), 2))
    individual = individual[:start] + individual[stop:start-1:-1] + individual[stop+1:]
    return individual,

def createPop():

def evaluation():
    trucks = 0
    totalDist = 0
    valid = 0

    return trucks, totalDist, valid
def main():
    random.seed
    startTime = datetime.datetime.now()
    bestParent = generate_parent(len(target))
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    #initialize population function

    #loop for number of generations
        #create next candidate population function


if __name__ == '__main__':
    main()
'''