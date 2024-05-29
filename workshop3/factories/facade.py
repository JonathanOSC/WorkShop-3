"""
This file has some classes related to the implementation of facade strucutre design..
Author: Jonathan Ochoa
"""

from factories import HighEngineFactory, LowEngineFactory


class EnginesFacade:

    type_engines = {}

    @staticmethod
    def get_engine(self, type_engine):
        if type_engine not in EnginesFacade.type_engines[type_engine]:
            #Add engine type
            EnginesFacade.type_engines[type_engine] = 
        
        return self.low_engine
    
##POETRY
## Ctr + Alt = varias lineas