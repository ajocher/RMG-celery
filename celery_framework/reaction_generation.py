from rmgpy import settings
from rmgpy.data.rmg import RMGDatabase

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