def Text(game):
    text = []
    with open("app/static/text/rulse_" + game + '.txt', "r", encoding = 'utf-8') as f_in:
        for line in f_in:
            text.append(line.rstrip())
    return text
