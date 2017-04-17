#https://www.codewars.com/kata/molecule-to-atoms/python
#Description:
#For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object.
#For example:
#water = 'H2O'
#parse_molecule(water)                 # return {H: 2, O: 1}
#magnesium_hydroxide = 'Mg(OH)2'
#parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}
#var fremy_salt = 'K4[ON(SO3)2]2'
#parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
#As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.
#Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

import re

def int_parse(text):
#'''This function recieves a text of two characters (found using regex), and returns the integer portion. e.g. "12" (returns 12)  or "5X" (returns 5) or "4[" (returns 4) or "[C" (returns None) or "[5" returns None  '''
    try:
        return int(text)
    except ValueError:
        try:
            return int(text[0])
        except ValueError:
            return None

def parse_molecule(mol):
    #This dictionary will be returned out of this function
    results = {}
    
    #make last digit fix; should be double digit for regex searching later, it expects all brakcets to end with two digits
    try:
        mol = mol[:-1] + '0' + str(int(mol[-1:]))
    except ValueError:
        mol += '01'
    #loop until molecule doesnt change anymore
    while True:  
    #attempt to find a bracket, if fail the exit the loop we are done
        find_bracket = re.search(r'([({\[][A-Za-z0-9]*[)}\]])(..)', mol)

        if find_bracket is None:
            break   #time to fix work through rest of formula,. no more brackets left!

        #bracket found; find the multiplier for the bracket (two digits after the bracket)
        multiplier = int_parse(find_bracket.groups()[1])
        #Lireatl text is one of three thigns: either it's find_bracket.groups()[0] (in the case of a bracket wiht nothing outside it),
    #or its find_bracket.groups()[0] + multipler, or that plus '0' plus multiplier
    
    #if multiplier is None then literal text (as found in formula) should just be the bracket,
    #otherwise it should be the bracket + number found
    #literal text is literally th
        if multiplier is None:
            literal_text = find_bracket.groups()[0]
            multiplier = 1
        else:
            literal_text = find_bracket.groups()[0] + str(multiplier)

        #now enumerate bracket
        elements = re.findall(r'([A-Z][a-z]?)([0-9]{0,2})', find_bracket.groups()[0])
        fixed_bracket = ''
        for element in elements:
            if not(element[1]):
                atom_count = 1
            else:
                atom_count = int(element[1])
            atom_count *= int(multiplier)
            fixed_bracket += str(element[0] + str(atom_count))
        if literal_text in mol:
            mol = mol.replace(literal_text, fixed_bracket, 1)
        else:
            mol = mol.replace(literal_text[:-1] + '0' + literal_text[-1], fixed_bracket, 1)
    #now make dict out of given data
    elements = re.findall(r'([A-Z][a-z]?)([0-9]{0,5})', mol)
    for element in elements:
        if element[0] in results:
            try:
                results[element[0]] += int(element[1])
            except ValueError:
                results[element[0]] += 1
        else:
            try:
                results[element[0]] = int(element[1])
            except ValueError:
                results[element[0]] = 1
    return results

#################################################
#################################################
#################################################

#Description:
#Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
#The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#Detailed rules
#The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
#The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
#For the purpose of this Kata, a year is 365 days and a day is 24 hours.

import collections
def format_duration(seconds):
    if seconds == 0: return "now"
    #Define time ordered dictionary
    times = collections.OrderedDict([('year', 31536000), ('day', 86400), ('hour', 3600), ('minute', 60), ('second', 1)])
    #Results that will be returned
    res = []
    #Loop through times starting from biggest, and add them on
    for duration in times.values():
        curr_time = seconds / duration 
        res.append(curr_time)
        seconds -= duration*curr_time
    
    #loop through results, and make into strings; objects added keeps track of last
    st = ''
    objects_added = 0
    for count, item in enumerate(res):
        if item != 0:
            objects_added += 1
            #plural determines plurality, ender determines whether we add comma or and
            plural = 's' if item > 1 else ''
            ender = ' and ' if objects_added + 1 == 5 - res.count(0) else ', '
            
            st += str(item) + ' ' + times.keys()[count] + plural + ender
    return st[:-2]      #remove trailing space and comma


#################################################
#################################################
#################################################

#https://www.codewars.com/kata/catching-car-mileage-numbers/python
#Description:
#"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?
#Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).
#"Interesting" Numbers
#Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
#Any digit followed by all zeros: 100, 90000
#Every digit is the same number: 1111
#The digits are sequential, incementing†: 1234
#The digits are sequential, decrementing‡: 4321
#The digits are a palindrome: 1221 or 73837
#The digits match one of the values in the awesomePhrases array

