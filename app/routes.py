from app import app
from app.forms import NearC_Form
from flask import render_template, redirect
from Constellation import new_constellation
from Constellation.dictC import rus_lat_dict, list_obj
from app.forRoutes.image_obj import Image_obj

@app.route('/second_game', methods = ["GET", "POST"])
def second_game():
    form = NearC_Form()
    const = new_constellation.one_step()
    messages = [const]
    image_name = rus_lat_dict[const] + '.png'
    return render_template('main_page.html.j2', title = "Home", messages = messages, 
        image_name = image_name, form = form)

@app.route('/image/<obj>')
def image_obj(obj):
    #obj in latin
    #obj can be constellation or something else (what for example?? M1, M43, M57 ...)
    if obj in list_obj:
        messages = Image_obj(obj)
        return render_template('image_obj.html.j2', title = "Image of " + obj, messages = messages, 
        obj_name = obj + '.png')
    else:
        return render_template('error.html.j2', title = '404', messages = ['404 NOT FOUND'])

@app.route('/image/')
def image():
    return render_template('error.html.j2', title = '404', messages = ['404 NOT FOUND'])
