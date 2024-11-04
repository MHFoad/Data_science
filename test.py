import re
def integers_in_brackets(s:str):
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    matches=re.findall(pattern, s)
    result=[int(match) for match in matches]
    return result
text= " afd [1asd1] [12 ] [a34] [ -43 ]tt [+12]xxx"
print (integers_in_brackets(text))