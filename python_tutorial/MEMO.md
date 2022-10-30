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
# [5.1.3. リストの内包表記](https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions)
 式、for 句、0個以上の for か if 句で構成される。  
 リスト内包表記の実行結果は、 for と if 句のコンテキスト中で式を評価した結果からなる新しいリストである。  
（よりわかりやすくいうなら、イテラブルオブジェクトの各要素を任意の変数名で取り出し式で評価、その結果を要素とする新たなリスト）
 
 ## 基本
`[式 for 任意の変数名 in イテラブルオブジェクト]`
```
>>> a = [x * 2 for x in range(3)]
>>> a
[0, 2, 4]
 ```
 ## 条件式がTrueとなるイテラブルオブジェクトのみを式で評価する
`[式 for 任意の変数名 in イテラブルオブジェクト if 条件式]`
```
>>> a = [x * 2 for x in range(10) if 5 < x]
>>> a
[12, 14, 16, 18]
 ```
# [5.3. タプルとシーケンス](https://docs.python.org/ja/3/tutorial/datastructures.html#tuples-and-sequences)
タプルはイミュータブル（不変）であるが、要素にリストのようなミュータブル（可変）な型を含めることは可能。
```
>>> a = ([1, 2, 3], "hello")
>>> a[0]
[1, 2, 3]
>>> a[1]
'hello'
>>> a[0][1]
2
>>> a[0][1] = 4
>>> a
([1, 4, 3], 'hello')
>>> a[0] = [4, 5, 6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
# [5.5. 辞書型 (dictionary)](https://docs.python.org/ja/3/tutorial/datastructures.html#dictionaries)
## リスト
```
>>> list = [1, 2, 3]
>>> list[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> list[3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```
## 辞書
```
>>> dict = {"a":1, "b":2}
>>> dict["c"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
>>> dict["c"] = 3
>>> dict
{'a': 1, 'b': 2, 'c': 3}
```
# [5.6. ループのテクニック](https://docs.python.org/ja/3/tutorial/datastructures.html#looping-techniques)
## 辞書
```
>>> dict = {"key1": "value1", "key2": "value2"}
>>> for x in dict:
...     print(x)
...
key1
key2
>>> for x in dict.keys():
...     print(x)
...
key1
key2
>>> for x in dict.values():
...     print(x)
...
value1
value2
>>> for x, y in dict.items():
...     print(x, y)
...
key1 value1
key2 value2
```
## シーケンス
```
>>> for i, v in enumerate(["v0", "v1", "v2"]):
...     print(i, v)
...
0 v0
1 v1
2 v2
```
## zip
```
>>> list1 = ["L11", "L12", "L13"]
>>> list2 = ["L21", "L22", "L23"]
>>> for l1, l2 in zip(list1, list1):
...     print(f"{l1}, {l2}")
...
L11, L11
L12, L12
L13, L13
```
# [6.1.2. モジュール検索パス](https://docs.python.org/ja/3/tutorial/modules.html#the-module-search-path)
例えば`import sample`とした場合、インタープリターは`sample`をどのように検索して見つけるのか。  
モジュールを検索する順番は以下。（`sys`は標準ライブラリの`sys`モジュール）
1. 組み込みモジュールに存在するか検索（`sys.builtin_module_names`にリストされている）
2. `sys.path` で指定されたディレクトリのリスト内で `sample.py` ファイルを検索。`sys.path` は次の場所で初期化されている。
    1. 入力されたスクリプトのあるディレクトリ (ファイルが指定されなかったときはカレントディレクトリ)。
    2. 環境変数PYTHONPATHで指定したディレクトリ(シェル変数の PATH と同じ構文)。
    3. インストールに依存するデフォルト (site モジュールによって処理される site-packages ディレクトリ等)。
# [7.2.1. ファイルオブジェクトのメソッド](https://docs.python.org/ja/3/tutorial/inputoutput.html#methods-of-file-objects)

`f=open("test.txt", "r", encoding="utf-8")` や `with open("test.txt", "r", encoding="utf-8") as f:`等でファイルオブジェクト`f`を生成したとする。
```
# ファイル内全部読み込み
f.read()

# 1行読み込み
f.readline()

# 複数行読み込み
for line in f:
    print(line)

# ファイル内容すべてをリスト形式で読み込み
f.readlines()
['line1\n', 'line2\n', 'line3\n', '\n']

list(f)
['line1\n', 'line2\n', 'line3\n', '\n']

# 書き込み
# 書き込まれた文字数を返す
f.write("line1\nline2\n")
12

# ファイルオブジェクト位置を示して変更する
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.tell()    # ファイルオブジェクトの位置を返すtell()
16
>>> f.seek(5)      # ファイルオブジェクトの位置を変更するseek()
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # ファイル終端から3バイト目に移動
13
>>> f.read(1)
b'd'
```
# [7.2.2. json による構造化されたデータの保存](https://docs.python.org/ja/3/tutorial/inputoutput.html#saving-structured-data-with-json)
* シリアライズ：pythonのデータ形式⇒文字列表現 に変換すること
* デシリアライズ：文字列表現⇒pythonのデータ形式 に変換すること
```
# pythonのデータ形式（list）をJSON形式の文字列表現に変換する
>>> import json
>>> x = [1, "test", "list"]
>>> json.dumps(x)
'[1, "test", "list"]'
```
# [8.3. 例外を処理する](https://docs.python.org/ja/3/tutorial/errors.html#handling-exceptions)
```
try:
    # まずtry節が実行される
    # 例外が発生すると以降の処理はスキップされる.
except:
    # 例外が発生すればexcept節が実行される.
else:
    # 例外が発生しなければ実行される.発生したらスキップされる.
finally:
    # 例外の発生有無にかかわらずfinally節があれば実行される
    # 例外がexceptで処理されなければfinally実行後に再送出される
    # finallyがbreak, continue, returnを実行する場合、例外は再送出されない
    # tryがbreak, continue, returnに達する場合、その直前にfinallyが実行される
    # finallyがreturnを含む場合、tryのreturnではなく、finallyのreturnが返る
```
# [9.2. Python のスコープと名前空間](https://docs.python.org/ja/3/tutorial/classes.html#python-scopes-and-namespaces)
[名前空間の参考](https://docs.pyq.jp/python/library/namespace.html), 
[スコープの参考](https://docs.pyq.jp/python/library/scope.html), 
[他参考](https://atmarkit.itmedia.co.jp/ait/articles/1612/09/news030_2.html), 
[他参考2](https://www.ceodata.com/python-namespaces-scope/)
## 名前空間
* 名前空間 (namespace) とは、名前からオブジェクトへの対応付け (mapping) のこと.
  * 例: 組込み名の集合 (abs() 等の関数や組込み例外名)、モジュール内のグローバルな名前、関数を呼び出したときのローカルな名前、オブジェクトの属性からなる集合
* 異なった名前空間にある名前の間には全く関係がない.2つのモジュールで同名の関数を定義できるが両者に関連はない.
* 違う表現をすると、他の名前（変数や関数の名前）と重複せず単一の名前として使うことができる範囲とも言える.
## スコープ
* スコープ (scope) とは、ある名前空間が修飾無しで直接アクセス（参照）できる名前の範囲のこと.（名前空間と被るがそこまで厳密に考えなくても良い）
* "直接アクセス可能" とは、修飾なしに (訳注: spam.egg ではなく単に egg のように) 名前を参照した際に、その名前空間から名前を見つけられること.
* 名前空間はオブジェクトと名前（変数・関数）の対応付けであり、スコープはそれが有効な範囲。
### スコープの種類
名前を参照する場合は以下の上から順に検索されていく.
1. ローカルスコープ
    * 現在実行しているコードを含む最小範囲のブロック
1. ローカルスコープを囲むスコープ（enclosing scope）
    * 関数定義内で関数定義している場合での外側関数のスコープ.
1. （モジュールレベルの）グローバルスコープ
    * モジュールのトップレベルで定義される名前はこのスコープに含まれる
1. 組み込み名前空間を表すスコープ
    * 組み込み関数やクラスを参照するための名前空間
## 代入
*  代入はデータをコピーしません.オブジェクトを名前に束縛するだけです.
# [9.3.2. クラスオブジェクト](https://docs.python.org/ja/3/tutorial/classes.html#class-objects)
* クラスオブジェクトは`属性参照（obj.name）`, `インスタンス生成`の2種類の操作を実行できる.
    * 有効な属性はクラスオブジェクト生成時にクラスの名前空間にあった名前すべて（`クラス変数等のデータ属性`, `クラスメソッド`, `__doc__`, 等）.
* クラスが `__init__()` メソッドを定義すると、新しく生成されたクラスインスタンスに対して `__init__()` が自動的に呼び出される.インスタンスオブジェクトを生成する際に特定の初期状態として生成することができる.
# [9.3.3. インスタンスオブジェクト](https://docs.python.org/ja/3/tutorial/classes.html#instance-objects)
* インスタンスオブジェクトは`属性参照（obj.name）`のみを実行できる.
    * 有効な属性は`データ属性（インスタンス変数, クラス変数等）`, `メソッド`の2種類.
# [9.3.4. メソッドオブジェクト](https://docs.python.org/ja/3/tutorial/classes.html#method-objects)
* メソッドとは、オブジェクトに "属している" 関数のこと
* メソッドの引数として、インスタンスオブジェクトが関数の第1引数として渡される.
```
# 以下のクラス定義がある場合
class MyClass:
    def f(self):
        return "HEllo World"

# インスタンス化
x = MyClass()

# fは引数無しで呼び出せる.
# 厳密には、x.f() と MyClass.f(x) は等価である.
x.f()
```
# [9.3.5. クラスとインスタンス変数](https://docs.python.org/ja/3/tutorial/classes.html#class-and-instance-variables)
* インスタンス変数: それぞれのインスタンスについて固有のデータのためのもの
* クラス変数: そのクラスのすべてのインスタンスによって共有される属性やメソッドのためのもの
# [9.4. いろいろな注意点](https://docs.python.org/ja/3/tutorial/classes.html#random-remarks)
* インスタンスとクラスの両方で同じ属性名が使用されている場合、属性検索はインスタンスが優先される.
# [9.5. 継承](https://docs.python.org/ja/3/tutorial/classes.html#inheritance)
* 継承先（サブクラス）で属性, メソッド参照する場合、継承先クラスで検索し見つからなければ基底クラスを検索、更に継承元クラスがあれば見つかるまで順に遡って検索していく.
* 継承に関する組み込み関数がある.
    * `isinstance(obj, classinfo)`
        * インスタンスの型を調べる.`obj.__class__`が`classinfo`やそのサブクラスのインスタンスであれば`True`.
    * `issubclass(class, classinfo)`
        * クラスの継承関係を調べる.`class`が`classinfo`のサブクラスであれば`True`.
# [9.8. イテレータ (iterator)](https://docs.python.org/ja/3/tutorial/classes.html#iterators)
## イテレータとは
`__iter__()`メソッド, `__next__()`メソッドを持っているオブジェクトのこと.
### `__iter__()`
* `オブジェクト.__iter__()` で呼び出す.
* オブジェクトからイテレータを作って返す.オブジェクトがイテレータだった場合はオブジェクトそのものを返す.
### `__next__()`
* `イテレータ.__next__()`で呼び出す.
* イテレータの要素を1つずつ取り出し、要素がなくなれば`StopIteration`例外を返す.
### 例
```
# listはイテレータではない(__next__を持っていない).
>>> list1 = [0, 1, 2]
>>> hasattr(list1, "__iter__")
True
>>> hasattr(list1, "__next__")
False

# オブジェクトからイテレータを返す組み込み関数 iter() を使ってイテレータ化する.
# イテレータ化されるので __next__() メソッドを持つ.
>>> it = iter(list1)
>>> hasattr(it, "__iter__")
True
>>> hasattr(it, "__next__")
True

# __next__()メソッドを呼び出す組み込み関数next()を使って要素を順に取り出す.
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
## `for`文の中身
`for`文は内部で以下の処理を行っている.
* 指定したオブジェクトに対して`iter()`を呼び出しイテレータが返される.
* 返されたイテレータに対して`next()`を呼び出し要素を順に取り出す.
* `StopIteration`例外が発生したらループ処理を終了する.
## イテレータを自作する
* `__next__()`, `__iter__()`を使えば自分でイテレータを作ることもできる.
* `__next__()`を持つオブジェクトを返す`__iter__()`を定義すれば良い.
* 実際に作成したものが https://github.com/mitty1293/learn_python/blob/main/python_tutorial/my_iterator.py
## 参考
https://1978works.com/2021/06/13/what-iterator-object-in-python-is-like/  
https://qiita.com/tchnkmr/items/e740173d7400f8672d75
# [9.9. ジェネレータ (generator)](https://docs.python.org/ja/3/tutorial/classes.html#generators)
* `yield()`を使ったジェネレータを用いてイテレータを作成できる.
* `__next__()`, `__iter__()`を用いた作成方法よりも定義がコンパクトで簡単.
# [10. 標準ライブラリミニツアー](https://docs.python.org/ja/3/tutorial/stdlib.html#brief-tour-of-the-standard-library)
## `os`モジュール
オペレーティングシステム関連の関数を提供する.
```
import os

# カレントディレクトリを取得
>>> os.getcwd()
'/home/mitty1293'

# ディレクトリの中身をリスト化
>>> os.listdir()
['.python_history', '.rustup', ...]
>>>
```
## `shutil`モジュール
ファイルやディレクトリの日常管理で使える高水準インターフェース.
```
>>> import shutil

# ファイルsrcをメタデータ（パーミッション等）を含まずdstとしてコピーする.
# dstにディレクトリを指定するとエラー（`IsADirectoryError`）.
>>> shutil.copyfile('src', 'dst')

# ファイルsrcをメタデータ（パーミッション等）を含まずdistとしてコピーする.
# dstにディレクトリを指定するとdst内にsrcと同じ名前のファイルを作成する.
>>> shutil.copy(src, dst)

# copyと同様の機能で、更にメタデータを含めてコピーする.
>>> shutil.copy2(src, dst)

# ファイル移動
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
## `glob`モジュール
```
import glob

# ディレクトリのワイルドカード検索からファイル一覧をリストで取得.
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```
## `sys`モジュール
* コマンドライン引数は`sys`モジュールの`argv`属性にリストで保存されている.
```
# args.py
import sys
print(sys.argv)

# CommandLine
$ python args.py arg1 arg2
['args.py', 'arg1', 'arg2']
```
* `sys.exit()`でスクリプトを終了させる.
## `re`モジュール
文字列処理のための正規表現を提供する.
## `math`モジュール
各数学関数を提供する.
```
import math

# 小数点以下を切り捨て
>>> math.floor(10.123)
10
# 正確には「引数以下の最大の整数」を返す
>>> math.floor(-10.123)
-11

# 小数点以下を切り上げ
>>> math.ceil(10.123)
11
# 正確には「引数以上の最小の整数」を返す
>>> math.ceil(-10.123)
-10
```
## `random`モジュール
擬似乱数を生成するモジュール
```
>>> import random

# 0以上stop未満の整数からランダムに選んで返す.rangeのランダム版.
>>> random.randrange(stop)
# start以上stop未満の整数でstepに当てはまる要素からランダムに選んで返す.rangeのランダム版.
>>> random.randrange(start, stop[, step])

# start以上stop以下の整数からランダムに選んで返す.
>>> random.randint(start, stop)

# シーケンスseqからk個を重複無しで抽出
>>> random.sample(seq, k)

# シーケンスseqからk個を重複有りで抽出
>>> random.choices

# シーケンスseqから1個を抽出
>>> random.choice(seq)
```
## データ圧縮モジュール
以下のようなモジュールでサポートされる.
zlib, gzip, bz2, lzma, zipfile, tarfile
## テスト
doctest, unittest
## メール関連モジュール
email, smtplib, poplib  
(mailという名前のライブラリは標準ライブラリには存在しない)
