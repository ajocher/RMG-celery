import itertools

from rmgpy import settings
from rmgpy.data.rmg import getDB
from rmgpy.data.rmg import RMGDatabase
from rmgpy.molecule import Molecule
from rmgpy.scoop_framework.util import map_

def simple_react(n_cp, n_iter):
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

    reactions = []
    for _ in range(n_iter):
        mol_tuples = [mol_tuple]*n_cp
        results = map_(react_molecules_wrapper,
                       mol_tuples)

        reactions_iter = itertools.chain.from_iterable(results)
        reactions.extend(list(reactions_iter))

    return reactions

def react_molecules_wrapper(reactants):

    return getDB('kinetics').react_molecules(reactants, 
                           only_families=None,
                           prod_resonance=False)

if __name__ == '__main__':

    print len(simple_react(n_cp=1, n_iter=1))