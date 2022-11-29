from flask import Flask, render_template, redirect, request
from form import PiperackArea, PiperackP, Equipos # formulario
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import os
from flask_caching import Cache
import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



app = Flask(__name__)
app.config['SECRET_KEY'] = 'pai2C'



'''
@app.route("/")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
'''

#app.run(debug=True)

@app.route('/')
def index():
    
    return  render_template('index.html')

@app.route('/planta', methods = ['GET', 'POST'])
def planta():
    form=PiperackArea()
    alto = None
    ancho = None
    world = None
    f= None
    l = None
    fp = None
    sp=None
    if form.is_submitted():
        ancho = int(request.form['ancho'])
        alto = int(request.form['alto'])
        world = np.zeros((alto,ancho))

        fig1 = plt.figure()
        plt.imshow(world)              
        plt.savefig('static/area.png', bbox_inches='tight')

        fig2 = plt.figure(figsize = (100,30))    
        ax = fig2.add_subplot(111, projection='3d')
        ax.scatter3D(alto, ancho, 2,s = 1000 , marker = "o", color='red')
        ax.scatter3D(0, ancho, 2,s = 1000 , marker = "o", color='red')
        ax.scatter3D(alto, 0, 2,s = 1000 , marker = "o", color='red')
        ax.scatter3D(0, 0, 2,s = 1000 , marker = "o", color='red')
        plt.savefig('static/area3d.png', bbox_inches='tight')
       


        return render_template('planta.html', form=form, alto=alto, ancho=ancho, get_plot = True, plot_url = 'static/area.png', plot3d_url= 'static/area3d.png')
    return  render_template('planta.html', form=form, ancho=ancho,alto=alto)

print(planta.ancho)

        

@app.route('/piperack', methods = ['GET', 'POST'])
def piperack():
    form=PiperackArea()
    form2=PiperackP()
    anchoP=None
    largoP=None
    altoP=None
    seccionesP=None
    f= None
    l = None
    fp = None
    sp=None
    world= None

    
    if form.is_submitted() and form2.is_submitted():
        ancho = int(request.form['ancho'])
        alto = int(request.form['alto'])
        anchoP =int(request.form['anchoP'])  
        largoP =int(request.form['largoP'])  
        altoP =int(request.form['altoP'])  
        seccionesP = int(request.form['seccionesP'])  

        world = np.zeros((alto,ancho))
        f = (l - largoP)//2
        
        fp = int(((l - largoP)//2))  #3
        
        sp = l - ((l - largoP)//2) #7
        

        lin_piperack = []

        for i in range(fp):
            world[i][fp-1] = 5
            linea = (i,fp-1)
            lin_piperack.append(linea)
        for j in range(sp,l,1):  
            world[j][fp-1] = 5
            linea = (j,fp-1)
            lin_piperack.append(linea)
        for h in range(fp):
            world[h][sp] = 5
            linea = (h,sp)
            lin_piperack.append(linea)
        for k in range(sp,l,1):
            world[k][sp] = 5
            linea = (k, sp)
            lin_piperack.append(linea)
        for o in range(fp, sp+1, 1):
            world[fp-1][o] = 5
            linea = (fp-1, o)
            lin_piperack.append(linea)
        for p in range(fp, sp+1, 1):
            world[sp][p] = 5
            linea = (sp,p)
            lin_piperack.append(linea)

        xp = [x[1] for x in lin_piperack]
        yp = [y[0] for y in lin_piperack]

        fig1 = plt.figure()
        plt.imshow(world)              
        plt.savefig('static/piperack2d.png', bbox_inches='tight')

        fig2 = plt.figure(figsize = (100,30))    
        ax = fig2.add_subplot(111, projection='3d')
        plt.savefig('static/piperack3d.png', bbox_inches='tight')

        return render_template('piperack.html', form=form, form2=form2, alto = alto, ancho = ancho, anchoP=anchoP, largoP=largoP, altoP=altoP, seccionesP=seccionesP, get_plot = True, plot_urlpr = 'static/piperack2d.png', plot3d_urlpr= 'static/piperack3d.png')
    return  render_template('piperack.html',form1=form, form2=form2)

@app.route('/equipos')
def equipos():
    return  render_template('equipos.html')



@app.route('/lineas')
def lineas():
    return  render_template('lineas.html')

@app.route('/resultados')
def resultados():
    return  render_template('resultados.html')


@app.route('/blog')
def blog():
    posts =[{'title': 'EL Tachudita', 'author': 'Tichis'},
            {'title': 'EL Jruss', 'author': 'Russ'}]
    return  render_template('index.html', autor ='Tichis', sunny= False, posts = posts)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = PiperackArea()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signUp.html', form=form, result=result)    

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    
    return 'This is the blog' + blog_id

if __name__ == '__main__':
    app.run()