def is_interesting(number, awesome_phrases):
    num_str = str(number)
    closes = [number+1, number+2]
    #Length
    if len(num_str) <3:
        num_str = '263690'
    if closes[0] < 100:
        closes[0] = 263690
    if closes[1] < 100:
        closes[1] = 263690
        
    print num_str, awesome_phrases, closes    

    #one digit all zeros
    if int(num_str[1:]) == 0: return 2
    #every digit same
    if len(set(num_str)) == 1: return 2
    #sequential ; increasing
    tmp = [10 if i == '0' else int(i) for i in list(num_str)]
    if tmp == range(tmp[0], tmp[0]+len(tmp)): return 2
    #sequential ; decreasing
    tmp =  [int(i) for i in num_str][::-1]
    if tmp == range(tmp[0], len(tmp)+tmp[0]) : return 2
    #palindrome
    if num_str == num_str[::-1]: return 2
    #awesomePhrases
    if number in awesome_phrases: return 2

    #one digit all zeros
    for others in closes:
        if int(str(others)[1:]) == 0: return 1
    #every digit same
    for others in closes:
        if len(set(str(others))) == 1: return 1
    #sequential ; increasing    
    for others in closes:
        tmp = [10 if i == '0' else int(i) for i in list(str(others))]
        if tmp == range(tmp[0], tmp[0]+len(tmp)): return 1    
    #sequential ; decreasing
    for others in closes:
        tmp = [int(i) for i in str(others)][::-1]
        if tmp == range(tmp[0], len(tmp)+tmp[0]): return 1
    #palindrome
    for others in closes:
        if str(others) == str(others)[::-1]: return 1
    #awesomePhrases
    print '49;'
    for others in closes:
        #print others, awesome_phrases, closes
        if others in awesome_phrases: return 1
    
    return 0

#################################################
#################################################
#################################################

#https://www.codewars.com/kata/social-golfer-problem-validator/python
#Description:
#A group of N golfers wants to play in groups of G players for D days in such a way that no golfer plays more than once with any other golfer. For example, for N=20, G=4, D=5, the solution at Wolfram MathWorld is
# Mon:    ABCD    EFGH    IJKL    MNOP    QRST
# Tue:    AEIM    BJOQ    CHNT    DGLS    FKPR
# Wed:    AGKO    BIPT    CFMS    DHJR    ELNQ
# Thu:    AHLP    BKNS    CEOR    DFIQ    GJMT
# Fri:    AFJN    BLMR    CGPQ    DEKT    HIOS

def valid(golf_game):
    #relations holds strings of which player has played which player, in alphabetic
    #order (e.g. AC means A played C; CA would be written "AC"). players dict is for 
    #game count of each player
    relations = []
    players = {}
    for day in golf_game:
        #Check for length of number of games c.f. first game lenght
        if len(day) != len(s[0]): return False
        #temporary list to hold every player who plays in one day ['A', 'B', 'C', 'D', 'E' ...]
        players_today = []
        for game in day:
            #if game length is not consistent (first game is arbitrary, but all must be the same length!)
            if len(game) != len(s[0][0]): return False
            #loop over the game strings themselves, then over remaining players in list
            #ABCD --> A-B, A-C, A-D, B-C, B-D, C-D (etc)
            for counter, player in enumerate(game):
                #add player to dictionary
                if players.get(player):
                    players[player] += 1
                else:
                    players[player] = 1
                for otherplayers in game[counter+1:]:
                    #add the alphabetized list of players whove played each other to relations table
                    relations.append(''.join(sorted([player , otherplayers])))
            players_today.extend(game)
        
        #Check for duplicity
        if len(players_today) != len(set(players_today)): return False
    #Check for an odd out player, who hasn't played the right # of games (dict holds each players game count)
    if len(set(players.values())) != 1: return False
    #Check for duplicity in the whole game (if two peoiple have playued each other > 1)
    if len(set(relations)) != len(relations): return False
    return True

#################################################
#################################################
#################################################

#https://www.codewars.com/kata/breadcrumb-generator/python
#Description:
#As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link to do all the dirty work in my place.
#What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.
#All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.
#one last extra rule: if one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.
#Ignore anchors and parameters

