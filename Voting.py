# -------------------------------
# Jacob Garcia
# jg56492
# -------------------------------

# ------------
# voting_read
# ------------

def voting_read (r):
    """
    Reads the two lines
    Determines the number of elections to process
    """
    
    line = r.readline()
    r.readline()

    try:
        num_elections = int(line)
    except ValueError:
        num_elections = 0

    return num_elections

# --------------
# class Ballot
# --------------

class ballot:

    '''
    A ballot in an election
    Contains a list of ints representing 
    '''
    
    def __init__(self, line):
        assert type(line) is str	
	
        self.marker = 0
        self.votes = []

        for vote in line.split():
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
        
        assert type(name) is str

        self.name = name
        self.ballots = []

    def __str__(self):
        return self.name
    
    def addVote (self, ballot ):
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
        
        output = ""

        for winner in self.winners:
            output += str(winner) + '\n'

        return output

    def readBallots(self, r):
        '''
        Reads ballots
        '''
        
        while(True::
            line = r.readline()
            ballots = ballot(line)
            if line == "\n" or line="":
                break
            self.ballots.append(ballot)


    def readCandidates(self, r):
        '''
        Reads candidates
        '''

        line = r.readline()
        
        try:
            candidates = int(line)
        except ValueError:
            candidates = 0

        while (candidates > 0):
            line = reader.readline()
            line = line.strip()
            candidate = candidate(line)
            self.candidates.append(candidate)

            candidates -= 1    

    def read(self, r):
        '''
        Reads from both readCandidates and readBallots
        '''

        self.readBallots(r)
        self.readCandidates(r)

    def run(self):
        '''
        Runs election
        '''

        while(True):

            # Assign ballots to set up while loop
            for ballot in self.Ballots:
                vote = ballot.getVote()
                candidate = self.candidate[vote - 1]
                candidate.add(ballot)
            
            while(True):

                '''
                Terminating condidtions
                '''

                #Check for a majority winner
                half = len(self.ballots) // 2
                for candidate in self.candidates:
                    if candidate.numVotes > half:
                        self.winners = [candidate]
                        return self.winners

                #Check for a tie between all candidates
                votes = []
                for candidate in self.candidates:
                    numVotes = candidate.numVotes()
                    if numVotes != 0:
                        votes.append(numVotes)
      
                if len(votes) > 0 and votes.count(votes[0]) == len(votes):
                    for candidate.numVotes() != 0:
                        self.winners.append(candidate)
                    return self.winners

               '''
               Non-terminating condidtions
               '''
            
               # Find candidate/candidates  with least votes
               leastVotes = -1
               for candidate in self.candidate:
                   numVotes = candidate.numVotes()

                   if numVotes <= 0:
                      continue
                   if leastVotes == -1:
                      leastVotes = numVotes
                   else:
                      leastVotes = min(leastVotes, numVotes)

               # Remove candidate/candidates with least votes
               ballots = []
               for candidate in self.candidate:
                   if leastVotes == candidate.numVotes():
                       ballots.extend(candidate.getBallots())
                       candidate.remove()
               
               # Restribute
               for ballot in ballots:
                   while (True):
                       vote = ballot.getVote()
                       candidate = self.candidates[vote -1]
                       if (canddiate.numVotes() !=0)
                           candidate.add(ballot)
                           break
