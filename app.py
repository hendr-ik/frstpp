from flask import Flask
app = Flask(__name__)



@app.route("/")
def homepage():
    return """
    <!DOCTYPE html>
    <head>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   </head>
   <body style="width: 880px; margin: auto;">
    <h1>Visible stuff goes here</h1>
    <p>here's a paragraph, fwiw</p>
    <p>And here's an image:</p>
    <a href="https://www.flickr.com/photos/zokuga/14615349406/">
    <img src="http://stash.compjour.org/assets/images/sunset.jpg" alt="it's a nice sunset">
    </a>
    </body>
    """


@app.route('/stanford')
def stanford_page():
    return """
      <h1>Hello stanford!</h1>

      <img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=stanford" alt="map of stanford">

      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">
    """




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
