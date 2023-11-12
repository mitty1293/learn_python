from abc import ABC, abstractmethod


# 各状態を示すSpeedMeterStateの具象からインスタンスを取り出すためだけのclass
# なのでstateパターン自体に影響するものではない.
class SingletonTrait:
    _instances = {}

    @classmethod
    def getInstance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonTrait, cls).__new__(cls)
        return cls._instances[cls]


class SpeedMeter:
    def __init__(self):
        self.speed = 0.0
        self.current_state = SafeState.getInstance()

    def set_speed(self, speed):
        self.speed = speed
        self.current_state = self.current_state.next_state(self.speed)

    def display(self):
        color = self.current_state.get_color()  # stateパターンで重要なのはここ
        return f"{self.speed:.2f} km/h {color}"


class SpeedMeterState(ABC):
    @abstractmethod
    def next_state(self, speed):
        pass

    @abstractmethod
    def get_color(self):
        pass


class SafeState(SpeedMeterState, SingletonTrait):
    def next_state(self, speed):
        return DangerState.getInstance() if speed > 100.0 else self

    def get_color(self):
        return "green"


class DangerState(SpeedMeterState, SingletonTrait):
    def next_state(self, speed):
        return SafeState.getInstance() if speed <= 80.0 else self

    def get_color(self):
        return "red"


# 使用例
speed_meter = SpeedMeter()
speed_meter.set_speed(75.0)
print(speed_meter.display())  # Output: 75.00 km/h green

speed_meter.set_speed(110.0)
print(speed_meter.display())  # Output: 110.00 km/h red
