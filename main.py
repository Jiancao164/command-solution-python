def solution(current_directory, new_directory):
    # check if the input is valid
    if new_directory is None or new_directory == "":
        return ""
    temp = ""
    # remove duplicate slashes
    for idx in range(0, len(new_directory)):
        if idx > 0 and new_directory[idx] == '/' and new_directory[idx - 1] == '/':
            continue
        temp += new_directory[idx]

    new_directory = temp
    new_directories = new_directory.split("/")

    # check if the new directory is valid
    for directory in new_directories:
        if len(directory) == 0:
            continue
        if directory == ".":
            continue
        if directory == "..":
            continue
        for c in directory:
            if '0' <= c <= '9':
                continue
            if 'a' <= c <= 'z':
                continue
            if "A" <= c <= 'Z':
                continue
            return "No such file or directory"

    directories = []

    new_directories = new_directory.split("/")
    # check if the new directory is an absolute path
    if new_directory[0] != '/':
        curr_directories = current_directory.split("/")
        for s in curr_directories:
            if len(s) == 0:
                continue
            directories.append(s)
    # parse directories
    for next_directory in new_directories:
        if len(next_directory) == 0:
            continue
        if next_directory == ".":
            continue
        elif next_directory == "..":
            if len(directories) > 0:
                directories.pop(len(directories) - 1)
        else:
            directories.append(next_directory)

    # construct the result from the list
    res = "/"
    for i in range(0, len(directories)):
        if i == 0:
            res += directories[i]
        else:
            res += "/" + directories[i]

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
