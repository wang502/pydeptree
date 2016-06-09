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
                if cur.replace(self.dir, "") not in self.file_funcs:
                    self.file_funcs[cur.replace(self.dir, "")] = []
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

                    """ extract function name """
                    func_name = _extract_func_name(line)
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
                    if line.find("(") != -1 and line.find(")") != -1:
                        """extract function name"""
                        func_name = _extract_func_name(line)
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
                        f = func(func_name)
                        """ extract arguments of function """
                        args = _extract_args(line)
                        f.args = args
                        cur_func = f

                        func_cross_line = True

                # class
                elif re.search(r"\s*class .+:", line):
                    cur_class = self.add_class(cur_class, file_dir)
                    class_name = _extract_class_name(line)
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
            fp.close()


    def add_class(self, cur_class, file_dir):
        if cur_class != None:
            if file_dir.replace(self.dir, "") not in self.file_funcs:
                self.file_funcs[file_dir.replace(self.dir, "")] = [cur_class]
            else:
                self.file_funcs[file_dir.replace(self.dir, "")].append(cur_class)
        return None

    # show the skelton of the project
    def show(self):
        s = []
        num_slash = 1
        strs = ""

        strs += self.dir.split('/')[-1] + "\n"
        strs += " "*num_slash*4
        strs += "|\n"

        for f in listdir(self.dir):
            s.append((join(self.dir, f), 1))

            # DFS to visit every file and chile folder
        while not len(s) == 0:
            cur = s.pop()
            depth = cur[1]
            if isfile(cur[0]) and is_py(cur[0]):
                strs += " "*depth*4
                strs += "+-- " + cur[0].split('/')[-1] + "\n"
                items = self.file_funcs[cur[0].replace(self.dir, "")]
                for item in items:
                    strs += " "*depth*5
                    strs += " "
                    if item.type == "func":
                        strs += "|-- " + str(item)
                    else:
                        strs += "|-- class " + item.name + "\n"
                        for func in item.funcs:
                            strs += " "*(depth*7)
                            strs += str(func)
            elif isfile(cur[0]) or re.search('.git$', cur[0]):
                pass
            else:
                strs += " "*depth*4
                strs += "+-- "
                name = cur[0].split('/')[-1] + "/"
                strs += name + "\n"
                for f in listdir(cur[0]):
                    s.append((join(cur[0], f), cur[1]+1))
        print strs

if __name__ == "__main__":

    # unit test for is_py()
    #print is_py("utils.py")
    #print is_py("utilespy")
    #print is_py("filename")

    # unit test for Dir()
    d = Dir("/Users/Xiaohui/Desktop/contribution/Toptal-API")
    d.show()
