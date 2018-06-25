import time
import sys

from reaction_generation import simple_react


if __name__ == '__main__':

    start = time.time() 

    n_cp = int(sys.argv[1])
    n_iter = int(sys.argv[2])
    n_pool = int(sys.argv[3])

    result = simple_react(n_cp, n_iter, n_pool)
    end = time.time()
    
    print end - start

