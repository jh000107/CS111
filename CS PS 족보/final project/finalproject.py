# Final Project
# Chan Sol Park
# CS 111

import math

def clean_text(txt):
            """takes a string of text txt as a parameter and returns
               a list containing the words in txt after it has been
              “cleaned”
            """
            replace = txt.lower()
            if '.' in replace:
                        replace = replace.replace('.','')
            if ',' in replace:
                        replace = replace.replace(',','')
            if '!' in replace:
                        replace = replace.replace('!','')
            if '?' in replace:
                        replace = replace.replace('?','')
            return replace

def stem(word):
            """gets a string and returns the stem of the string"""
            if len(word) <= 3 :
                        return word
            if len(word) == 4:
                        return word
            if word[2] == 'l' and word[3] == 'l':
                        return word[:4]
            if word[-4:] == 'iers':
                        word = word[:-3]
                        return word
            elif word[-1] == 's':
                        word = word[:-1]
                        return word
            elif word[-3:] == 'ies' :
                        word = word[:-2]
                        return word
            elif word[-2:] == 'ly':
                        word = word[:-2]
                        return word
            elif word[-3:] == 'ful':
                        word = word[:-3]
                        return word
            elif word[-2:] == 'er':
                        if word[-3] == word[-4]:
                                    word = word[:-3]
                                    return word
                        else:
                                    word = word[:-1]
                                    return word
            elif word[-3:] == 'ing':
                        if word[-4] == word[-5]:
                                    word = word[:-4]
                                    return word
                        else:
                                    word = word[:-3]+'e'
                                    return word
            elif word[-1] == 'y':
                        word = word[:-1] + 'i'
                        return word
            elif word[-2:] == 'ed':
                        word = word[:-2]
                        return word
            return word

def compare_dictionaries(d1, d2):
            """ takes two feature dictionaries d1 and d2 as
                inputs, and computes and return their
                log similarity score
            """
            score = 0
            total = 0
            for g in d1:
                        total += d1[g]
            for c in d2:
                        if c in d1:
                                    score += (d2[c])*(math.log(d1[c]/total))
                        else:
                                    score += (d2[c])*(math.log(0.5/total))
            return score
            
            

