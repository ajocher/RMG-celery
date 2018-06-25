from rmgpy import settings
from rmgpy.data.rmg import RMGDatabase
from rmgpy.molecule import Molecule
from rmgpy.data.rmg import getDB

import itertools
import gc
import time
import sys
import resource
# Shows different information on the memory of machine
import psutil 
from memory_profiler import profile
from multiprocessing import Pool


def initPool(num):
    print "Initializing pool with ", num,  " processes."

@profile
def parallel(mol_tuples_chunks, p):
    tmp = []

    # Execute multiprocessing map. It blocks until the result is ready.
    # This method chops the iterable into a number of chunks which it 
    # submits to the process pool as separate tasks. 
    # The (approximate) size of these chunks can be specified by setting 
    # chunksize to a positive integer.
    r = p.map_async(react_molecules_wrapper, mol_tuples_chunks, chunksize=1, callback=tmp.append)
    r.wait()
   
    return tmp

@profile
def simple_react(n_cp, n_iter, n_pool):
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

    p = Pool(processes=n_pool, initializer=initPool, initargs=(n_pool, ), maxtasksperchild=2)
    
    for i in range(n_iter):
        result = []
    
        mol_tuples = [mol_tuple]*n_cp

        # Check the number of cores and memory usage
        print("Information regarding memory usage:",psutil.virtual_memory())
        #    num_cores = psutil.cpu_count()
        #    print("This kernel has ",num_cores,"cores and you can find the information regarding the memory usage:",psutil.virtual_memory())

        result = parallel(mol_tuples, p)

        print '{0} iter: {1} reactions.'.format(i, len(list(itertools.chain.from_iterable(*result))))
        result = None
 
        # resource module for finding the current (Resident) memory
        # consumption (actual RAM that the program is using) in byte
        print 'Current (Resident) memory consumption {0}.'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    
    p.close()

    return result


def react_molecules_wrapper(reactants):

    return getDB('kinetics').react_molecules(reactants,
                           only_families=None,
                           prod_resonance=False)


