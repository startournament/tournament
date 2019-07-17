translate = {'ОС': 'Остаток сверхновой', 'ШС': 'Шаровое скопление', "РС": "Рассеянное скопление", "РС + ДТ": "Рассеянное скопление с диффузной туманностью", "ПТ": "Планетарная туманность", "Галактика": "Галактика", "Дв. звезда WNC4": "Двойная звезда", 'ДТ': 'Диффузная туманность', 'Группа из 4 звёзд': 'Группа из 4 звёзд', 'включает Каустическую долину': 'включает Каустическую долину'}
messier_dict = {}
i = 0
with open("messier_table.txt", "r") as f_in, open('new_messier.py', 'w') as f_out:
    t = f_in.readline().rstrip().split(',')  
    while t != ['']:
        i += 1
        name = t[0]
        if t[0] == '':
            name = '-'
        Type = translate[t[1]]
        distance = t[2] + ' тыс. св. лет'
        magnitude = t[4] + '<sup>m</sup>'
        messier_dict['M' + str(i)] = {'name': name, 'type': Type, 'distance': distance, 'constellation': t[3], 'magnitude': magnitude}
        t = f_in.readline().rstrip().split(',')
    print('messier_dict =', messier_dict, file = f_out)
