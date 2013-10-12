#!/usr/bin/env python

import sys, os
import CORBA, Philosophy, Philosophy__POA

PHILOSOPHY_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'philosophy.py'))

class PhilosophyServer(Philosophy__POA.PhilosophyServer):
    def philosophize(self):
        pipe   = os.popen(PHILOSOPHY_PATH)
        wisdom = pipe.read()
        if pipe.close():
            # An error occurred with the pipe
            wisdom = "An error occurred while trying to philosophize."
        return wisdom

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = PhilosophyServer()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()
