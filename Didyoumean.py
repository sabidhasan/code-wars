class Dictionary(object):
    def __init__(self, words):
        self.words = words
        
    def find_most_similar(self,term):
        if term in self.words: return term
        len_dif = map(lambda x: abs(len(x) - len(term)) , self.words)
        
        
        true_comp = []

        for c, item in enumerate(self.words):
            shortest = item if len(item) < len(term) else term
            longest = term if shortest == item else item

            #loop through frames
            #print longest, '      ', shortest,
            count = 0
            for f_len in range(1, len(shortest)):
                # print "checking %s letter words" % f_len
                for i in range(len(shortest) - f_len +1):
                    # print shortest[i:i+f_len], '       ', longest[i:i+f_len] 
                    # print shortest[i:i+f_len]
                    count = count + (longest.count(shortest[i:i+f_len] ) )#*f_len
            # try:
            true_comp.append(float(count) - (len_dif[c]*2))
            print float(count) - (len_dif[c]*2)
            # except:
                # true_comp.append(0)
                # print 'same', float(count), len_dif[c]
        
        print self.words, term, max(true_comp), self.words[true_comp.index(max(true_comp))]
        return  self.words[true_comp.index(max(true_comp))]
  #                      print shortest[i:f_len], longest.count(shortest[i:f_len])
            
            # diff = 0
            # print 'testing', item, ' and term is ', term
            # for count, letter in enumerate(shortest):
                #print count, letter, longest[count]
                # if letter != longest[count]:
                    # diff += 1
            # char_comp.append(diff)
        # x = [sum(item) for item in zip(len_dif, char_comp)]
        # print len_dif
        # print char_comp
        # print min(x)
        # print self.words[x.index(min(x))]
            
test_dict = Dictionary(['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana'])
test_dict.find_most_similar('strawbery')