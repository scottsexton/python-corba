#!/usr/bin/env python
import CORBA, Philosophy

class PhilosophyClient(object):
    def __init__(self, ior):
        orb = CORBA.ORB_init()
        self.servant = orb.string_to_object(ior)
        self.servant._narrow(Philosophy.PhilosophyServer)

    def philosophize(self):
        print self.servant.philosophize()
