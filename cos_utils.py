'''
Autor: Sakurag1_LSJ
LastEditors: Sakurag1_LSJ
'''
# -*- coding=utf-8
from ast import arg
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from datetime import datetime

secret_id = 'AKIDWrxoQnumPp0wd4GCsJUP5Wiwve8MK3Xl'
secret_key = '1mHXXHl0zjETTDixxnOkriJflcDYfW7T'
region = 'ap-chongqing'
token = None
scheme = 'http'
bucket = 'srf-web-1305632823'

config = CosConfig(Region=region, SecretId=secret_id,
                   SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)


def add_date(file_name):
    """
    文件前增加时间戳
    """
    file_name = datetime.strftime(datetime.today(), '%Y-%m-%d') + '/'+file_name
    return file_name


def simple_upload(file_name, file_path):
    """
    文件流 简单上传
    file_path: 上传文件在本地存储的路径
    key: 上传文件在cos上存储的名称
    """
    file_name = add_date(file_name)
    with open(file_path, 'rb') as fp:
        response = client.put_object(
            Bucket=bucket,
            Body=fp,
            Key=file_name,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
    print(file_name)


def content_upload(file_name, content):
    """
    字节流 简单上传
    file_name: 上传文件在cos上存储的名称
    content: 上传文件的内容，二进制形式
    """
    file_name = add_date(file_name)
    response = client.put_object(
        Bucket=bucket,
        Body=content,
        Key=file_name
    )
    print(file_name)


def local_upload(file_name, file_path):
    """
    本地路径 简单上传
    file_path: 上传文件的本地路径
    file_name: 上传文件在cos上存储的名称
    """
    file_name = add_date(file_name)
    response = client.put_object_from_local_file(
        Bucket=bucket,
        LocalFilePath=file_path,
        Key=file_name,
    )
    print(file_name)


def http_upload(file_name, content, content_type='text/html; charset=utf-8'):
    """
    设置 HTTP 头部 简单上传
    file_name: 上传文件在cos上的文件名称
    content: 上传文件的内容，二进制形式
    content_type: 上传文件的文件类型(HTTP) 默认：text/html; charset=utf-8
    """
    file_name = add_date(file_name)
    response = client.put_object(
        Bucket=bucket,
        Body=content,
        Key=file_name,
        ContentType=content_type
    )
    print(file_name)
