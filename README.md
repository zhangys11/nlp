# Collection of NLP related codes and notebooks

## 1. 爬虫

Web Crawler.ipynb

## 2. 数据预处理

合并多个来源的数据。  
Preprocessing.ipynb

## 3. 分词

Word Segmentation.ipynb

## 4. 文本向量化

TF-IDF.ipynb
Bag-of-Words and N-gram.ipynb

## 5. 主题模型

Topic Models.ipynb    
Topic Models - Food Safety.ipynb

## 6. 文本分类

Text Classification.ipynb 食品添加剂案例  
Text Classification - Drug Fact Sheets.ipynb

## 7. BERT预训练模型

BERT.ipynb squad QA finetune案例   

## 8. GPT模型

GPT.ipynb 英文、中文预训练模型；Flask应用     

# 案例研究：食品添加剂

聚焦食品中有害化学物质的检验，包括农残、抗生素、霉菌毒素、食品添加剂等。
通过实时文本挖掘构建食品和有害化学物的知识图谱，并基于Force-directed graph提供交互式可视化。

<img src='case_study\food_additives\design.png'>

相关材料：/case_study/food_additive/  TODO:数据为2020年之前，需更新。  
文本分类（判定抓取的文本是否食品安全主题相关）：Text Classification.ipynb  TODO: use BERT finetuned model   
语义关系提取：http://spacs.brahma.pub/association/   
可视化：http://spacs.brahma.pub/v/force/ 

Contributions：  
一个自动定时更新的食品添加剂主题语料库；
<img src='case_study\food_additives\text_corpus.png'>

结构化的食品添加剂知识图谱管理系统；
<img src='case_study\food_additives\knowledge_graph.png'>

基于Force-directed graph的交互式可视化工具。
<img src='case_study\food_additives\fdg.gif'>

