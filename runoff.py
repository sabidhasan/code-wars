def runoff(voters):
    #Majority needed to win (> 50%)
    majority = len(voters)/2.0
    
    #Generate set of all candidates; used to figure out which candidates not voted on
    all_voters = {ballot for row in voters for ballot in row}
    
    #rounds of election
    election_rounds = len(voters[0])
    
    for number in range(election_rounds):
        #winner stores the tally of the current round
        winner = {}
        #tally the votes
        for row in voters:
            if row[0] in winner and row[0]:
                winner[row[0]] += 1
            else:
                winner[row[0]] = 1
        print winner
        break
        #now find lowest and highest count
        highest = []
        lowest = []
        for candidate, votes in winner.items():
            if votes == max(winner.values()):
                highest.append(candidate)
            #two seperate if blocks because voters might be both highest and lowest (eg 1)
            if votes == min(winner.values()):
                lowest.append(candidate)
        
        #Add all non-voted for candidates also need to be removed (eg. if you get no votes in first round youre out)!
        for candidate in all_voters:
            if not(winner.get(candidate)):
                lowest.append(candidate)

        #if highest vote was non existent, then there is no winner
        if highest[0] == '':
            print "No winner"
            return None
        
        #check for winner
        if winner[highest[0]] >= majority:
            return highest[0]
        
        #shift over losers, by looping through the voters again
        for count, row in enumerate(voters):
            #if the leading voter is loser, then
            if row[0] in lowest:
                #this is needed so that we can see if there are no more candiadates left
                row[0] = ''
                #loop through the remaining choices
                for counter,choices in enumerate(row[1:]):
                    #if the choice is loser, then invalidate it, otherwise move it to top of list
                    if choices in lowest:
                        row[1+counter] = ''
                    else:
                        row[0] = choices
                        break

voters = [
['Johan Liebert', 'Drake Luft', 'Brian J. Mason', 'Daisuke Aramaki', 'Gihren Zabi', 'Abelt Dessler'],
['Abelt Dessler', 'Brian J. Mason', 'Daisuke Aramaki', 'Johan Liebert', 'Drake Luft', 'Gihren Zabi'],
['Drake Luft', 'Gihren Zabi', 'Abelt Dessler', 'Brian J. Mason', 'Daisuke Aramaki', 'Johan Liebert'],
['Brian J. Mason', 'Johan Liebert', 'Gihren Zabi', 'Drake Luft', 'Abelt Dessler', 'Daisuke Aramaki'],
['Drake Luft', 'Johan Liebert', 'Daisuke Aramaki', 'Brian J. Mason', 'Gihren Zabi', 'Abelt Dessler'],
['Johan Liebert', 'Drake Luft', 'Gihren Zabi', 'Daisuke Aramaki', 'Brian J. Mason', 'Abelt Dessler'],
['Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Abelt Dessler', 'Daisuke Aramaki', 'Gihren Zabi'],
['Brian J. Mason', 'Abelt Dessler', 'Johan Liebert', 'Drake Luft', 'Gihren Zabi', 'Daisuke Aramaki']
]
   
runoff(voters)          