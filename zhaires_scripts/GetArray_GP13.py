# whipped up from Matias's GenerateArrayFromshower.py for gp13


from math import sqrt
from random import randrange, random
import numpy as np

def get_gp13(arrayfile):
    
    #generate a core position
    #In a regular hexagon, the simplest method is to divide it into three rhombuses.
    # That way (a) they have the same area, and (b) you can pick a random point in any one rhombus with
    # two random variables from 0 to 1. (thanks Greg Kuperberg at stack overflow!).

    def randinunithex():
      vectors = [(-1.,0),(.5,sqrt(3.)/2.),(.5,-sqrt(3.)/2.)]
      x = randrange(3);
      (v1,v2) = (vectors[x], vectors[(x+1)%3])
      (x,y) = (random(),random())
      return (x*v1[0]+y*v2[0],x*v1[1]+y*v2[1])

    v=randinunithex()
    core=np.zeros(3)
    core[0]=v[0]
    core[1]=v[1]
    core[2]=0

    #load the points
    ant_pos=np.loadtxt(arrayfile)#,usecols = (2,3,4))
    
    
    
    #determine exagon size, to get the scaledcore position
    hexagon_size=(max(ant_pos[:,0])-min(ant_pos[:,0]))/2
    #scale the core
    core=core*hexagon_size*2 # PM: core can be outside the array with 50% chance
    #move the core
    ant_pos=ant_pos-core
    return core, ant_pos

