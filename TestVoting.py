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

    #Blank input
    def test_ballot1(self):
        r = StringIO(" ")
        ballots = ballot(r)
        self.assertEqual(ballots, [])
        print (ballots)

# ----
# main
# ----

main()

        

