# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# ------------
# voting_read
# ------------

def voting_read (r):
    """
    
    read movies and users
    r a reader
    return a multi-dimensional list, 1st entry in each list is a movie number followed by customer ids
    """
    

# --------------
# class Ballot
# --------------

class ballot:

    '''
    A ballot in an election
    Contains a list of ints representing 
    '''
    
    def __init__(self, line):
		
        self.marker = 0
        self.votes = []

        for vote in line:
            vote = int(vote)
            self.votes.append(vote)

    def __str__(self):
        return str(self.votes)
		
    def getVote(self):
        marker = self.marker
        self.marker += 1
        return self.votes[marker]

# ---------------
# class Candidate
# ---------------

class candidate:
   
    '''
    A candidate in an election
    Has a asscioated name and ballot
    '''

    def __init__(self, name):
        '''
        Constructor
        One list for each candidate
        '''
        
        self.name = name
        self.ballots = []
    
    def add (self, ballot ):
        '''
        Adds a ballot to candidate
        '''

        self.ballots.append(ballot)

    def clear(self):
        '''
        Resets all ballots from candidate
        '''
        
        self.ballots=[]

    def getBallots(self):
        '''
        Returns all ballots for this candidate
        '''

        return self.ballots

    def numVotes(self):
        '''
        Returns the number of votes for this candidate
        '''

        return len(self.ballots)

# ---------------
# class Election
# ---------------

class election:
    '''
    An Australiam voting election
    '''

    def __init__(self):
        self.ballots = []
        self.candidates = []
        self.winners = []

    def __str__(self):
        '''
        Returns the winner/winners of this election
        '''

    def solve(self):
        '''
        Determines the winner of the election
        '''
