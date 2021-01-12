
# A class to simulate a directory in the system
class Folder:
    def __init__(self, name):
        self.name = name
    subFolders = []
    parent = ""
    name = ""

 
"""
simulate the following directory in system
         |--def -- ghi
    abc--|--klm
         |--gh
    
    tmt--|
"""
root = Folder("mycd")
p1 = Folder("abc")
p1.parent = root
root.subFolders.append(p1)
p2 = Folder("def")
p2.parent = p1
p1.subFolders.append(p2)
p3 = Folder("klm")
p3.parent = p1
p1.subFolders.append(p3)
p4 = Folder("gh")
p1.subFolders.append(p4)
p4.parent = p1
p5 = Folder("ghi")
p5.parent = p2
p2.subFolders.append(p5)


def solution(current_directory, new_directory):
    # check if the input is valid
    if new_directory is None or new_directory == "":
        return ""
    folders = current_directory.split("/")
    directories = []
    path = root
    # move the path's pointer to the current directory
    for x in folders:
        if x == "":
            continue
        for y in path.subFolders:
            if y.name == x:
                path = y
                directories.append(y.name)
                break
    # remove duplicate slashes
    idx = 0
    while idx < len(new_directory):
        if idx - 1 >= 0 and new_directory[idx - 1] == '/' and new_directory[idx] == '/':
            new_directory = new_directory[:idx] + new_directory[idx + 1:]
        else:
            idx += 1
    # check if the new directory is an absolute path
    if new_directory[0] == '/':
        new_directory = new_directory[1:]
        folders = new_directory.split("/")
        directories = []
    else:
        folders = new_directory.split("/")
    # traverse the folders
    for i in folders:
        if len(i) == 0:
            continue
        if i == ".":
            continue
        elif i == "..":
            if path.parent is not None:
                path = path.parent
            if len(directories) > 0:
                directories.pop(len(directories) - 1)
        else:
            flag = True
            for p in path.subFolders:
                if p.name == i:
                    directories.append(p.name)
                    path = p
                    flag = False
                    break
            if flag:
                return "No such file or directory"
    # construct the result
    res = "/"
    for i in range(len(directories)):
        curr = directories[i]
        if i == 0:
            res += curr
        else:
            res += "/" + curr

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
