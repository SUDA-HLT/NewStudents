# 命名实体识别

## 命名实体识别任务描述：
命名实体识别(Named Entity Recognition, NER)，主要任务是识别出文本中属于特定类别的词语并加以归类。
目前较为常见的处理方法是，将NER任务抽象为序列标注问题。

例：<br> 
首先定义一个标签集合：{B-PER，I-PER，I-PER，O}<br> 
给定文本序列：
>周杰伦的教育经历是怎么样的？

若当前任务为识别文本中的人名，则对应的标签序列为：
>B-PER I-PER I-PER O O O O O O O O O O O

归类时，将BII的组合归为同一类：人名（PER）


## 任务流程：
1. 学习条件随机场模型，理解训练过程；
2. 设计适合当前中文NER任务的特征模板，使用工具训练CRF模型；
3. 尝试调整参数、特征模板和标签集，提升模型性能。
4. 在指定训练集上训练模型，并计算出在测试集上的识别性能（实现评价工具为：准确率、召回率、F1值）

* 准确率(precision) = 正确分类的样本数 / 实际分类样本数
* 召回率(recall) = 正确分类的样本数 / 应有文本数
* F1 = precision * recall * 2 / (precision + recall)

## 数据说明
本次训练任务使用的是MSRA中文数据集，数据中包含三个实体类别：<br>
  |标签| LOC | ORG  | PER |<br>
	------------------------<br>
	|含义| 地名 |组织名|人名|<br>
	------------------------<br>

使用的标签集为：BIO模式（可尝试其它标签集）<br>

数据举例：字符\t标签
>   历	B-LOC<br>
		博	I-LOC<br>
		、	O<br>
		古	B-ORG<br>
		研	I-ORG<br>
		所	I-ORG<br>


## 工具使用
**CRF讲义：** http://hlt.suda.edu.cn/~zhli/teach/cip-2015-fall/11-global-linear-model/main.pdf<br>
**pycrfsuite安装：** pip install python-crfsuite<br>
**pycrfsuite教程：** https://github.com/txHe/UseOfPycrfsuite<br>
**深度学习模型：** http://120.132.13.131:8080/wiki/index.php/%E7%94%A8%E6%88%B7:Ethan_yys<br>


