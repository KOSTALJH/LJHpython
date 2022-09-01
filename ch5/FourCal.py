class FourCal:
    
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def setdata(self, first:int, second:int):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
         result = self.first / self.second
         return result

