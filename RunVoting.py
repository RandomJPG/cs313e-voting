# -------------------------------
# Chris Oballe, Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

import sys

from voting import voting_read, voting_guess, voting_solve, voting_print, voting_dict

# ----
# main
# ----

voting_solve(sys.stdin, sys.stdout, c = open("/u/prat0318/voting-tests/erb988-ProbeAnswers.txt","r"), d1 = open("/u/prat0318/voting-tests/hs9234-mvrtg.txt", 'r'), d2 = open("/u/prat0318/voting-tests/kj8293-cacheUserAvg.txt", 'r') )