import re
def generate_bc(url, separator):
    #replace trailing slash, http[s]://, easier to do with regex than without
    bad_regs = ['^https?:\/\/', '\/$']
    for regs in bad_regs:
        t = re.compile(regs)
        url = t.sub('', url)
    #url now contains the fixed URL

    #First pull apart URL by '/' and remove all parametric junk (?, #, etc)
    links = [x.split('?')[0].split('#')[0] for x in url.split('/')]

    #make new list, which will contain the growing return value
    s_ret = []    
    #If final one is index.something, then we need to ignore it, otherwise fix it up by removing '.something'
    if 'index.' in links[-1]:
        links.pop()
    else:
        links[-1] = links[-1].split('.')[0]

    #first one is always HOME, but if only one thing, then it is SPAN rather than anchor
    if len(links) == 1:
        s_ret.append('<span class="active">HOME</span>')
    else:
        s_ret.append('<a href="/">HOME</a>')
    
    #bad words that are ignored for shortening URL
    bads = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    #start at 1, because first one already dealt with.,..
    for count,link in enumerate(links[1:]):
        #must prettify if too long
        if len(link) > 30:
            #split by hyphen, and filter out the bad words
            removed_words_link = filter(lambda x: not(x.lower() in bads), link.split('-'))
            #re glue the link together with first character(s) only
            link = ''.join([x[0] for x in removed_words_link])            
        #if we are not on final one, then add it with achonr, otherwise add as span, we use splicing to ensure 
        #full URL up to now is included. also replace hyphens with spaces and make uppercase
        if count != len(links) -2:
            s_ret.append('<a href="/%s/">%s</a>' % ('/'.join(links[1:count+2]), link.replace('-', ' ').upper()))
        else:
            s_ret.append('<span class="active">%s</span>' % link.replace('-', ' ').upper())
    
    return separator.join(s_ret)


#################################################
#################################################
#################################################

#https://www.codewars.com/kata/ip-validation/python
#Description:
#Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.
#Examples of valid inputs: 1.2.3.4 123.45.67.89
#Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089

def is_valid_IP(strng):
    if strng.count('.') != 3 : return False
    if len(strng) == 0: return False
    
    
    l = strng.split('.')
    for k in l:
        if k[0:1] == '0' or k[0:1] == ' ' or k[-1] == ' ': return False
        
        try:
            k = int(k)
        except ValueError:
            return False
            
        if k > 255 or k < 0: return False
    return True
    
#################################################
#################################################
#################################################

#https://www.codewars.com/kata/valid-braces/python
#Description:
#Write a function called validBraces that takes a string of braces, and determines if the order of the braces is valid. validBraces should return true if the string is valid, and false if it's invalid.
#A string of braces is considered valid if all braces are matched with the correct brace


def validBraces(string):
  while len(string) > 0:
    replaced = False
    for item in ["()", "[]", "{}"]:
      if item in string:
        string = string.replace(item, '')
        replaced = True
    if replaced == False:
      return False
  return True

#################################################
#################################################
#################################################

#https://www.codewars.com/kata/ten-pin-bowling/python
#Description:
#Ten-Pin Bowling
#In this challenge you will be given a string representing a player's ten frames. It will look something like this: 'X X 9/ 80 X X 90 8/ 7/ 44' (in Java: "X X 9/ 80 X X 90 8/ 7/ 44"), where each frame is space-delimited, 'X' represents strikes, and '/' represents spares. Your goal is take in this string of frames into a function called bowlingScore and return the players total score.

def get_score(tup):
  if tup[1] == 'X' or tup[1] == '/':
    return 10
  else:
    return int(tup[1])

def bowling_score(frames):
  #11 11 11 11 11 11 11 11 11 11
  frame_list = []
  total_score = 0
  #score_list = []
  
  for frame_count, frame in enumerate(frames.split(' ')):
    for ball in frame:
      frame_list.append((frame_count, ball,))
  
  #loop through and add scores
  for counter, score in enumerate(frame_list):
    if score[1] == "X":
      if score[0] != 9:
        total_score = total_score + 10
        #look at the next two scores, if X then add 10, if num/ then add 10, otherwuse add numbers
        if frame_list[counter+1][1] == 'X':
          total_score += 10
        else:
          total_score += get_score(frame_list[counter+1])  
        #now do second throw
        if frame_list[counter+2][1] == 'X':
          total_score += 10
        elif frame_list[counter+2][1] == '/':
          total_score -= get_score(frame_list[counter+1])
          total_score += 10
        else:
          total_score += get_score(frame_list[counter+2])  
      else:
        total_score += 10
    elif score[1] == "/":
      if score[0] != 9:
        #if next one is strike, or next one is number
        #print 'old total score  ', total_score, ' new totla score ', total_score - int(frame_list[counter-1][1]) + 10
        total_score = total_score - int(frame_list[counter-1][1]) + 10
        if frame_list[counter+1][1] == "X":
          total_score += 10
        else:
          total_score += int(frame_list[counter+1][1]) 
      else:
        total_score = total_score + 10 - int(frame_list[counter-1][1])
    else:
      total_score += int(score[1])
    
    #score_list.append((frame_list[counter][1], total_score))
  return total_score  
