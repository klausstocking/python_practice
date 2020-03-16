#======================將模組架構為套件,並配置__init__.py===================================

from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
