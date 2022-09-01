# [3.1.3 リスト型 (list)](https://docs.python.org/ja/3/tutorial/introduction.html#lists)
## スライス
リストはスライスができる
```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[0]
'a'
>>> letters[-2]
'f'
>>> letters[2:4]
['c', 'd']
```
スライスに代入できる
```
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:] = []
>>> letters
[]
```
