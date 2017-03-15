'''
Skip to content
This repository
Search
Pull requests
Issues
Gist
 @CongOSU
 Sign out
 Watch 1
  Star 0
 Fork 0 CongOSU/HW4_MO-GA
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathHW4_MO-GA/HW_4.py
77276b4  8 minutes ago
 LAPTOP-27T359M3\RothC removed locations class
1 contributor
RawBlameHistory     
224 lines (190 sloc)  6.04 KB
'''
import math
import sys
import random


#Get distance between locations
def LocationDist(locF,locT):
    From = Location(locF)
    To = Location(locT)
    distance = ((From[0]-To[0])**2+(From[1]-To[1])**2)**(1/2)
    return distance

#get location
def Location(loc):

    # Xloc,Yloc,ReadyTime,CloseTime,ServiceTime
    Loc0 = [0, 0, 0, 100000000, 0]
    Loc1 = [45, 68, 85, 900, 20]
    Loc2 = [45, 70, 100, 500, 20]
    Loc3 = [42, 66, 5, 1500, 20]
    Loc4 = [42, 68, 350, 1000, 20]
    Loc5 = [42, 65, 85, 200, 10]
    Loc6 = [40, 69, 0, 350, 10]
    Loc7 = [40, 66, 0, 920, 10]
    Loc8 = [38, 68, 70, 2000, 15]
    Loc9 = [38, 70, 3000, 3100, 15]
    Loc10 = [35, 66, 2500, 2750, 15]

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

def initializePop():

    initialPop_1 = []
    initialPop_2 = []
    initialPop_1 = random.sample(range(1, 11), 10)
    #print(initialPop_1)
    initialPop_2 = random.sample(range(1, 11), 10)
    #print(initialPop_2)

    trucksID_1 = []
    trucksID_2 = []
    while len(trucksID_1) < 10:
        trucksID_1.append(random.randint(1,4))
    print(trucksID_1)
    while len(trucksID_2) < 10:
        trucksID_2.append(random.randint(1,4))
    #print(trucksID_2)
    
    initial_1=[]
    initial_2=[]
    initial_1.append(initialPop_1)
    initial_2.append(initialPop_2)
    initial_1.append(trucksID_1)
    initial_2.append(trucksID_2)
    return initial_1, initial_2



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
    #A = initializePop()
    #parent_a = A[4]
    #parent_b = A[5]
    n = len(parent_a)
    cross_points = sorted([random.randint(0, n) for _ in range(2)])
    swapped = _swap(parent_a, parent_b, cross_points)
    mapped = _map(swapped, cross_points)
 
    return mapped


def mutation(individual):
    start, stop = sorted(random.sample(range(len(individual)), 2))
    individual = individual[:start] + individual[stop:start-1:-1] + individual[stop+1:]
    return individual,


def totalRouteDist(route=[]):
    dist = 0
    if route == []:
        return dist

    for x in range(len(route)):
        if x == 0:
            dist = dist + LocationDist(0,route[x])
        if x+1 == len(route):
            dist = dist + LocationDist(route[x],0)
        else:
            dist = dist + LocationDist(route[x-1],route[x])

def checkValid(route=[]):
    time = 0
    valid = True
    if route == []:
        return valid

    for x in range(len(route)):
        Loc=Location(x)
        if x == 0:
            time = time + LocationDist(0,route[x])
            if time < Loc(2):
                time = Loc(2)+Loc(4)
            else:
                time = time + Loc(4)
        if x+1 == len(route):
            time = time + LocationDist(route[x],0)
            if time < Loc(2):
                time = Loc(2)+Loc(4)
            else:
                time = time + Loc(4)
        else:
            time = time + LocationDist(route[x-1],route[x])

        if time > Loc(3):
            valid = False
            return valid

    return valid

def evaluation(chromosome=[]):
    trucks = 4
    totalDist = 0
    valid = True
    route1 = []
    route2 = []
    route3 = []
    route4 = []

    for i in range(len(chromosome[0])):
        dex = chromosome[0].index(i+1)
        if chromosome[1][dex] == 1:
            route1.append(chromosome[0][dex])
        if chromosome[1][dex] == 2:
            route2.append(chromosome[0][dex])
        if chromosome[1][dex] == 3:
            route3.append(chromosome[0][dex])
        if chromosome[1][dex] == 4:
            route4.append(chromosome[0][dex])

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
    totalDist = totalRouteDist(route1)+totalRouteDist(route2)+totalRouteDist(route3)+totalRouteDist(route4)

    #gets total # of trucks
    if route1 == []:
        trucks = trucks - 1
    if route2 == []:
        trucks = trucks - 1
    if route3 == []:
        trucks = trucks - 1
    if route4 == []:
        trucks = trucks - 1

    #weighted objected function
    weightedObj = trucks * 50 + totalDist

    return trucks, totalDist, valid, weightedObj



def main():
    candidate = []
    count = 0
    '''
    candidate1, candidate2 = initializePop()
    candidate.append(candidate1)
    print(candidate1)
    '''
    while count < 10:
        candidate1, candidate2 = initializePop()
        x,y,val1,z = evaluation(candidate1)
        x,y,val2,z = evaliation(candidate2)
        if val1 == True:
            candidate.append(candidate1)
            count = count + 1
            if count == 10:
                break
        if val2 == True:
            candidate.append(candidate2)
            count = count + 1
            
    for i in range(10):
        for j in range(i+1, 10):
            candidate3_1, candidate4_1 = PMXcrossover(candidate[i][0], candidate[j][0])
            candidate3, candidate4 = PMXcrossover(candidate[i][1], candidate[j][1])
            candidate.append(candidate3)
            candidate.append(candidate4)
            
    for i in range(len(candidate)):
        candidate5_1 = mutation(candidate[i][0])
        candidate5 = mutation(candidate[i][1])
        candidate.append(candidate)
        
    final_candidate = []
    for i in range(len(candidate)):
        x, y, valid, z = candidate[i]
        if valid == True:
            final_candidate.append(candidate[i])
    print(final_candidate)







    #initialize population function

    #loop for number of generations
        #create next candidate population function


if __name__ == '__main__':
    main()

    '''Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
'''