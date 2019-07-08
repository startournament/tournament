from app.forms import second_game_const_form
from Constellation.dictionary import *

def SecondGameConst(const, form: second_game_const_form) -> list:
    if form.validate_on_submit():
        list_ans = form.text.data.split(', ')
        list_ans[-1] = list_ans[-1].rstrip()
        list_return = []
        CloseConstellations = dict_constell[lat_rus_dict[const]].copy()
        for el in list_ans:
            if el in CloseConstellations:
                list_return.append((el, 1))
                CloseConstellations.remove(el)
            else:
                list_return.append((el, 0))
        return list_return + CloseConstellations
    return []