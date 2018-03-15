#assuming N = 3 for RRT*
import math, sys, pygame, random
from math import *
from pygame import *
from pylygon import Polygon

class Node(object):
    def __init__(self, point, parent):
        super(Node, self).__init__()
        self.point = point
        self.parent = parent

XDIM = 900
YDIM = 900
windowSize = [XDIM, YDIM]
delta = 15.0
GAME_LEVEL = 1
GOAL_RADIUS = 10
MIN_DISTANCE_TO_ADD = 1.0
NUMNODES = 5000
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode(windowSize)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
cyan = 0,180,105
dark_green = 0, 102, 0

count = 0
triObs = []

def dist(p1,p2):     #distance between two points
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def point_circle_collision(p1, p2, radius):
    distance = dist(p1,p2)
    if (distance <= radius):
        return True
    return False

def step_from_to(p1,p2):
    if dist(p1,p2) < delta:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + delta*cos(theta), p1[1] + delta*sin(theta)

def collides(p):    #check if point collides with the obstacle
    for tri in triObs:
        if tri.collidepoint(p) == True:
            return True
    return False


def get_random_clear():
    while True:
        p = random.random()*XDIM, random.random()*YDIM
        noCollision = collides(p)
        if noCollision == False:
            return p


def init_obstacles(obss):  #initialized the obstacle
    global triObs
    triObs = []
    tri = []
    print("config "+ str(obss[1]))
    print ("obss",obss[2:])
    for obs in obss[2:len(obss)-1]:
        print("obs",obs)
        tri = [int(t)/10 for t in obs.split(" ")]
        if len(tri)<6:
            pass
        else:
            print(">>>tri", tri)
            #triObs.append(Polygon([(tri[0:1]), (tri[2:3]), (tri[4:5])]))
            triObs.append(Polygon([(tri[0],tri[1]), (tri[2],tri[3]), (tri[4],tri[5])]))
            #triObs.append(Polygon([(0, 70), (110, 0), (110, 70)]))
    print(triObs)            
    for _ in triObs:
        pygame.draw.polygon(screen, black, _)
        
def reset(lines):
    global count
    numObs = lines[1]
    screen.fill(white)

    init_obstacles(lines)
    count = 0

def main():
    global count
    
    with open("input_1.txt", "r") as f:
        lines = f.read().splitlines()

    #for index,l in enumerate(lines):
        #if index == 0:
        line0 = lines[0].split(" ")

    initPoseSet = True
    initialPoint = Node([int(line0[0])/10, int(line0[1])/10], None)
    pygame.draw.circle(screen, red, initialPoint.point, GOAL_RADIUS)
    print(initialPoint.point)
    goalPoseSet = True
    goalPoint = Node([int(line0[2])/10, int(line0[3])/10], None)
    pygame.draw.circle(screen, blue, goalPoint.point, GOAL_RADIUS)
    print(goalPoint.point)
    currentState = 'buildTree'

    nodes = []
    path_nodes = []
    reset(lines)

    while True:
    
        nodes.append(initialPoint)
        if currentState == 'goalFound':
            currNode = goalNode.parent
            pygame.display.set_caption('Goal Reached')
            print("Goal Reached")
            while currNode.parent != None:
                pygame.draw.line(screen,red,currNode.point,currNode.parent.point)
                currNode = currNode.parent
            optimizePhase = True
        elif currentState == 'optimize':
            fpsClock.tick(0.5)
            pass
        elif currentState == 'buildTree':
            count = count+1
            pygame.display.set_caption('Performing RRT')
            if count < NUMNODES:
                foundNext = False
                while foundNext == False:
                    rand = get_random_clear()
                    rand2 = get_random_clear()
                    rand3 = get_random_clear()
                    parentNode = nodes[0]
                    path_nodes.append(parentNode)
                    for p in nodes:
                        if dist(p.point,rand) <= dist(parentNode.point,rand) and dist(p.point,rand2) <= dist(parentNode.point,rand2) and dist(p.point,rand3) <= dist(parentNode.point,rand3):
                            newPoint = step_from_to(p.point,rand)
                            newPoint2 = step_from_to(p.point,rand2)
                            newPoint3 = step_from_to(p.point,rand3)
                            if collides(newPoint) == False and collides(newPoint2) == False and collides(newPoint3) == False:
                                parentNode = p
                                foundNext = True
                            path_nodes.append(parentNode)

                newnode = step_from_to(parentNode.point,rand)
                newnode2 = step_from_to(parentNode.point,rand2)
                newnode3 = step_from_to(parentNode.point,rand3)
                nodes.append(Node(newnode, parentNode))
                nodes.append(Node(newnode2, parentNode))
                nodes.append(Node(newnode3, parentNode))
                pygame.draw.line(screen,blue,parentNode.point,newnode)
                pygame.draw.line(screen,green,parentNode.point,newnode2)
                pygame.draw.line(screen,dark_green,parentNode.point,newnode3)

                if point_circle_collision(newnode, goalPoint.point, GOAL_RADIUS) or point_circle_collision(newnode2, goalPoint.point, GOAL_RADIUS) or point_circle_collision(newnode3, goalPoint.point, GOAL_RADIUS):
                    currentState = 'goalFound'

                    goalNode = nodes[len(nodes)-1]

                
            else:
                print("Ran out of nodes... :(")
                return;

        pygame.display.update()
        fpsClock.tick(10000)


if __name__ == '__main__':
    main()
    







