#!/usr/bin/env python3

def file_extensions(filename):
    no_extension_files = []
    extension_dict = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if '.' in line:
                name, extension = line.rsplit('.', 1)
                if extension not in extension_dict:
                    extension_dict[extension] = []
                extension_dict[extension].append(line)
            else:
                no_extension_files.append(line)

    return (no_extension_files, extension_dict)

def main():
    no_extension_files, extension_dict = file_extensions("./filenames.txt")
    print(f"{len(no_extension_files)} files with no extension")
    for extension in sorted(extension_dict.keys()):
        print(f"{extension} {len(extension_dict[extension])}")

if __name__ == "__main__":
    main()
