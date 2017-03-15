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

#Get distance between locations
def LocationDist(locF,locT):
    From = Location(locF)
    To = Location(locT)
    distance = (From(1)-To(1))**2+(From(2)-To(2))**2)**(1/2)
    return distance

#get location
def Location(loc):
    Loc0 = Location(0, 0, 2, 0, 100000000)
    Loc1 = Location(45, 68, 2, 2, 20)
    Loc2 = Location(45, 70, 4, 2, 200)
    Loc3 = Location(42, 66, 5, 15, 4000)
    Loc4 = Location(42, 68, 3, 0, 10)
    Loc5 = Location(42, 65, 1, 2, 1)
    Loc6 = Location(40, 69, 1, 2, 1)
    Loc7 = Location(40, 66, 6, 2, 1)
    Loc8 = Location(38, 68, 7, 2, 1)
    Loc9 = Location(38, 70, 2, 2, 1)
    Loc10 = Location(35, 66, 1, 2, 1)
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


def totalRouteDist(route=[]):
    dist = 0
    for x in range(len(route)):
        if x == 0:
            dist = dist + LocationDist(0,route[x])
        if x+1 == len(route):
            dist = dist + LocationDist(route[x],0)
        else:
            dist = dist + LocationDist(route[x-1],route[x])

def checkValid(route=[])
    time = 0
    valid = true
    for x in range(len(route)):
        if x == 0:
            time = time + LocationDist(0,route[x])
        if x+1 == len(route):
            time = time + LocationDist(route[x],0)
        else:
            time = time + LocationDist(route[x-1],route[x])
        return valid

def evaluation(chromosome=[]):
    trucks = 4
    totalDist = 0
    valid = True
    route1 = []
    route2 = []
    route3 = []
    route4 = []

    #check to see if  the route is valid with time  windows
    if checkValid(route1) == False:
        valid = False
    if checkValid(route2) == False:
        valid = False
    if checkValid(route3) == False:
        valid = False
    if checkValid(route4) == False:
        valid = False

    #sum to get total distance
    totalDist = distR1 + distR2 + distR3 + distR5

    #gets total # of trucks
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