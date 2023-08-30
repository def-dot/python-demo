import time
import xlrd
import os
import pandas as pd

try:
    basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, "test.xls")
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    print(df)
    print('hello world')
except Exception as e:
    print(str(e))
while True:
    time.sleep(30)