class TextModel:
            """ a blueprint for objects that model a body of text """
            def __init__(self, model_name):
                        """constructs a new TextModel object by
                           accepting a string model_name as a parameter
                        """
                        self.name = model_name
                        self.words = {}
                        self.word_lengths = {}
                        self.stems = {}
                        self.sentence_lengths = {}
                        self.punctuation = {}
                        
            def __repr__(self):
                        """Return a string representation of the TextModel."""
                        s = 'text model name: ' + self.name + '\n'
                        s += '  number of words: ' + str(len(self.words)) + '\n'
                        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
                        s += '  number of stems: ' + str(len(self.stems)) + '\n'
                        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
                        s += '  number of punctuations: ' + str(len(self.punctuation))
                        return s

            def add_string(self, s):
                        """adds a string of text s to the model by augmenting
                           the feature dictionaries defined in the constructor
                        """
                        pre_textfile = s.split()
                        for v in pre_textfile:
                                    if v[-1] in '?!.,:;':
                                                if v[-1] == '?' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                elif v[-1] == '!' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                elif v[-1] == '.' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                elif v[-1] == ',' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                elif v[-1] == ':' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                elif v[-1] == ';' and v[-1] not in self.punctuation:
                                                            self.punctuation[v[-1]] = 1
                                                else:
                                                            self.punctuation[v[-1]] += 1
                                    
                        textfile = ''
                        for b in s:
                                    if b in '.?!':
                                                b = b.replace(b, '.')
                                                textfile += b
                                    else:
                                                textfile +=b
                                                
                        pre_list = textfile.split('.')[:-1]
                                    
                        for z in pre_list:
                                    sen = z.split()
                                    if len(sen) not in self.sentence_lengths:
                                                self.sentence_lengths[len(sen)] = 1
                                    else:
                                                self.sentence_lengths[len(sen)] += 1
                        
                        clean = clean_text(s)
                        word_list = clean.split()
                        
                        for w in word_list:
                                    x = len(w)
                                    y = stem(w)
                                    if w not in self.words:
                                                self.words[w] = 1
                                    else:
                                                self.words[w] += 1
                                    if x not in self.word_lengths:
                                                self.word_lengths[x] = 1
                                    else:
                                                self.word_lengths[x] += 1
                                    if y not in self.stems:
                                                self.stems[y] = 1
                                    else:
                                                self.stems[y] += 1
                                                
            def add_file(self, filename):
                        """adds all of the text in the file identified by filename
                           to the model
                        """
                        f = open(filename, 'r', encoding='utf8', errors='ignore')
                        text = f.read()
                        self.add_string(text)

            def save_model(self):
                        """saves the TextModel object self by writing its various
                           feature dictionaries to files
                        """
                        f1 = open(self.name + '_words', 'w')
                        f2 = open(self.name + '_word_lengths', 'w')
                        f3 = open(self.name + '_stems', 'w')
                        f4 = open(self.name + '_sentence_lengths', 'w')
                        f5 = open(self.name + '_punctuation', 'w')
                        f1.write(str(self.words))
                        f2.write(str(self.word_lengths))
                        f3.write(str(self.stems))
                        f4.write(str(self.sentence_lengths))
                        f5.write(str(self.punctuation))
                        f1.close()
                        f2.close()
                        f3.close()
                        f4.close()
                        f5.close()

            def read_model(self):
                        """reads the stored dictionaries for the called TextModel
                           object from their files and assigns them to the
                           attributes of the called TextModel
                        """
                        f1 = open(self.name + '_words', 'r')
                        f2 = open(self.name + '_word_lengths', 'r')
                        f3 = open(self.name + '_stems', 'r')
                        f4 = open(self.name + '_sentence_lengths', 'r')
                        f5 = open(self.name + '_punctuation', 'r')
                        d_str1 = f1.read()
                        d_str2 = f2.read()
                        d_str3 = f3.read()
                        d_str4 = f4.read()
                        d_str5 = f5.read()
                        f1.close()
                        f2.close()
                        f3.close()
                        f4.close()
                        f5.close()
                        self.words = dict(eval(d_str1))
                        self.word_lengths = dict(eval(d_str2))
                        self.stems = dict(eval(d_str3))
                        self.sentence_lengths = dict(eval(d_str4))
                        self.punctuation = dict(eval(d_str5))

            def similarity_scores(self, other):
                        """returns a list of log similarity scores measuring
                           the similarity of self and other
                        """
                        word_score = []
                        word_score += [compare_dictionaries(other.words, self.words)]
                        word_score += [compare_dictionaries(other.word_lengths, self.word_lengths)]
                        word_score += [compare_dictionaries(other.stems, self.stems)]
                        word_score += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
                        word_score += [compare_dictionaries(other.punctuation, self.punctuation)]
                        return word_score

            def classify(self, source1, source2):
                        """compares the called TextModel object (self) to two other
                          “source” TextModel objects and determines which of these
                           other TextModels is the more likely source of the called TextModel
                        """
                        scores1 = self.similarity_scores(source1)
                        scores2 = self.similarity_scores(source2)
                        print('scores for',source1.name,': ', scores1)
                        print('scores for',source2.name,': ', scores2)
                        sum1 = 0
                        sum2 = 0
                        for a in scores1:
                                    sum1 += a
                        for b in scores2:
                                    sum2 += b
                        if sum1 >= sum2:
                                    print(self.name,'is more likely to have come from', source1.name)
                        else:
                                    print(self.name,'is more likely to have come from', source2.name)


def test():
            """ your docstring goes here """
            source1 = TextModel('source1')
            source1.add_string('It is interesting that she is interested.')

            source2 = TextModel('source2')
            source2.add_string('I am very, very excited about this!')

            mystery = TextModel('mystery')
            mystery.add_string('Is he interested? No, but I am.')
            mystery.classify(source1, source2)

def run_tests():
            """ your docstring goes here """
            source1 = TextModel('rowling')
            source1.add_file('rowling_source_text.txt')

            source2 = TextModel('shakespeare')
            source2.add_file('shakespeare_source_text.txt')

            new1 = TextModel('hamlet')
            new1.add_file('hamlet_summary_text.txt')
            new1.classify(source1, source2)

            new2 = TextModel('montana1948')
            new2.add_file('montana1948_text.txt')
            new2.classify(source1, source2)

            new3 = TextModel('CNN')
            new3.add_file('CNN_text.txt')
            new3.classify(source1, source2)

            new4 = TextModel('capecod')
            new4.add_file('capecod_text.txt')
            new4.classify(source1, source2)
