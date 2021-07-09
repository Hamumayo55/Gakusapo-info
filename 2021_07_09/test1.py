# コード例1: test1.py
import re
filname = 'iris.data'

pattern = r'(^\d+\.\d+),.+'

data = []
with open(filname, 'r') as fh:
    for line in fh:
        line = line.rstrip()
        result = re.match(pattern, line) #patternにマッチする場所を抽出。
        if result: #matchの結果がNoneではなかったらリストに追加する
            value = result.group(1) #マッチした1つ目の文字列を抽出。
            data.append(value)

print(data)
