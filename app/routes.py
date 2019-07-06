from app import app
from app.forms import second_game_form
from flask import render_template, redirect
from Constellation import new_constellation
from Constellation.dictionary import rus_lat_dict, lat_rus_dict, dictionary
from app.forRoutes.image_obj import Image_obj
from app.forRoutes.mainpage import MainPage
from app.forRoutes.text import Text


@app.route('/')
@app.route('/mainpage/')
def mainpage():
    messages = MainPage()
    return render_template('mainpage.html.j2', title = 'Main Page', messages = messages)

@app.route('/second_game/', methods = ["GET", "POST"])
def second_game():
    form = second_game_form()
    const = new_constellation.one_step()
    messages = [const]
    image_name = rus_lat_dict[const] + '.png'
    return render_template('second_game.html.j2', title = "Second game", messages = messages, 
        image_name = image_name, form = form)

@app.route('/image/<obj>/')
def image_obj(obj):
    if obj in dictionary:
        if obj == 'constellation':
            links = ['<a href=/image/'+el+'/>'+lat_rus_dict[el]+'</a>' for el in dictionary[obj]]
        else:
            links = ['<a href=/image/' + el + '/>' + el + '</a>' for el in dictionary[obj]]
        return render_template('image.html.j2', title = 'List of ' + obj, links = links, messages = ['Выберите объект:'])
    elif obj in dictionary['constellation'] or obj in dictionary['messier'] or obj in dictionary['stars']:
        messages = Image_obj(obj)
        return render_template('image_obj.html.j2', title = "Image of " + obj, messages = messages, obj = obj)
    else:
        return render_template('error.html.j2', title = '404', messages = ['404 NOT FOUND'])

@app.route('/image/')
def image():
    return render_template('error.html.j2', title = '404', messages = ['404 NOT FOUND'])

@app.route('/rulse/<game>/')
def rulse(game):
    text = Text(game)
    return render_template('rulse.html.j2', title = 'Rulse', messages = ['Правила игры'], text = text)
