from rmgpy import settings
from rmgpy.data.rmg import RMGDatabase
from rmgpy.molecule import Molecule
from rmgpy.data.rmg import getDB

import itertools

from celery_framework.celery_app import app

#@app.task(ignore_result=False)
#def database_setup():
#    # load RMG database to create reactions
#    database = RMGDatabase()
#
#    database.load(
#        path = settings['database.directory'], 
#        thermoLibraries = ['primaryThermoLibrary'], # can add others if necessary
#        kineticsFamilies = 'all', 
#        reactionLibraries = [], 
#        kineticsDepositories = ''
#    )
#
#    thermodb = database.thermo
#    print thermodb.libraries.keys()


@app.task(ignore_result=False)
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
    mol2 = Molecule().fromSMILES('CC')

    mol_tuple = (mol0, mol1)

    reactions = []
    for i in range(n_iter):
        mol_tuples = [mol_tuple]*n_cp

        # Execute celery map
#        result = map(react_molecules_wrapper, mol_tuples)

        # Execute celery map and group
        result2 = group(map(react_molecules_wrapper, mol_tuples))
        result = result2.join()

        # Execute celery map, chunks and group
#        result2 = chunks(map(react_molecules_wrapper, mol_tuples),2).group()
#        result = result2.join()

#        reactions_iter = itertools.chain.from_iterable(result)
#        print "{0} iter: {1} reactions.".format(i, len(list(reactions_iter)))

    return result


def react_molecules_wrapper(reactants):

    return getDB('kinetics').react_molecules(reactants,
                           only_families=None,
                           prod_resonance=False)


