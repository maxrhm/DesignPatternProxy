import abc 

 

class calculatorBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass
class NumberMultiplier(calculatorBase):
    def calculate(self):
        number = 1+1
        return number

 


class NumberMultiplierProxy(calculatorBase):
    __realNumberMultiplier = None
    def calculate(self):
        if self.__realNumberMultiplier == None:
            self.__realNumberMultiplier = NumberMultiplier()
            self.__cachedValue = NumberMultiplier.calculate(self.__realNumberMultiplier)
            return self.__cachedValue

 

test = NumberMultiplierProxy()
print(test.calculate())