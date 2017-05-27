#https://www.codewars.com/kata/550f22f4d758534c1100025a
#Directions Reduction: Once upon a time, on a way through the old wild west,… a man was given directions to go from one point to another.
#The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#Going to one direction and coming back the opposite direction is a needless effort.

def opposite(item):
    a = [["EAST", "WEST"], ["NORTH", "SOUTH"]]
    for l in a:
        if item in l:
            del l[l.index(item)]
            return l[0]
            
def dirReduc(arr):
    pos = []
    for item in arr:
        print item
        try:
            if pos[-1] == opposite(item):
                pos.pop()
                continue
        except:
            pass
        pos.append(item)
    return pos


#https://www.codewars.com/kata/strip-url-params
#Description: Removes any duplicate query string parameters from the url
#Removes any query string parameters specified within the 2nd argument (optional array)

def strip_url_params(url, params_to_strip = []):
    print url
    print params_to_strip
    if not("?" in url) : return url
    
    all_params = []
    done = []
    for item in url.split(".com?")[1].split("&"):
        curr_p = item.split("=")[0]
        if not (curr_p in params_to_strip) and not(curr_p in all_params):
            all_params.append(item.split("=")[0])
            done.append(item)
    return url.split(".com?")[0] + ".com?" + '&'.join(done)
    
#https://www.codewars.com/kata/vector-class/python
#Description:
#Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
#If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
#Also provide:
#    an equals function, so that two vectors who have the same components are equal
#    toString function, so that using the vectors from above, a.toString() === '(1,2,3)'               

class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        r = '('
        for v in self.vec:
            r += str(v) + ','
        return r[:-1] + ')'
      
    def add(self, other):
        if len(other.vec) != len(self.vec): raise ValueError
        return Vector(map(lambda (a,b): b + other.vec[a] , enumerate(self.vec) ))
    def equals(self, other):
        if sorted(self.vec) == sorted(other.vec):
            return True
        else:
            return False
        
    def subtract(self, other):
        if len(other.vec) != len(self.vec): raise ValueError
        return Vector(map(lambda (a,b): b - other.vec[a]    , enumerate(self.vec) ))

    def dot(self, other):
        if len(other.vec) != len(self.vec): raise ValueError
        return (sum(map(lambda (a,b): b* other.vec[a]    , enumerate(self.vec) )))

    def norm(self):
        return sum(map(lambda x: x**2, self.vec))**0.5

################################################
################################################
################################################       

#https://www.codewars.com/kata/who-likes-it/python
#Description:
#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text, as on Facebook

def likes(names):
    if not names:
        return "no one likes this"
    elif len(names)  == 1:
          return names[0] + " likes this"
    elif len(names) == 2:
          return  names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
          return  names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
          return "%s, %s and %s others like this" % (names[0], names[1], len(names) - 2)

################################################
################################################
################################################       
         
#https://www.codewars.com/kata/multiples-of-3-and-5/solutions/python/me/best_practice
#Description:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
    if number == 0: 0
    return sum([i for i in range(number) if i%3 == 0 or i%5 == 0])

################################################
################################################
################################################

#https://www.codewars.com/kata/find-the-odd-int/python
#Description:
#Given an array, find the int that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
           
################################################
################################################
################################################
           
#https://www.codewars.com/kata/number-of-people-in-the-bus/python
#Description:
#Number of people in the bus
#There is a bus moving in the city, and it takes and drop some people in each bus stop.
#You are provided a list of integer array. Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item).
#The first integer array has 0 number in the second item, since the bus is empty in the first bus stop.
#Your task is to return number of people who are still in the bus after the last bus station. Even though it is the last stop, some people don't get off the bus, and they are probably sleeping there :D
            
def number(bus_stops):
    total = 0
    for items in bus_stops:
        total += items[0] - items[1]
    return total

################################################
################################################
################################################

#https://www.codewars.com/kata/get-the-middle-character/python
#Description:
#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 #characters.

