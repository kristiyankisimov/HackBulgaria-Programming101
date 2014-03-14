def reduce_file_path(path):
    splitted_path = path.split("/")
    new_path = []
    for item in splitted_path:
        if item != '' and item != '.' and item != '..':
            new_path.append(item)
        elif item == '..' and new_path != []:
            new_path.pop()
    return "/" + "/".join(new_path)