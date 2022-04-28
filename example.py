'''
Autor: Sakurag1_LSJ
LastEditors: Sakurag1_LSJ
'''
'''
Autor: Sakurag1_LSJ
LastEditors: Sakurag1_LSJ
'''
from utils.cos_utils import content_upload
import os

# 传入的可能是文件地址，也可能是序列，判断是否为文件
# 输入由两部分组成 taskID;(seq|file_path) 使用;连接
s = input()
taskID,seqOrFile = s.split(';')
if os.path.exists(seqOrFile):
    pass

# do something
# 保存结果
result = []

# 上传结果并打印上传文件在oss上的地址(返回给java后端)
content_upload('%s.suffix'%taskID,result)