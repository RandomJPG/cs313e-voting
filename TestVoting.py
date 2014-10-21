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
    def test_ballot1(self):
        r = StringIO(" ")
        ballots = ballot(r)
        self.assertEqual(ballots, [])
        print (ballots)

    #Single ballot input
    def test_ballot2(self):
        r = StringIO("1")
        ballots = ballot(r)
        self.assertEqual(ballots.getVote(), 1)

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

        

