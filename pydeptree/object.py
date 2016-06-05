"""
pydeptree

object.py

-- represents a python class object implementation --

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""

class func():
    def __init__(self, name):
        self.name = name
        self.args = []

    def add_arg(self, arg):
        self.args.append(arg)

    def __str__(self):
        s = self.name + "("
        for arg in self.args:
            s += arg + ","
        s[len(s)-1] = ")"
        return s

class object():

    def __init__(self, name):
        self.name = name
        self.funcs = []

    def add_func(self, func):
        self.funcs.append(func)

    def __str__(self):
        s = "class " + self.name + "()\n"
        for func in self.funcs:
            s += " -- " + func
        return s
