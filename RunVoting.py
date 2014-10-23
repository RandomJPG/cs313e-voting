# -------------------------------
# Chris Oballe, Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

import sys

from Voting import voting_read, election

# ----
# main
# ----

def main():
    numElections = voting_read(sys.stdin)
    
    while numElections > 0:
    
        elections = election()
        elections.read(sys.stdin)
        elections.run()
        print (elections)
        
        numElections -=1
 
main()

