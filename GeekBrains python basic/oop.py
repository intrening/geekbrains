class Word:
    text = ''
    part = ''
    _gram_harakter = ''
    def __init__(self,text='',part=''):
        self.text = text
        self.part = part

class Noun(Word):
    pass
class Verb(Word):
    pass

class Sentence:
    content = []
    def __init__ (self):
        pass

    def show(self,*words):
        for word in words:
            self.content.append(word)
        
    def show_parts(self):
        for i in self.content:
            print (i._gram_harakter)

w1= Word ('идти', 'глагол')
w2= Word ('предмет', 'подлежащее')
s = Sentence()
s.show (w1,w2)
s.show_parts()