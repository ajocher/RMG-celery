import itertools

from rmgpy import settings
from rmgpy.data.rmg import getDB
from rmgpy.data.rmg import RMGDatabase
from rmgpy.molecule import Molecule
from rmgpy.scoop_framework.util import map_

def simple_react(n):
    # load RMG database to create reactions
    database = RMGDatabase()

    database.load(
        path = settings['database.directory'], 
        thermoLibraries = ['primaryThermoLibrary'], # can add others if necessary
        kineticsFamilies = 'all', 
        reactionLibraries = [], 
        kineticsDepositories = ''
    )

    kinetics_db = database.kinetics
    mol0 = Molecule().fromSMILES('CCCCCCCCC1CCCc2ccccc21')

    mol1 = Molecule().fromSMILES('CCCCCCCCC1CCCC2C=CC=CC=21')

    mol_tuple = (mol0, mol1)
    mol_tuples = [mol_tuple]*n

    results = map_(react_molecules_wrapper,
                   mol_tuples)

    reactions = itertools.chain.from_iterable(results)

    return list(reactions)

def react_molecules_wrapper(reactants):

    return getDB('kinetics').react_molecules(reactants, 
                           only_families=None,
                           prod_resonance=False)

if __name__ == '__main__':

    print simple_react(100)