# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from voting import voting_read, voting_guess, voting_print, voting_solve, voting_rsme, voting_dict
#------------
# Testvoting
#------------

class TestVoting (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self):
        r               = StringIO("1:\n10813\n20000\n40\n2:\n12355")
        user_movie_list = voting_read(r)
        self.assertEqual(user_movie_list, [[1, 10813, 20000, 40],[2, 12355]])

    def test_read_2 (self):
        r               = StringIO("1:\n34\n567\n67\n2:\n45\n6788\n88\n3:\n12\n13\n4:\n6789\n567:\n222\n2234\n226")
        user_movie_list = voting_read(r)
        self.assertEqual(user_movie_list, [[1, 34, 567, 67], [2, 45, 6788, 88], [3, 12, 13], [4, 6789], [567, 222, 2234, 226]])

    def test_read_3 (self):
        r               = StringIO("1:")
        user_movie_list = voting_read(r)
        self.assertEqual(user_movie_list, [[1]])

    # -----
    # guess
    # -----

    def test_guess_1 (self):
        l            = [[1, 33, 567, 67], [36, 19, 34]]
        c            = [[1, 3, 3, 3], [36, 3, 3]]
        d1           = {1:3, 36:3.0}
        d2           = {33:2, 567:2, 67:2, 19:2, 34:2}
        user_guesses = voting_guess(l,c, d1, d2)
        self.assertEqual(user_guesses,[[1, 2.465, 2.465, 2.465], [36, 2.465, 2.465],'0.54']) 

    def test_guess_2 (self):
        l            = [[1, 33, 567, 67], [36, 19, 34]]
        c            = [[1, 3, 3, 3], [36, 3, 3]]
        d1           = {1:3, 36:2.0}
        d2           = {33:2, 567:2, 67:2, 19:2.5, 34:2.5}
        user_guesses = voting_guess(l,c, d1, d2)
        self.assertEqual(user_guesses,[[1, 2.465, 2.465, 2.465], [36, 2.21, 2.21],'0.65'])
     

    # -----
    # print
    # -----
    
    def test_print_1 (self):
        w      = StringIO() 
        l      = [[1, 2, 3], [4, 5, 6], 3]
        voting_print(l,w)
        self.assertEqual(w.getvalue(), "1:\n2\n3\n4:\n5\n6\nRMSE: 3")

    def test_print_2 (self):
        w = StringIO()
        l = [[1, 2.3456, 2.67],[2, 4.677, 3.333], 1.0]
        voting_print(l,w)
        self.assertEqual(w.getvalue(), "1:\n2.3\n2.7\n2:\n4.7\n3.3\nRMSE: 1.0")
    
    def test_print_3(self):
        w = StringIO()
        l = [[1, 2.3456, 2.67],[2, 4.677, 3.333], '1.0']
        voting_print(l,w)
        self.assertEqual(w.getvalue(), "1:\n2.3\n2.7\n2:\n4.7\n3.3\nRMSE: 1.0")
    # -----
    # solve
    # -----

    def test_solve (self):
        r  = StringIO("1:\n34\n567\n67\n2:\n45\n6788\n88\n3:\n12\n13\n4:\n6789\n567:\n222\n2234\n226")
        w  = StringIO()
        c  = StringIO("1:\n3\n3\n3\n2:\n3\n3\n3\n3:\n3\n3\n4:\n3\n567:\n3\n3\n3\n")
        d1 = StringIO("1 3\n2 3\n3 3\n4 3\n567 3")
        d2 = StringIO("34 3\n567 3\n67 3\n45 3\n6788 3\n88 3\n12 3\n13 3\n6789 3\n222 3\n2234 3\n226 3")
        voting_solve(r, w, c, d1, d2)
        self.assertEqual(w.getvalue(), "1:\n3.0\n3.0\n3.0\n2:\n3.0\n3.0\n3.0\n3:\n3.0\n3.0\n4:\n3.0\n567:\n3.0\n3.0\n3.0\nRMSE: 0.02")
    
    # ----
    # rsme
    # ----
    
    def test_rsme_1 (self):   
        a = [[2,2, 3, 4]]
        b = [[2,4, 1, 6]]
        c = voting_rsme(a, b)
        self.assertEqual(c, '2.00')

    def test_rsme_2 (self):
        a = [[1, 2, 3, 4, 5], [2, 2, 3, 4, 5]]
        b = [[1, 1, 3, 5, 7], [2, 1, 1, 1, 1]] 
        c = voting_rsme(a, b)
        self.assertEqual(c, '2.12')

    def test_rsme_3 (self):
        a = [[3, 2, 3, 4, 5], [4, 1, 2, 3]]
        b = [[3, 2, 3, 4, 5], [4, 3, 4, 4]]
        c = voting_rsme(a, b)
        self.assertEqual(c, '1.13')

    def test_rsme_4 (self):
        a = [[2, 1]]
        b = [[2,2]]
        c = voting_rsme(a, b)
        self.assertEqual(c, '1.00')

    def test_rsme_5 (self):
        a = [[4, 3, 3, 3, 3 ,3, 3, 3, 3], [5, 5], [6, 4, 4, 5]]
        b = [[4, 1, 3, 2, 2, 2, 3, 3, 3],[5, 3], [6, 2, 3, 3]]
        c = voting_rsme(a, b)
        self.assertEqual(c, '1.29')

    def test_rsme_6 (self):
        a = [[0,0],[1]]
        b = [[0,0],[1]]
        c = voting_rsme(a,b)
        self.assertEqual(c, '0.00')

    # ----
    # dict
    # ----

    def test_dict_1 (self):
        a = StringIO("1 2\n3 4")
        b = voting_dict(a)
        self.assertEqual(b[1], 2)
        self.assertEqual(b[3], 4)

    def test_dict_2(self):
        a = StringIO("1 2.56\n3 4.7")
        b = voting_dict(a)
        self.assertEqual(b[1], 2.56)
        self.assertEqual(b[3], 4.7)

    def test_dict_3(self):
        a = StringIO("1 2.56\n3 4.7\n5 4.5556")
        b = voting_dict(a)
        self.assertEqual(b[1], 2.56)
        self.assertEqual(b[3], 4.7)
        self.assertEqual(b[5], 4.5556)
        
   
        
    
# ----
# main
# ----

main()

        

