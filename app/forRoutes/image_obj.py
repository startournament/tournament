from Constellation.dictionary import lat_rus_dict, dict_constell, rus_lat_dict, dictionary, messier_dict

def Image_obj(obj):
    if obj in lat_rus_dict:
        return [lat_rus_dict[obj]+' ('+obj+')']+['<a href="/image/'+rus_lat_dict[el]+'">'+el+'</a> ' for el in dict_constell[lat_rus_dict[obj]]]
    elif obj in dictionary['messier']:
        x = int(obj[1:]) + 1
        y = int(obj[1:]) - 1
        if x == 111:
            x = 1
        if y == 0:
            y = 110
        list_ans = ['<p><table class="Table"><tr><td>Назвние:</td><td>'+messier_dict[obj]['name']+'</td></tr><tr><td>Созвездие: </td><td>'+messier_dict[obj]['constellation']+'</td></tr><tr><td>Тип: </td><td>'+messier_dict[obj]['type']+'</td></tr><tr><td>Расстояние: </td><td>'+messier_dict[obj]['distance']+'</td></tr><tr><td>Звездная величина: </td><td>'+messier_dict[obj]['magnitude']+'</td></tr></table></p>'+'<a href="/image/messier/" class="button_submit">Вернуться к таблице</a>']
        return [obj] + ['<br><a href="/image/M' + str(y) + '" class="button_submit">Предыдущий</a> <a href="/image/M' + str(x) + '" class="button_submit">Следующий</a>'] + list_ans
    return [obj]
