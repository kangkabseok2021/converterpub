class HelloWorld:
    def __init__(self) -> None:
        self._msg = "hello "

    def hello(self) -> str:
        return self._msg + "hello"

    def world(self) -> str:
        return self._msg + "world"

    def add(self, x: int, y: int) -> int:
        print(self._msg)  # added to avert pylint error
        return x + y

    def __repr__(self) -> str:
        return "HelloWorld()"
