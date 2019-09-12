from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.

# a form for crossing off watched movies
crossoff_form = """
<form action="/crossoff" method="post">
    <label for="crosoff-movie">
        I want to cross off
        <select id="crosoff-movie" name="crossed-off-movie">
            {0}
        </select>
        from my Watchlist.
    </label>
    <input type="submit" value="Cross/Uncross">
</form>
"""

movies = []

# TODO:
# Finish filling in the function below so that the user will see a message like:
# "Star Wars has been crossed off your watchlist".
# And create a route above the function definition to receive and handle the request from 
# your crossoff_form.
@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']
    
    if '<strike>' in movies[movies.index(crossed_off_movie)]:
        movies[movies.index(crossed_off_movie)] = crossed_off_movie.replace('strike','p')
    else:
        movies[movies.index(crossed_off_movie)] = '<strike>' + crossed_off_movie + '</strike>'

    return index()

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']
    movies.append(new_movie)
    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"

    return index()


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    options = []
    movies_list = []

    for movie in movies:
        options.append('<option value="' + movie + '">' + movie + "</option>")
        movies_list.append('<li style="list-style: none;">' + movie + '</li>')
    # build the response string
    content = page_header + edit_header + add_form + crossoff_form.format(''.join(options)) + '<h3>Movies list:</h3>' + '<ul>' +  ''.join(movies_list) + '</ul>' + page_footer

    return content


app.run()
