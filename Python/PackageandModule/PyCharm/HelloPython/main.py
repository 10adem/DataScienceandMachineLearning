print("hello python")

from random import randint
# import ademmodule
from ademmodule import example_func
from AnimalPackage import info
from AnimalPackage.CatPackage import meow # sub package (alt paket)
import numpy

print(numpy.zeros((3,4)))

# ademmodule.example_func()
example_func()

info.info()
# meow.speak()

meow.test()
