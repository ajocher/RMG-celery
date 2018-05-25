from rmgpy import settings
from rmgpy.data.rmg import RMGDatabase
from rmgpy.molecule import Molecule

from celery_framework.celery_app import app

@app.task(ignore_result=False)
def database_setup():
    # load RMG database to create reactions
    database = RMGDatabase()

    database.load(
        path = settings['database.directory'], 
        thermoLibraries = ['primaryThermoLibrary'], # can add others if necessary
        kineticsFamilies = 'all', 
        reactionLibraries = [], 
        kineticsDepositories = ''
    )

    thermodb = database.thermo
    print thermodb.libraries.keys()


@app.task(ignore_result=False)
def simple_react():
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
    mol = Molecule().fromSMILES('CC')

    reactants = [mol]
    return kinetics_db.react_molecules(reactants, 
                           only_families=['R_Recombination'],
                           prod_resonance=False)

