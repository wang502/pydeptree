"""
pydeptree

Dir.py

-- A directory object that porcess all the .py file implementations within the current directory
-- traverse the folder using DFS and visit every .py files --

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""

from os import listdir
from os.path import isfile, join
import re
from Class import Class, func
from utils import _extract_func_name, _extract_class_name, _extract_args

# check if a file is python file
def is_py(filename):
    return True if re.search("\.py$", filename) != None else False

class Dir():
    """
        Dir() object represents a directory and its hierachy child file and child directories
    """
    def __init__(self, d):
        # parent directory to visit
        self.dir = d

        # key value pair for a specific file and its implemented functions
        self.file_funcs = {}
        self.dir_dfs()

    def dir_dfs(self):
        # array of all files
        files = []
        s = []
        for f in listdir(self.dir):
            s.append(join(self.dir, f))

        # DFS to visit every file and chile folder
        while not len(s) == 0:
            cur = s.pop()
            if isfile(cur) and is_py(cur):
                self.visit_file(cur)
            elif isfile(cur):
                pass
            else:
                for f in listdir(cur):
                    s.append(join(cur, f))

    def visit_file(self, file_dir):
        cur_class = None
        cur_func = None
        func_cross_line = False

        with open(file_dir) as fp:
            for line in fp:
                # independent function
                if re.match(r"^def .+:", line):
                    cur_class = self.add_class(cur_class, file_dir)

                    #print file_dir
                    #print line

                    """ extract function name """
                    func_name = _extract_func_name(line)
                    #print func_name
                    f = func(func_name)

                    """ extract arguments of function """
                    args = _extract_args(line)

                    f.args = args
                    if file_dir.replace(self.dir, "") not in self.file_funcs:
                        self.file_funcs[file_dir.replace(self.dir, "")] = [f]
                    else:
                        self.file_funcs[file_dir.replace(self.dir, "")].append(f)

                # function within a class or function with more indentations
                elif re.search(r"\s+def .+:", line):
                    #print file_dir
                    #print line

                    if line.find("(") != -1 and line.find(")") != -1:
                        """extract function name"""
                        func_name = _extract_func_name(line)
                        #print func_name
                        f = func(func_name)

                        """ extract arguments of function """
                        args = _extract_args(line)
                        f.args = args

                        if cur_class != None and line.find("self") != -1:
                            cur_class.add_func(f)

                    # function header that occupies at leaset 2 lines
                    elif line.find("(") != -1:
                        """extract function name"""
                        func_name = _extract_func_name(line)
                        #print func_name
                        f = func(func_name)
                        """ extract arguments of function """
                        args = _extract_args(line)
                        f.args = args
                        cur_func = f

                        func_cross_line = True

                # class
                elif re.search(r"\s*class .+:", line):
                    cur_class = self.add_class(cur_class, file_dir)

                    #print file_dir
                    #print line
                    class_name = _extract_class_name(line)
                    #print class_name
                    cur_class = Class(class_name)

                elif func_cross_line:
                    args = _extract_args(line)
                    if cur_func != None:
                        for arg in args:
                            cur_func.add_arg(arg)
                    if line.find(")") != -1:
                        func_cross_line = False
                        if cur_class != None and line.find("self") != -1:
                            cur_class.add_func(cur_func)
                        cur_func = None

    def add_class(self, cur_class, file_dir):
        if cur_class != None:
            if file_dir.replace(self.dir, "") not in self.file_funcs:
                self.file_funcs[file_dir.replace(self.dir, "")] = [cur_class]
            else:
                self.file_funcs[file_dir.replace(self.dir, "")].append(cur_class)
        return None

    def prettify_file_funcs(self):
        strs = self.dir + "\n"
        for (k, v) in self.file_funcs.items():
            # number of slashes denotes how far this dir is from home dir
            num_slash = len(k) - len(k.replace("/", ""))
            strs += " "*num_slash
            strs += "|\n"
            strs += " "*num_slash
            strs += "+-- "
            strs +=  k + "\n"
            for item in v:
                strs += " "*num_slash
                strs += "  "
                if item.type == "func":
                    strs += str(item)
                else:
                    strs += "class " + item.name + "\n"
                    for func in item.funcs:
                        strs += " "*(num_slash+6)
                        strs += str(func)
        print strs

if __name__ == "__main__":

    # unit test for is_py()
    #print is_py("utils.py")
    #print is_py("utilespy")
    #print is_py("filename")

    # unit test for Dir()
    d = Dir("/Users/Xiaohui/Desktop/contribution/Toptal-API")
    # d.dir_dfs()

    d.prettify_file_funcs()
