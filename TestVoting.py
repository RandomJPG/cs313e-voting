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
    # ----
    # read
    # ----
    
    # One line
    def test_read_1(self):
        r = StringIO("1 \n")
        read = voting_read(r)
        self.assertEqual(read, 1)
    
    # Multiple Lines
    def test_read_2(self):
        r = StringIO("2 \n""\nApple Pie")
        read = voting_read(r)
        self.assertEqual(read, 2)
    
    # --------
    # ballot
    # --------
   
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
        
    # Out of order ballot
    def test_ballot5(self):
        ballots = ballot("3 2 1 5 6 4")
        self.assertEqual(str(ballots), "[3, 2, 1, 5, 6, 4]")
        self.assertEqual(ballots.getVote(), 3)
        self.assertEqual(ballots.getVote(), 2)
        self.assertEqual(ballots.getVote(), 1)
        self.assertEqual(ballots.getVote(), 5)
        self.assertEqual(ballots.getVote(), 6)
        self.assertEqual(ballots.getVote(), 4)

    # ----------
    # candidate
    # ----------

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
        candidates.addVote(ballot(""))
        self.assertEqual(candidates.numVotes(), 1)

    #Multiple vote
    def test_candidate4(self):
        candidates = candidate("Charlie")
        self.assertEqual(str(candidates), "Charlie")
        candidates.addVote(ballot(""))
        candidates.addVote(ballot(""))
        candidates.addVote(ballot(""))
        self.assertEqual(candidates.numVotes(), 3)

    # ----------
    # election
    # ----------

    # Blank candidates
    def test_election1(self):
        r = StringIO('')
        elections = election()
        elections.readCandidates(r)
        self.assertEqual(len(elections.candidates), 0)

    # One candidate
    def test_election2(self):
        r = StringIO("1\nMe\n")
        elections = election()
        elections.readCandidates(r)
        self.assertEqual(len(elections.candidates), 1)
        self.assertEqual(str(elections.candidates[0]), "Me")
        
    # Multiple candidates
    def test_elections3(self):
        r = StringIO("2\nMe\nYou\n")
        elections = election()
        elections.readCandidates(r)
        self.assertEqual(len(elections.candidates), 2)
        self.assertEqual(str(elections.candidates[0]), "Me")
        self.assertEqual(str(elections.candidates[1]), "You")
        
    # Blank ballots
    def test_elections4(self):
       r = StringIO('')
       elections =election()
       elections.readCandidates(r)
       self.assertEqual(len(elections.ballots), 0)
       self.assertEqual(elections.ballots, [])
    
# ----
# main
# ----

main()

        

