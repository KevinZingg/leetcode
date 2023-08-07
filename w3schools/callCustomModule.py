import mymodule
from mymodule import person1
import platform

bruh = mymodule.greeting("Kevin")

x = platform.system()
y = dir(platform)

print(x)
print(y)
print(person1["age"])
print(person1)
