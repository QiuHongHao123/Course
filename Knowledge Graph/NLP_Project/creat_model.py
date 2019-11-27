from py2neo import Graph,Node,Relationship
from pyhanlp import *
class creat_models():
    graph = Graph("http://localhost:7474",auth=("neo4j","123456"))
    def creat_weapon_dict(self):
        property_set=[]
        node_list=self.graph.run("match (x:Weapon) return x ").data()
        fn= open('weapon_name.txt','w',encoding='utf-8')
        fp= open('Property_name.txt','w',encoding='utf-8')
        for one in node_list:
            for k,v in one['x'].items():

                if(k=='name'):
                    v=v.replace(" ","")
                    fn.write(v+" "+"weapon"+" "+"200\n")
                else:
                    property_set.append(k)
        property_set=list(set(property_set))
        for p in property_set:
            p=p.replace(" ", '')
            fp.write(p+" "+"nz"+" "+"100\n")

    def creat_organization_dict(self):
        node_list = self.graph.run("match (x:单位) return x ").data()
        f = open('organization_name.txt', 'w', encoding='utf-8')
        for one in node_list:
            for k,v in one['x'].items():
                v=v.replace(" ", "")
                f.write(v+" "+"ni"+" "+"100\n")

    def creat_labels_dict(self):
        node_list = self.graph.run("match (x:label) return x ").data()
        f = open('labels_name.txt', 'w', encoding='utf-8')
        for one in node_list:
            for k, v in one['x'].items():
                v=v.replace(" ", "")
                f.write(v + " " + "nz" + " " + "100\n")
CRFnewSegment=HanLP.newSegment("crf")
tlist=CRFnewSegment.seg("“幻影”Ⅲ/5/50喷气战斗机的飞行速度是多少？")
for i in tlist:
    print(i.nature,i.word)
'''
cr=creat_models()
cr.creat_weapon_dict()
cr.creat_organization_dict()
cr.creat_labels_dict()
'''