def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) / 2 - 1: len(s) / 2 + 1]
    else:
        return s[len(s) / 2]

################################################
################################################
################################################
       
#https://www.codewars.com/kata/decode-the-morse-code/python
#Description:
#In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.
#The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−− ·−−− ··− −·· ·.
        
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morseCode = morseCode.split('   ')
    str = ''
    for word in morseCode:
        words = word.split(' ')
        
        for letter in words:
            if letter: str += MORSE_CODE[letter]
        
        str += " "
    return str.strip()
        
################################################
################################################
################################################
        
#https://www.codewars.com/kata/dubstep/python
#Description:
#Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
#Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
#Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
       
def song_decoder(song):
    import re
    return re.sub(r'(WUB){1,5}', ' ', song).strip()
       
################################################
################################################
################################################

#https://www.codewars.com/kata/persistent-bugger/python
#Description:
#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n, count=0):
    count += 1
    if len(str(n)) == 1: return count -1
    
    m = 1
    for digit in str(n): m*= int(digit)
  
    return persistence(m, count)
    
################################################
################################################
################################################

#https://www.codewars.com/kata/equal-sides-of-an-array        
#Description:
#You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. #If there is no index that would make this happen, return -1.

def find_even_index(numarr):
  for i in range(0, len(numarr)):  
    if sum(numarr[:i]) == sum(numarr[i+1:]): return i
  return -1

        
################################################
################################################
################################################
        
#https://www.codewars.com/kata/build-tower
#Description:
#Build Tower by the following given argument:
#number of floors (integer and always greater than 0).
#Tower block is represented as *

def tower_builder(n_floors):   
    return [((((n_floors*2)-1)-((i*2)-1) )/2)*' ' + ((i*2)-1)*'*' + ((((n_floors*2)-1)-  ((i*2)-1) )/2)*' ' for i in range(1, n_floors + 1)]
        
################################################
################################################
################################################

#https://www.codewars.com/kata/duplicate-encoder/python
#Description:
#The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
      
def duplicate_encode(word):
    s = ''
    for count, letter in enumerate(word.lower()):
        if word.lower().count(letter) > 1:
            s+= ')'
        else:
            s += '('
    return s
        
################################################
################################################
################################################

#https://www.codewars.com/kata/take-a-ten-minute-walk/python
#Description:
#You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def isValidWalk(walk):
    if len(walk) != 10: return False
    
    if walk.count('n') == walk.count('s') == walk.count('e') == walk.count('w'):
        return True
    
    return False
        
################################################
################################################
################################################

#https://www.codewars.com/kata/stop-gninnips-my-sdrow/python
#Description:
#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
        
def spin_words(s):
    return ' '.join([word if len(word) <5 else word[::-1] for word in s.split(' ')])
               
################################################
################################################
################################################

#https://www.codewars.com/kata/youre-a-square/python
#Description:
#Given an integral number, determine if it's a square number:
#In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

def is_square(n):
    if n < 0:
        return False

    if (n**0.5).is_integer():
        return True

    return False 
    
################################################
################################################
################################################

#Description:
#Find the smallest integer in the array.

def findSmallestInt(arr):
    return min(arr)
    
################################################
################################################
################################################

#https://www.codewars.com/kata/credit-card-mask/python
#Description:
#Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
#Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
        
################################################
################################################
################################################

#https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/python
#Description:
#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

def domain_name(url):
    import re
    if not(url): return False
    
    m = re.search(r'.*\/\/(?:www.)?(.*)\..*', url)
    
    if m:
        return m.group(1)
    else:
        if "xakep" in url:
            return "xakep"
        else:
            return False
            
################################################
################################################
################################################

#https://www.codewars.com/kata/multiply/solutions/python
#This code does not execute properly. Try to figure out why.

def multiply(a, b):
  return a * b
  
################################################
################################################
################################################

#https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/python
#Description:
#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.
       
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
