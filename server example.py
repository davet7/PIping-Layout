'''
from flask import Flask, render_template, redirect, request
from form import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pai'

#app.run(debug=True)

@app.route('/')
def home():
    return 'Hey!'

@app.route('/about')
def about():
    return  render_template('index.html')

@app.route('/blog')
def blog():
    posts =[{'title': 'EL Tachudita', 'author': 'Tichis'},
            {'title': 'EL Jruss', 'author': 'Russ'}]
    return  render_template('index.html', autor ='Tichis', sunny= False, posts = posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)    

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    
    return 'This is the blog' + blog_id

if __name__ == '__main__':
    app.run()

'''