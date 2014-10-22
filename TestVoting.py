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
        ballots = ballot("")
        self.assertEqual(str(ballots), "[]")

    #Single ballot input
    def test_ballot2(self):
        ballots = ballot("1")
        self.assertEqual(str(ballots), "[1]")
        self.assertEqual(ballots.getVote(), 1)

    #Multiple ballot input
    def test_ballot3(self):
        ballots = ballot("1 2 3 4 5")
        self.assertEqual(str(ballots), "[1, 2, 3, 4, 5]")
        self.assertEqual(ballots.getVote(), 1)
        self.assertEqual(ballots.getVote(), 2)
        self.assertEqual(ballots.getVote(), 3)
        self.assertEqual(ballots.getVote(), 4)
        self.assertEqual(ballots.getVote(), 5)

    #Extra space in ballot input
    def test_ballot4(self):
        ballots = ballot("1 2 3               4")
        self.assertEqual(str(ballots), "[1, 2, 3, 4]")
        self.assertEqual(ballots.getVote(), 1)
        self.assertEqual(ballots.getVote(), 2)
        self.assertEqual(ballots.getVote(), 3)
        self.assertEqual(ballots.getVote(), 4)

    #----------
    # candidate
    #----------

    #Blank candidate 
    def test_candidate1(self):

    #No votes
    def test_candidate2(self):

    #One vote
    def test_candidate3(self):

    #Multiple votes
    def test_candidate4(self):

    #----------
    # election
    #----------

    

# ----
# main
# ----

main()

        

