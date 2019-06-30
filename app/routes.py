from app import app
from flask import render_template
from Constellation import new_constellation
from Constellation.dictC import rus_lat_dict as rus_lat_dict

@app.route('/')
@app.route('/home')
def home():
    const = new_constellation.one_step()
    messages = [const]
    image_name = rus_lat_dict[const] + '.png'
    return render_template('main_page.html.j2', title = "Home", messages = messages, image_name = image_name)
