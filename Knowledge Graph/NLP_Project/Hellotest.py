from py2neo import Node,Relationship,Graph,NodeMatcher
from typing import List
import json
class insert():

    test_graph = Graph(
        "http://localhost:7474",
        username="neo4j",
        password="123456"
    )
    matcher = NodeMatcher(test_graph)
    '''
    节点创建函数
    '''
    def creat_node(self,kind="label",name=""):
        node = Node(kind, name=name)
        self.test_graph.create(node)


    '''
    向一个已有节点添加特性。若不存在该节点则将节点创建
    要求特性列表为二元组集合，其中二元组第一位为特性名第二位为特性值
    '''
    def add__feature(self,kind,name,feature_list:List):
        nodelist=self.matcher.match(kind,name=name)
        node=nodelist.first()
        if len(nodelist)==0:
            node=Node(kind,name=name)
            self.test_graph.create(node)
        for one_feature in feature_list:
            node[one_feature[0]]=one_feature[1]
        self.test_graph.push(node)
    '''
    关系添加函数。
    '''
    def add_relationship(self,node1_kind="label",node1_name="",node2_kind="label",node2_name="",relationship="no"):
        node1list=self.matcher.match(node1_kind,name=node1_name)
        node2list=self.matcher.match(node2_kind,name=node2_name)
        node1=node1list.first()
        node2=node2list.first()
        if len(node1list)==0:
                node1 = Node(node1_kind, name=node1_name)
                self.test_graph.create(node1)
        if len(node2list)==0:
                node2 = Node(node2_kind, name=node2_name)
                self.test_graph.create(node2)

        node1_call_node2 = Relationship(node1, relationship, node2)
        self.test_graph.create(node1_call_node2)

#读取数据
class load_data():
    insert=insert()
    data=""
    jdata=[]
    def __init__(self,file):
        self.data= open(file, 'r',encoding='utf-8')

    def tran_data(self):
        for line in self.data:
            one=json.loads(line)
            self.jdata.append(one)
    def insert_jdata(self):

        for one in self.jdata:
            name=""
            kind=""
            bkind=""
            nation=""
            location=""
            made_location=""
            feature_list=[]
            for k,v in one.items():
                if k=="名称":
                    name=v
                    feature_list.append([k, v])
                elif k=="产国":
                    nation=v
                    feature_list.append([k, v])
                elif k=="类型":
                    kind=v
                    feature_list.append([k, v])
                elif k=="大类":
                    bkind=v
                    feature_list.append([k, v])
                elif k=="研发单位":
                    location=v
                    feature_list.append([k, v])
                elif k==("制造厂"or "制造商"):
                    made_location=v
                    feature_list.append([k, v])
                elif k=="图片" or k=="_id":
                    continue
                else:
                    feature_list.append([k,v])

            print(name,kind,bkind,nation,location,feature_list)


            self.insert.add_relationship("Weapon", name, "国家", nation, "产国")
            self.insert.add_relationship("Weapon", name, "单位", location, "研发单位")
            self.insert.add_relationship("Weapon", name, "单位", made_location, "制造单位")
            self.insert.add_relationship("单位",location, "国家", nation, "位于")
            self.insert.add_relationship("单位", made_location, "国家", nation, "位于")
            self.insert.add_relationship("Weapon", name, "label",kind, "属于")
            self.insert.add_relationship("label", kind, "label",bkind, "属于")
            self.insert.add__feature("Weapon",name,feature_list)






test=load_data("military.json")
test.tran_data()
test.insert_jdata()




