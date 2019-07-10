from app import app
from app.forms import first_game_const_form, second_game_const_form
from flask import render_template, redirect
from Constellation import new_constellation
from Constellation.dictionary import rus_lat_dict, lat_rus_dict, dictionary
from app.forRoutes.image_obj import Image_obj
from app.forRoutes.mainpage import MainPage
from app.forRoutes.text import Text
from app.forRoutes.second_game import SecondGameConst
from app.forRoutes.parser import parser

@app.route('/')
@app.route('/mainpage/')
def mainpage():
    messages = MainPage()
    const = new_constellation.one_step()
    return render_template('mainpage.html.j2', title = 'Main Page', 
        messages = messages, const = const)

@app.route('/first_game/<const>/', methods = ["GET", "POST"])
def first_game_const(const):
    form = first_game_const_form()
    messages = [const]
    new_const = new_constellation.one_step()
    if form.validate_on_submit():
        text = form.text.data
        if text == lat_rus_dict[const]:
            text = parser([text + ' &#10004'])
        else:
            text = parser([text + ' &#10008', lat_rus_dict[const]])
        return render_template('const_game.html.j2', title = "First game", 
            messages = messages, form = form, text = text, image_name = const + '.png', 
            game = 'first_game', next_const = new_const)
    return render_template('const_game_ans.html.j2', title = "First game", 
        messages = messages, form = form, image_name = const + '.png')

@app.route('/second_game/<const>/', methods = ["GET", "POST"])
def second_game_const(const):
    form = second_game_const_form()
    messages = [lat_rus_dict[const]]
    list_mark = SecondGameConst(const, form)
    if list_mark:
        return second_game(list_mark, const)
    return render_template('const_game_ans.html.j2', title = "Second game", 
        messages = messages, form = form)

@app.route('/image/<obj>/')
def image_obj(obj):
    if obj in dictionary:
        if obj == 'constellation':
            links = ['<a href=/image/' + el + '/>' + lat_rus_dict[el] + '</a>' 
            for el in dictionary[obj]]
        else:
            links = ['<a href=/image/' + el + '/>' + el + '</a>' 
            for el in dictionary[obj]]
        return render_template('image.html.j2', title = 'List of ' + obj, 
            links = links, messages = ['Выберите объект:'])
    elif obj in dictionary['constellation'] + dictionary['messier'] + dictionary['stars']:
        messages = Image_obj(obj)
        return render_template('image_obj.html.j2', title = "Image of " + obj, 
            messages = messages, obj = obj)
    else:
        return render_template('error.html.j2', title = '404', 
            messages = ['404 NOT FOUND'])

@app.route('/image/')
def image():
    return render_template('error.html.j2', title = '404', 
        messages = ['404 NOT FOUND'])

@app.route('/rulse/<game>/')
def rulse(game):
    text = Text(game)
    return render_template('rulse.html.j2', title = 'Rulse', 
        messages = ['Правила игры'], text = text)

@app.route('/messier/<obj>')
def messier(obj):

    return render_template()

def second_game(lst, const):
    print_list = []
    image_name = const + '.png'
    new_const = new_constellation.one_step()
    for i in range(len(lst)):
        if type(lst[i]) == tuple:
            if lst[i][1] == 1:
                print_list.append(lst[i][0] + ' &#10004')
            elif lst[i][0] != '':
                print_list.append(lst[i][0] + ' &#10008')
        else:
            print_list.append(lst[i])
    print_list = parser(print_list)
    return render_template('const_game.html.j2', title = "Second game", 
        text = print_list, image_name = image_name, next_const = new_const, 
        messages = [const], game = 'second_game')
