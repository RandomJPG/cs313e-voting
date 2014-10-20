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
    
    big_list     = []
    movie_number = 0
    
    for line in r:
        line = line.strip()
        if ":" in line:
            movie_list    = []
            movie_list.append(int(line[:-1]))
            big_list.append(movie_list)
            movie_number += 1
        else:
            big_list[movie_number - 1].append(int(line))
    
    assert big_list != []
    return(big_list)

# -------------
# voting_guess  
# -------------

def voting_guess (l, c, d1, d2):
    """

    guess ratings for users
    l is a multi-dimensional list of movies and users
    c is a multi-dimensional list of the correct answers
    d1 is a dictionary of movie averages
    d2 is a dicitonary of user averages
    returns a list of guess ratings for users with rsme from correct answers appended
    """

    for movie in l:
        for user in range(1, len(movie)):
            movie[user] = (0.515 * d1[movie[0]] + 0.52 * d2[movie[user]]) - .12
            

    rsme = voting_rsme(l, c)
    l.append(rsme)


    return(l)

# -------------
# voting_print
# -------------

def voting_print (l,w):
    """

    print movies and guessed ratings with rsme at the end
    l is a multi-dimensional list of movies and guesses
    w is a writer
    prints movies with guesses on new lines
    """

    for movie in l[:-1]:
        for user in range(len(movie)):
            if user == 0:
                w.write(str(movie[user]) + ":" + "\n")
            else:
                w.write(str(round(movie[user], 1)) + "\n")

    w.write('RMSE:'+ ' ' + str(l[-1]))

    

    

# -------------
# voting_solve
# -------------

def voting_solve(r,w,c, d1, d2):
    """
    solve voting problem
    r is a reader
    w is a writer
    c is a txt file containing the correct answers
    d1 is a txt file containing movie averages
    d2 is a txt file containing user averages
    """

    l    = voting_read(r)
    corr = voting_read(c)
    dic1 = voting_dict(d1)
    dic2 = voting_dict(d2)
    g    = voting_guess(l,corr, dic1, dic2)
    voting_print(g,w)            

# -------------
# voting_rsme
# -------------
	
def voting_rsme(a,p):
    """
    determines root square mean error
    a is a multi-dimensional list of guesses
    p is a multi-dimensional list of answers
    returns root square mean error
    """
    
    p_keys     = [movie[0] for movie in p]  # From the answer key, extract answers for movies in a
    p_relevent = []
    for movie in a:
        if movie[0] in p_keys:
            p_relevent.append(p[a.index(movie)])

    assert len(a) == len(p_relevent)
	
    sum        = 0
    count      = 0    
    for movie in range(len(a)):
        for rating in range(1, len(a[movie])):
            diff_sq = (a[movie][rating] - p_relevent[movie][rating]) ** 2
            sum    += diff_sq
            count  += 1

    avg_sq = sum / float(count)
    rsme   = (avg_sq) ** 0.5
    rsme   = format(rsme, '.2f')

    assert float(rsme) >= 0
    return rsme

# ------------
# voting_dict
# ------------

def voting_dict(r):
    """
    build a dictionary of averages
    r is a reader
    return a dictionary of averages indexed by id
    """

    avg_dict = {}

    for line in r:
        line = line.strip()
        line = line.split()
        avg_dict[int(line[0])] = float(line[1])


    return avg_dict
   

    



    



