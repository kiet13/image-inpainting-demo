from flask import Flask, render_template, get_template_attribute
import os
import logging
from glob import glob

app = Flask(__name__, template_folder='templates')

# a simple home page with textbox to input English word
@app.route('/')
def home1():
    return render_template('home.html')

@app.route('/home')
def home2():
    return render_template('home.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/gallery')
def gallery():
    images = sorted(os.listdir(os.path.join(app.static_folder, f"images/places365_8c/butte")))
    return render_template('gallery.html', images=images, category='places365_8c/butte')

@app.route('/<path:category>')
def load_images(category):
    images = sorted(os.listdir(os.path.join(app.static_folder, f"images/{category}")))
    return render_template('gallery.html', images=images, category=category)

if __name__ == '__main__':
    app.run(port='8080', debug=True)