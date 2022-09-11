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
# [4.4. break 文と continue 文とループの else 節](https://docs.python.org/ja/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
## break
最も内側の`for` または `while`ループを中断する  
ネストされた多重ループの場合、外側のループは続行される
## else
`else`と同じインデントの`for`ループが`break`されずに正常終了したら実行される
ループ途中で`break`されたら実行されない
try-elseみたいな感じ
```
for i in [1, 2, 3]:
    for j in [10, 20, 30]:
        print(i, j)
        if i == 2 and j == 20:
            print("break")
            break
    else:
        print("in else")

1 10
1 20
1 30
in else
2 10
2 20
break
3 10
3 20
3 30
in else
```
## continue
ループの次のイテレーションを実行する
# [4.7. 関数を定義する](https://docs.python.org/ja/3/tutorial/controlflow.html#defining-functions)
## 関数外変数の参照
関数内で変数の参照をする場合、以下の順で参照すべき変数を検索する
1. 関数内のローカルシンボルテーブル（変数等が記憶される）を検索
2. 外側の関数のローカルシンボルテーブルを検索
3. グローバルなシンボルテーブルを検索
4. 組み込みの名前テーブルを検索
つまり、関数内では外側の関数の変数やグローバル変数に代入はできないが参照はできる
```
# aはadd関数の外で宣言しているがadd関数内で参照できる
>>> a = 10
>>> def add(n):
...     result = n + a
...     print(result)
...
>>> add(7)
17
```
## pythonの関数は「参照の値渡し」
一番上のリンクがわかりやすい  
要は参照値を値渡ししている
* [Pythonの引数の渡し方について解説（値渡し・参照渡し）](https://hosl.dev/python/pythonvaluereference/)
* [値渡しと参照渡しの違いを理解する](https://magazine.rubyist.net/articles/0032/0032-CallByValueAndCallByReference.html)
* [Pythonの関数が「値渡し」か「参照渡し」か](https://pythonmaniac.com/call-by-value-or-reference/)
```
# aとbには10を示す同じ参照値が入っている.当然idも同じ.
>>> a = 10
>>> b = a
>>> print(f"a:{a}, a_id:{id(a)}")
a:10, a_id:9789248
>>> print(f"b:{b}, b_id:{id(b)}")
b:10, b_id:9789248

# aに別オブジェクト50を代入すると、aは50を示す別の参照値を持つのでidも変わる
>>> a = 50
>>> print(f"a:{a}, a_id:{id(a)}")
a:50, a_id:9790528
# bは10の参照値を持ったままなので何も変わらない
>>> print(f"b:{b}, b_id:{id(b)}")
b:10, b_id:9789248

bにaと同じ参照値を渡してやるとbのidも変わる
>>> b = a
>>> print(f"a:{a}, a_id:{id(a)}")
a:50, a_id:9790528
>>> print(f"b:{b}, b_id:{id(b)}")
b:50, b_id:9790528
```
# [4.8. 関数定義についてもう少し](https://docs.python.org/ja/3/tutorial/controlflow.html#more-on-defining-functions)
> 引数の定義方法には 3 つの形式があり

デフォルト値のある引数、位置専用キーワード専用引数、可変長引数 である。

が、https://docs.python.org/ja/3/glossary.html#term-parameter や [Qiita](https://qiita.com/raviqqe/items/ee2bcb6bef86502f8cc6#python-3%E3%81%A7%E3%81%AE%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E3%81%82%E3%82%8B%E3%81%84%E3%81%AF%E3%81%9D%E3%81%AE%E5%AE%A3%E8%A8%80%E3%81%AE%E6%96%B9%E6%B3%95)を確認し、  
5種類、6種類と考える方が良い。
# [5.1. リスト型についてもう少し](https://docs.python.org/ja/3/tutorial/datastructures.html#more-on-lists)
`insert`, `remove`, `sort` などのリストを操作する一部メソッドは `None` を返す。 
