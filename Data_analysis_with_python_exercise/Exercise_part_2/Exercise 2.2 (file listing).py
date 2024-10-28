import re
def file_listing(given_filename):
    pattern = r".*?\s*(\d+)\s*(\w{3})\s*(\d+)\s*(\d+):(\d+)(.*)"
    with open (given_filename) as file:
        match=re.findall(pattern,file.read())
        return[(int(size), month, int(day), int(hour), int(minute), filename) for size, month, day, hour, minute, filename in match]


c=file_listing("C:/Users/Foad/Python_exercise_for _data_analysis/Data_analysis_with_python_exercise/Exercise_part_2/listing.txt")
print(c)