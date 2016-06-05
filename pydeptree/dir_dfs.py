"""
pydeptree

dir_dfs.py

-- traverse the folder using DFS and visit every .py files --

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""

from os import listdir
from os.path import isfile, join
import re

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
        with open(file_dir) as fp:
            for line in fp:
                if re.search(r".def.+:", line):
                    print file_dir, line
                    if file_dir not in self.file_funcs:
                        self.file_funcs[file_dir] = [line]
                    else:
                        self.file_funcs[file_dir].append(line)
                elif re.search(r"^class.+:", line):


if __name__ == "__main__":

    # unit test for is_py()
    print is_py("utils.py")
    print is_py("utilespy")
    print is_py("filename")

    # unit test for Dir()
    d = Dir("/Users/Xiaohui/Desktop/contribution/Toptal-API")
    d.dir_dfs()
    for (k, v) in d.file_funcs.items():
        print k, v, "\n"
