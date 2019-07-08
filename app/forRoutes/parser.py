def parser(lst):
    list_ans = []
    for line in lst:
        line_0 = ''
        for i in range(len(line)):
            if line[i] == '>':
                line_0 += '&gt'
            elif line[i] == '<':
                line_0 += '&lt'
            else:
                line_0 += line[i]
        list_ans.append(line_0)
    return list_ans
    