from py2neo import Graph, Node, Relationship
# import pandas as pd
import csv
# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("http://localhost:7474", username="neo4j", password='12345678')
graph.delete_all() #清除neo4j中原有的结点等所有信息

with open(r'clean\Neo4j_Inputs(AND).csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data[1])
#['0', 'doi', 'Subject', 'Action', 'Object', 'Year']

for i  in  range(1,len(data)):   #循环建立节点
    node = Node('DOI',name = data[i][1],Subject= data[i][2],ObjectD = data[i][4],Action = data[i][3],year=data[i][5])
    relation = Node('ObjectD',name = data[i][4])
    relation1 = Node('Action',name = data[i][3])
    relation2 = Node('Subject',name = data[i][2])
    relation3 = Node('year',name = data[i][5])
    graph.create(node)
    graph.create(relation)
    graph.create(relation1)
    graph.create(relation2)
    graph.create(relation3)
    print('第{}条数据创建成功'.format(i))

#删除两两节点的重复节点
graph.run('MATCH (n:ObjectD) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
graph.run('MATCH (n:Action) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
graph.run('MATCH (n:Subject) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')
graph.run('MATCH (n:year) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node')

#建立对应关系
graph.run('MATCH (entity1:DOI) , (entity2:ObjectD{name:entity1.ObjectD}) CREATE (entity1)-[:Object]->(entity2)')
graph.run('MATCH (entity1:DOI) , (entity2:Action{name:entity1.Action}) CREATE (entity1)-[:Action]->(entity2)')
graph.run('MATCH (entity1:DOI) , (entity2:Subject{name:entity1.Subject}) CREATE (entity1)-[:Subject]->(entity2)')
graph.run('MATCH (entity1:DOI) , (entity2:year{name:entity1.year}) CREATE (entity1)-[:Year]->(entity2)')