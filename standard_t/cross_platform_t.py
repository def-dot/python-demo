"""跨平台测试"""


if __name__ == '__main__':
    import os

    # 创建目录
    os.mkdir('mydir')

    # 删除文件
    os.remove('myfile.txt')

    # 列出目录内容
    files = os.listdir('mydir')
