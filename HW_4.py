import math
import sys
import random

class Location():
    def __init__(self,xloc,yloc,service, lowTime,highTime,ID):
        self.ID = ID
        self.xloc = xloc
        self.yloc = yloc
        self.service = service
        self.lowTime = lowTime
        self.highTime = highTime

#Get Locations function
def Location(loc):
    Loc0 = Location(0, 0, 2, 0, 100000000)
    Loc1 = Location(10, 12, 2, 2, 20)
    Loc2 = Location(-5, 15, 4, 2, 200)
    Loc3 = Location(25, -1, 5, 15, 4000)
    Loc4 = Location(5, 5, 3, 0, 10)
    Loc5 = Location(26, 4, 1, 2, 1)
    Loc6 = Location(-18, -9, 1, 2, 1)
    Loc7 = Location(10, 11, 6, 2, 1)
    Loc8 = Location(15, -5, 7, 2, 1)
    Loc9 = Location(28, 28, 2, 2, 1)
    Loc10 = Location(-28, 18, 1, 2, 1)
    if loc == 0:
        return Loc0
    if loc == 1:
        return Loc1
    if loc == 2:
        return Loc2
    if loc == 3:
        return Loc3
    if loc == 4:
        return Loc4
    if loc == 5:
        return Loc5
    if loc == 6:
        return Loc6
    if loc == 7:
        return Loc7
    if loc == 8:
        return Loc8
    if loc == 9:
        return Loc9
    if loc == 10:
        return Loc10

'''
def initializePop():

    initialPopulation = []

    while len(initialPopulation) < 10:

        trucks, totalDist, valid = evaluation()
        if valid == 1:
            initialPopulation

    return initialPopulation
'''


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

def PMXcrossover(ind1, ind2):
    size = (len(ind1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    temp1 = ind1[cxpoint1:cxpoint2+1] + ind2
    temp2 = ind1[cxpoint1:cxpoint2+1] + ind1
    ind1 = []
    for x in temp1:
        if x not in ind1:
            ind1.append(x)
    ind2 = []
    for x in temp2:
        if x not in ind2:
            ind2.append(x)
    return ind1, ind2


def mutation(individual):
    start, stop = sorted(random.sample(range(len(individual)), 2))
    individual = individual[:start] + individual[stop:start-1:-1] + individual[stop+1:]
    return individual,



def evaluation(chromosome=[]):
    trucks = 4
    totalDist = 0
    valid = 0
    route1 = []
    route2 = []
    route3 = []
    route4 = []
    #get routes
    for x in chromosome(1,):

    #compute distance
    #check to see if  the route is valid with time  windows
    for x in route1:
        if x == len(route1):
    for x in route2:
        if x == len(route1):
    for x in route3:
        if x == len(route1):
    for x in route4:
        if x == len(route1):

    #sum to get total distance
    totalDist = distR1 + distR2 + distR3 + distR5

    if route1 == []:
        trucks = trucks - 1
    if route2 == []:
        trucks = trucks - 1
    if route3 == []:
        trucks = trucks - 1
    if route4 == []:
        trucks = trucks - 1

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