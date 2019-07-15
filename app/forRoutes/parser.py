translate = {'>': '&gt', '<': '&lt', 'ё': 'е'}

def parser(lst):
    list_ans = []
    for line in lst:
        line_0 = ''
        line = line.title()
        for i in range(len(line)):
            if line[i] in translate:
                line_0 += translate[line[i]]
            else:
                line_0 += line[i]
        list_ans.append(line_0)
    return list_ans
    