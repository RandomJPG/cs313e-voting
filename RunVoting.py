# -------------------------------
# Chris Oballe, Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

import sys

from voting import read, Election

# ----
# main
# ----

def main():
    numElections = read(sys.stdin)
    
    while numElections > 0:
    
        elections = election()
        election.read(sys.stdin)
        election.evaluate()
        print election
        
        numElections -=1
 
 main()

