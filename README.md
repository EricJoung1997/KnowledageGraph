# KnowledageGraph
- 使用Neo4j数据库的小型知识图谱测试
- 配置：Neo4j 4.1 + Python3.6
- 文章用唯一编号DOI表示，每个DOI有S、A、O、Year四个属性，S、A、O、Year分别作为节点建立，关系用Subject、Action、Object、Year表示。
每输入一条数据，分别为其创建DOI，Subject，Action，Object和Year的节点和彼此的关系，遍历所有数据后删除重复节点。最后建立有效节点5027个，关系共计10436条。部分网络图见
“可视化_知识基因图谱.svg”文件
