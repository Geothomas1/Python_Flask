from flask import Flask, render_template, url_for
app=Flask(__name__)

posts=[
    {
        'author':'Geo Thomas',
        'title':'About Geo Thomas',
        'content':'i am developer call devgeo',
        'time':'20 April 2020'
    },
    {
        'author':'Thomas',
        'title':'About Thomas',
        'content':'i am developer call devthomas',
        'time':'26 April 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title="about")

if __name__== '__main__':
    app.run(debug=True)
