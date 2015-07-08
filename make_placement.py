#!/usr/bin/env python
import sys
from pcbnew import *
import math
pcb = LoadBoard("led_circle.kicad_pcb")

def PointsInCircum(r,n=16):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in xrange(0,n+1)]

def SetObjs(pcb):
    last = None
    count = 0
    points = PointsInCircum(5000000)

    new_points = []
    for p in points:
        new_points.append(wxPoint(p[0]*4,p[1]*4))

    for module in pcb.GetModules():
        if("D" in module.GetReference()):

            module.SetPosition(new_points[count])
            print module.GetPosition()
            print new_points[count]
            count +=1

SetObjs(pcb)
pcb.Save("led_circle.kicad_pcb")
