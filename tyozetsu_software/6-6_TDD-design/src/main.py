import sys
import os


# 現在のスクリプトのディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))

# プロジェクトのルートディレクトリを取得
project_root = os.path.dirname(current_dir)

# プロジェクトのルートディレクトリをモジュールの検索パスに追加
sys.path.append(project_root)

from src.core.number_converter import NumberConverter
from src.spec.pass_through_rule import PassThroughRule
from src.spec.cyclic_number_rule import CyclicNumberRule


rule1 = CyclicNumberRule(3, "Fizz")
rule2 = CyclicNumberRule(5, "Buzz")
rule3 = PassThroughRule()
fizzbuzz = NumberConverter([rule1, rule2, rule3])

for i in range(0, 21):
    print(fizzbuzz.convert(i))
