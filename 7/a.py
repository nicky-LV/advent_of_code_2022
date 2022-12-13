def solution():
    current_dir = "/"
    dir_hierarchy = {'/': []}
    dir_sizes = {'/': 0}
    output = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')

            # command
            if line.split(" ")[0] == "$":
                cmd = line.split(" ")[1]

                # cd into dir
                if cmd == 'cd':
                    subdir = line.split(" ")[2]

                    if subdir == '..':
                        current_dir = current_dir[:current_dir.rfind('/')]

                    elif subdir == '/':
                        current_dir = '/'

                    else:
                        current_dir = current_dir + f'/{subdir}' if current_dir != '/' else f'/{subdir}'

            else:
                # list file or dirs
                filetype = line.split(" ")[0]

                if filetype == "dir":
                    dirname = current_dir + f'/{line.split(" ")[1]}' if current_dir != '/' else f'/{line.split(" ")[1]}'
                    dir_sizes[dirname] = 0
                    dir_hierarchy[dirname] = []

                    try:
                        dir_hierarchy[current_dir].append(dirname)

                    except KeyError:
                        dir_hierarchy[current_dir] = [dirname]

                else:
                    # list files
                    filesize = int(line.split(" ")[0])

                    dir_sizes[current_dir] += filesize

    for parent_dir in dir_hierarchy.keys():
        child_dirs = dir_hierarchy[parent_dir]

        while child_dirs:
            child_dir = child_dirs.pop(0)
            dir_sizes[parent_dir] += dir_sizes[child_dir]
            child_dirs.extend(dir_hierarchy[child_dir])

        if dir_sizes[parent_dir] <= 100000:
            output += dir_sizes[parent_dir]

    return output

print(solution())
