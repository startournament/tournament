from Constellation.dictionary import lat_rus_dict, dict_constell, rus_lat_dict, dictionary

def Image_obj(obj):
    if obj in lat_rus_dict:
        return [lat_rus_dict[obj]+' ('+obj+')']+['\n']+['<a href="/image/'+rus_lat_dict[el]+'">'+el+'</a>' for el in dict_constell[lat_rus_dict[obj]]]
    elif obj in dictionary['messier']:
        x = int(obj[1:]) + 1
        if x == 111:
            x = 1
        return [obj, '<a href="/image/' + 'M' + str(x) + '">' + 'M' + str(x) + '</a>']
    return [obj]
