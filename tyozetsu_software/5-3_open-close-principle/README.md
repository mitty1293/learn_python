# 5-3_open-close-principle
5-3 開放閉鎖原則 に関するコードのディレクトリ
## ファイル構成
- `fizzbuzz_core.py`
    - 本質, 抽象モデルを表す.
        - 整数`n`を入力すると, 文字列`carry`を返す.
        - 整数と文字列に関するルールは`list`の要素として複数定義できる.
        - `match`にてルールを満たすか判定され, 満たしたときには`apply`で何かしらの操作が行われる.
        - `carry`は独立しておらず, 複数ルール間で共有され, `apply`での操作が累積される.
- `fizzbuzz_spec.py`
    - 仕様を表す.
        - 特定の数`base`の倍数かどうか判定する`match`
        - `carry`に任意の文字列`replacement`を結合する`apply`
        - 最終的に`carry`に何も操作が行われていない場合のルール
- `fizzbuzz.py`
    - 実際に使ってみるコード.
    - `python fizzbuzz.py`
## メモ
- ルール（約数か判定, 3倍か判定, etc）を追加したい場合, 以下のみ行えば他コードを書き直さなくて良い.
    - `fizzbuzz_spec.py`に`match`と`apply`を持つルールclassを追加
    - `fizzbuzz.py`の`NumberConverter`の引数を追加
    - 本質である`fizzbuzz_core.py`は触る必要がない
- つまり拡張はしやすく（open）, 変更しなくて良い（close）な設計となる.
## 参考リンク
- https://docs.python.org/ja/3/library/abc.html
- https://zenn.dev/plhr7/articles/36ddd240ccbb97
- https://maasaablog.com/development/backend/python/3923/
- https://hawksnowlog.blogspot.com/2021/05/python-interface-with-abc.html