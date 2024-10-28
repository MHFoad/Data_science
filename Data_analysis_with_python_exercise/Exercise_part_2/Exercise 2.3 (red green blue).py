import re
def red_green_blue(given_filename):
    pattern=r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n"
    with open (given_filename) as file:
        match= re.findall(pattern,file.read())
        return ["{}\t{}\t{}\t{}".format(r,g,b,name) for r,g,b,name in match ]

result= red_green_blue("./rgb.txt")
for item in result:
    print(item)