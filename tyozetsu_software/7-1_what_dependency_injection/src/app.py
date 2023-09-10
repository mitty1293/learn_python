from src.fizzbuzz_app_factory import FizzBuzzAppFactory


class App:
    def main(self) -> None:
        factory = FizzBuzzAppFactory()
        printer = factory.create()
        printer.print_range(1, 100)


app = App()
app.main()
