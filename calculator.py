import abc
import time

class calculatorBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass

class NumberMultiplier(calculatorBase):
    def calculate(self):
        result = 1
        i = 2
        while i <= 10:
            result = result * i
            time.sleep(1)
            i = i + 1 
        return result

class NumberMultiplierProxy(calculatorBase):
    __realNumberMultiplier = None
    def calculate(self):
        if self.__realNumberMultiplier == None:
            self.__realNumberMultiplier = NumberMultiplier()
            self.__cachedValue = NumberMultiplier.calculate(self.__realNumberMultiplier)
        return self.__cachedValue

test = NumberMultiplierProxy()
i = 0
while i < 10:
    print(test.calculate())
    i = i + 1