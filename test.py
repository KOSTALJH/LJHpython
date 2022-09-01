from ch5.Calculator import Calculator as Cal
from ch5.MoreFourCal import MoreFourCal
from ch5.SefeFourCal import SafeFourCal

cal1 = SafeFourCal(4,2)
cal2 = MoreFourCal()
cal3 = MoreFourCal(1)


print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
print(cal1.pow())