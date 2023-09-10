```
pwd
/workspaces/learn_python/tyozetsu_software/7-1_what_dependency_injection
python -m unittest discover -s ./tests
export PYTHONPATH=$PYTHONPATH:$(pwd)
python ./src/app.py 
```
* 実装、生成、使用 を分ける
    - 実装 ＝ 依存 する インスタンス は 外部 から 与え て もらう 前提 で 無責任 に 作る
    - 生成 ＝ 適切 な 依存 インスタンス を 取得 し て 注入 済み で 使用者 に 与える
    - 使用 ＝ 取得 または 与え られ た インスタンス は 完成 し て いる ので あと は 使う だけ
* 6-6のコードのままで、各種ルールをprint_rangeメソッド内で自力で生成する場合は各種ルール（具象のふるまい）に依存してしまっている.
* つまり各種ルールの変更にprint_rangeが影響を受ける
* 今回のように実装、生成、使用 を分けることで、使用時には各実装は気にせず、実装に変更があっても生成部分のみを修正すれば良くなる