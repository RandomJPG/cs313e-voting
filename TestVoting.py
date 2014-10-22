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
        candidates = candidate("")
        self.assertEqual(str(candidates), "")

    #No vote
    def test_candidate2(self):
        candidates = candidate("Abe")
        self.assertEqual(str(candidates), "Abe")

    #One vote
    def test_candidate3(self):
        candidates = candidate("Bob")
        self.assertEqual(str(candidates), "Bob")
        candidates.add(ballot(""))
        self.assertEqual(candidates.numVotes(), 1)

    #Multiple vote
    def test_candidate4(self):
        candidates = candidate("Charlie")
        self.assertEqual(str(candidates), "Charlie")
        candidates.add(ballot(""))
        candidates.add(ballot(""))
        candidates.add(ballot(""))
        self.assertEqual(candidates.numVotes(), 3)

    #----------
    # election
    #----------

    

# ----
# main
# ----

main()

        

