from py2neo import Graph,Node,Relationship
from sklearn.externals import joblib
from creat_classify_model import chinese_tokenizer
import tflearn
import numpy as np
from pyhanlp import *
def chinese_tokenizer(documents):
    """
    把中文文本转为词序列
    """
    CRFnewSegment = HanLP.newSegment("crf")
    for document in documents:
        words=[]
        # 分词
        seged=CRFnewSegment.seg(document)
        for s in seged:
            words.append(s.word)
        yield words
class do_qa():
    CRFnewSegment = HanLP.newSegment("crf")
    graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    search_sql=[
        "match (n:Weapon{name:'rweapon'}) return n.射程",
        "match (w{name:'rweapon'})-[:`产国`]-(n) return n.name",
        "match (n:Weapon{name:'rweapon'}) return n.`乘员与载员`",
        "match (a)-[r:研发单位]->(x) where a.name='rweapon' return x.name",
        "match (a)-[r:制造单位]->(x) where a.name='rweapon' return x.name",
        "match (a)-[r:位于]->(x) where a.name='roran' return x.name",



    ]

    def classify(self,question):

        have_seg = self.CRFnewSegment.seg(question)
        for i in have_seg:
            if i.nature.toString() == 'weapon':
                question=question.replace(i.word,'weapon')
                question = question.replace(" ", '')
        toclassify=[]
        toclassify.append(question)
        vp = tflearn.data_utils.VocabularyProcessor.restore('vocab.pickle')  # 加载词汇表模型
        toclassify = vp.transform(toclassify)
        toclassify = np.array(list(toclassify))
        clf = joblib.load("svm_model.m")
        classify=clf.predict(toclassify )
        #print(classify)
        return classify[0]
    def get_answers(self,question):

        if self.classify(question)==0:
            self.answer_0(question)
        if self.classify(question) == 1:
            self.answer_1(question)


    def answer_0(self,question):
        have_seg = self.CRFnewSegment.seg(question)
        weapon=""
        for i in have_seg:
            if i.nature.toString() == 'weapon':
                print(i.word)
                weapon=i.word
        sql=self.search_sql[0].replace('rweapon',weapon)
        print(sql)
        answers=self.graph.run(sql).data()
        print(answers)

    def answer_1(self, question):
        have_seg = self.CRFnewSegment.seg(question)
        weapon = ""
        for i in have_seg:
            if i.nature.toString() == 'weapon':
                print(i.word)
                weapon = i.word
        sql = self.search_sql[1].replace('rweapon', weapon)

        print(sql)
        answers = self.graph.run(sql).data()
        print(answers)
    def answer_2(self,question):
        have_seg = self.CRFnewSegment.seg(question)
        weapon = ""
        for i in have_seg:
            if i.nature.toString() == 'weapon':
                print(i.word)
                weapon = i.word
        sql = self.search_sql[2].replace('rweapon', weapon)
        print(sql)
        answers = self.graph.run(sql).data()
        print(answers)

do=do_qa()
do.get_answers("四式203毫米重火箭是哪个国家生产的")



