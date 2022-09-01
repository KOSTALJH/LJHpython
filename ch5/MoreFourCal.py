from ch5 import FourCal

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result