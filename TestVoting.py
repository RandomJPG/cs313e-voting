# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Voting import voting_read, ballot, candidate, election

#------------
# Testvoting
#------------

class TestVoting (TestCase) :
    
    #--------
    # ballot
    #--------
   
    #Blank ballot input


    #Single ballot input
    def test_ballot2(self):
        r = StringIO("1")
        ballots = ballot(r)
        self.assertEqual(ballots.getVote(), 1)

    #Multiple ballot input
    def test_ballot3(self):
        r = StringIO("1 2 3 4 5")
        ballots = ballot(r)
        print (ballots)

    #----------
    # candidate
    #----------

    #----------
    # election
    #----------

    

# ----
# main
# ----

main()

        

