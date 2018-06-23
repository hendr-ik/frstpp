# define imports
from flask import Flask
from string import Template
app = Flask(__name__)


# define html template
HTML_TEMPLATE = Template("""
    <!DOCTYPE html>
    <head>
    <title>Place - FRSTPP</title>
    <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
    </head>

    <body style="width: 880px; margin: auto;">
    <h1>Hello ${place_name}!</h1>
    <img src="http://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">
    <img src="http://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
    </body>
    """)



#-------------------------------------------------------------
# routes


# define app route for homepage
@app.route("/")
def homepage():
    return """
    <!DOCTYPE html>
    <head>
    <title>Home - FRSTPP</title>
    <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
    </head>

    <body style="width: 880px; margin: auto;">
    <h1>Hi there</h1>
    </body>
    """



# define app route for places
@app.route('/places/<p>')
def places_view(p):
    return(HTML_TEMPLATE.substitute(place_name=p))



# define app route for weather
@app.route('/weather/<blahblahblah>')
def weather_view(blahblahblah):
    s = """I don't know what the weather is in {zzz}"""
    return s.format(zzz=blahblahblah)




#-------------------------------------------------------------
# standard boilerplate
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
