from app import app
from app.forms import NearC_Form
from flask import render_template, redirect
from Constellation import new_constellation
from Constellation.dictC import rus_lat_dict as rus_lat_dict

@app.route('/')
def space():
    form = NearC_Form()
    const = new_constellation.one_step()
    messages = [const]
    image_name = rus_lat_dict[const] + '.png'
    return render_template('main_page.html.j2', title = "Home", messages = messages, 
        image_name = image_name, form = form)

@app.route('/home', methods = ["GET", "POST"])
def home():
    form = NearC_Form()
    const = new_constellation.one_step()
    messages = [const]
    image_name = rus_lat_dict[const] + '.png'
    return render_template('main_page.html.j2', title = "Home", messages = messages, 
        image_name = image_name, form = form)

@app.route('/favicon.ico')
def favicon():
    return redirect('/home')