#!/usr/bin/env python
import sys
from pcbnew import *
import math
#ToUnits = ToMM
#FromUnits = FromMM
#ToUnits=ToMils
#FromUnits=FromMils
#filename=sys.argv[1]
pcb = LoadBoard("led_circle.kicad_pcb")
#pcb = LoadBoard("test.kicad_pcb")

def PointsInCircum(r,n=16):
    return [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in xrange(0,n+1)]



def SetObjs(pcb):
    last = None
    count = 0
    points = PointsInCircum(5000000)

    new_points = []
    for p in points:
        new_points.append(wxPoint(p[0]*4,p[1]*4))
        #new_points.append(wxPoint(0,0))

    for module in pcb.GetModules():
        if("D" in module.GetReference()):

            module.SetPosition(new_points[count])
            print module.GetPosition()
            print new_points[count]
            count +=1


# for module in pcb.GetModules():
#     print "* Module: %s"%module.GetReference()
#     try:
#         module.GetValueObj().SetVisible(False)      # set Value as Hidden
#         module.GetReferenceObj().SetVisible(True)   # set Reference as Visible
#     except Exception as e:
#         print e



SetObjs(pcb)
        #    print "* Module: %s at %s"%(module.GetReference(),ToUnits(module.GetPosition()))
pcb.Save("led_circle.kicad_pcb")

#help(last)
