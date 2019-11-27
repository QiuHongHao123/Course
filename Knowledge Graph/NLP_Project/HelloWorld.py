from pyhanlp import *
from typing import List
import re


class entity_extractor():

    train_data=[]
    filename=""

    def __init__(self,filename):
        self.filename=filename
    def loadfile(self):
        f=open(self.filename,encoding='UTF-8')
        content=f.readline()
        while content:
            content=re.split('。',content)
            self.train_data+=content
            content = f.readline()

        return 0
    def do(self):
        data=self.train_data
        print(data)
        for line in data:
            # 依存句法分析
            sentence = HanLP.parseDependency(line)
            word_array = sentence.getWordArray()
            for word in word_array:
                print("%s --(%s)--> %s->%s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA,word.CPOSTAG))
                if word.DEPREL=="核心关系":
                    #核心谓语
                    print(word.LEMMA)

                    for word1 in word_array:      #找谓语
                        if word1.HEAD==word.HEAD and word1.DEPREL=="动宾关系":
                            print(word1.LEMMA)





extractor=entity_extractor("hello.txt")
extractor.loadfile()
extractor.do()


