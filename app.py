# define imports
from flask import Flask
from string import Template
app = Flask(__name__)


# define html template
HTML_TEMPLATE = Template("""
      <h2>
        YouTube video link:
        <a href="https://www.youtube.com/watch?v=${youtube_id}">
          ${youtube_id}
        </a>
      </h2>

      <iframe src="https://www.youtube.com/embed/${youtube_id}" width="853" height="480" frameborder="0" allowfullscreen></iframe>""")




#-------------------------------------------------------------
# routes


# define app route for homepage
@app.route('/')
def homepage():
    vidhtml =  HTML_TEMPLATE.substitute(youtube_id='YQHsXMglC9A')
    return """<h1>Hello world!</h1>""" + vidhtml



# define app route for etc
@app.route('/videos/<vid>')
def videos(vid):
    return HTML_TEMPLATE.substitute(youtube_id=vid)




#-------------------------------------------------------------
# standard boilerplate
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
