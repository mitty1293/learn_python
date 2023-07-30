from fizzbuzz_core import NumberConverter
from fizzbuzz_spec import CyclicNumberRule, PassThroughRule

fizzbuzz = NumberConverter([
    CyclicNumberRule(3, "Fizz"),
    CyclicNumberRule(5, "Buzz"),
    PassThroughRule()
])

for i in range(1, 21):
    print(fizzbuzz.convert(i))
