# Junhui Cho
# Final Project
# jh00@bu.edu

import math

def clean_text(txt):
        """ takes a string of text txt as a parameter and returns
            a list containing the words in txt after it has been
            "cleaned"
        """
        text = txt.lower()
        for punctuations in '.,!?':
            text = text.replace(punctuations, '')
        return text

def stem(s):
        """ accepts a string as a parameter and return the stem of s
            The stem of a word is the root part of the word
        """
        stem = s
        if len(s) <= 3:
            return stem
        elif s[-1] == 's':
            stem = s[:-1]
            if s[-3:] == 'ies':
                stem = s[:-2]
            if s[-3:] == 'ers':
                stem = s[:-3]
        elif s[-1] == 'y':
            stem = s[:-1] + 'i'
        elif s[-1] == 'e':
            stem = s[:-1]
        elif s[-2:] == 'er':
            if s[-3] == s[-4]:
                stem = s[:-3]
            else:
                stem = s[:-2]
        elif s[-2:] == 'en':
            stem = s[:-2]
        elif s[-3:] == 'est':
            stem = s[:-3]
        elif s[-3:] == 'ful':
            stem = s[:-3]
        elif s[-3:] == 'ing':
            if len(s) >= 5:
                if s[-4] == s[-5]:
                    stem = s[:-4]
                else:
                    stem = s[:-3]
            else:
                stem = s
        return stem

def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs, and return their
        log similarity score
    """
    score = 0
    total = 0
    for x in d1:
        total += d1[x]
    for item in d2:
        if item in d1:
            score += (math.log(d1[item]/total)) * d2[item]
        else:
            score += (math.log(0.5/total)) * d2[item]
    return score
        

class TextModel:
    """ serve as a blueprint for objects that model a body of text """

    def __init__(self, model_name):
        """ constructs a new TextModel object by accepting a string
            model_name that is passed in a parameter
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuations = {}
        

    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations))
        return s


    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        for_sen_length = ''
        for letter in s:
            if letter in '?!;':
                    letter = letter.replace(letter, '.')
                    for_sen_length += letter
            else:
                    for_sen_length += letter
        list_words = for_sen_length.split('.')[:-1]
        for x in list_words:
            sentence = x.split()
            if len(sentence) in self.sentence_lengths:
                    self.sentence_lengths[len(sentence)] += 1
            else:
                    self.sentence_lengths[len(sentence)] = 1
                    
        for_punctuation = s.split()
        for word in for_punctuation:
            if word[-1] in '.,:;?-!':
                if word[-1] == '.' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == ',' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == ':' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == ';' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == '?' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == '-' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                elif word[-1] == '!' and word[-1] not in self.punctuations:
                    self.punctuations[word[-1]] = 1
                else:
                    self.punctuations[word[-1]] += 1
                
        
        cleaned = clean_text(s)
        word_list = cleaned.split()

        # Template for updating the words dictionary.
        for w in word_list:
            a = stem(w)
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
            if a not in self.stems:
                self.stems[a] = 1
            else:
                self.stems[a] += 1

        # Add code to update other feature dictionaries
        
            

    def add_file(self,filename):
        """ adds all of the tect in the file identified by filename
            to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)

    def save_model(self):
        """ saves the TextModel object self by writing its various
            feature dictionaries to files
        """
        f1 = open(self.name + '_words', 'w')
        f1.write(str(self.words))
        f1.close
        f2 = open(self.name + '_word_lengths', 'w')
        f2.write(str(self.word_lengths))
        f2.close
        f3 = open(self.name + '_stems', 'w')
        f3.write(str(self.stems))
        f3.close
        f4 = open(self.name + '_sentence_lengths', 'w')
        f4.write(str(self.sentence_lengths))
        f4.close
        f5 = open(self.name + '_punctuations', 'w')
        f5.write(str(self.punctuations))
        f5.close

    def read_model(self):
        """ reads the stored dictionaries for the called TextModel
            object from their files and assigns them to the
            attributes of the called TextModel
        """
        f1 = open(self.name + '_words', 'r')
        d_str1 = f1.read()
        f1.close
        self.words = dict(eval(d_str1))
        f2 = open(self.name + '_word_lengths', 'r')
        d_str2 = f2.read()
        self.word_lengths = dict(eval(d_str2))
        f2.close
        f3 = open(self.name + '_stems', 'r')
        d_str3 = f3.read()
        f3.close
        self.stems = dict(eval(d_str3))
        f4 = open(self.name + '_sentence_lengths', 'r')
        d_str4 = f4.read()
        f4.close
        self.sentence_lengths = dict(eval(d_str4))
        f5 = open(self.name + '_punctuations', 'r')
        d_str5 = f5.read
        f5.close
        self.punctuations = dict(eval(d_str5))

    def similarity_scores(self, other):
        """ returns a list of log similarity scores measuring the similarity of self
            and other
        """
        list_scores = []
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        punctuations_score = compare_dictionaries(other.punctuations, self.punctuations)
        list_scores += [word_score] + [word_lengths_score] + [stems_score] + [sentence_lengths_score] + [punctuations_score]
        return list_scores

    def classify(self, source1, source2):
        """ compares the called TextModel object to two other "source" TextModel
            objects (source1 and source2) and determines which of these other
            TextModel is the more likely source of the called TextModel
        """
        sources1 = self.similarity_scores(source1)
        sources2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ': ' + str(sources1))
        print('scores for ' + source2.name + ': ' + str(sources2))
        count1 = 0
        count2 = 0
        for x in range(len(sources1)):
            if sources1[x] > sources2[x]:
                count1 += 1
            elif sources1[x] < sources2[x]:
                count2 += 1
        if count1 > count2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)
        

# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def test():
    """ test function """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def run_tests():
    """ tests for the following articles """
    source1 = TextModel('times')
    source1.add_file('times1_source_text.txt')
    source1.add_file('times2_source_text.txt')
    source1.add_file('times3_source_text.txt')
    

    source2 = TextModel('chicagotribune')
    source2.add_file('chicago1_source_text.txt')
    source2.add_file('chicago2_source_text.txt')
    source2.add_file('chicago3_source_text.txt')
    

    new1 = TextModel('wr112')
    new1.add_file('wr112_source_text.txt')
    new1.classify(source1, source2)

    # Add code for three other new models below.
    print('\n')
    new2 = TextModel('martin')
    new2.add_file('martin_source_text.txt')
    new2.classify(source1, source2)
    print('\n')
    new3 = TextModel('globe')
    new3.add_file('globe_source_text.txt')
    new3.classify(source1, source2)
    print('\n')
    new4 = TextModel('usatoday')
    new4.add_file('usatoday_source_text.txt')
    new4.classify(source1, source2)


    

    
    
        
        
    
        

        
