Mostly for my testing purposes.

Figure I'd try out flask restful-plus and then in the future also try out vuejs as the frontend for it

## TO DO
- [] vuejs installation
- [] vuejs setup
- [] better app configuration
- [] set up database things, sqlalchemy
- [] play around with setting up multiple resources

# Set up
I decided to use python3 and conda, which I usually don't use, so there will be some playing around to get things going, mainly with the virtual environment.

Get virtualenv up and running in whatever way you'd like.

`make develop`

# The app
`python app.py`
Will start the Flask server.

The api is configured to be `/api/todo` for the purposes of being able to set up multiple api resources within a single project (if you'd like to)

`curl http://localhost:5000/api/todo/todo4 -d "data=Remember the milk" -X PUT`

`curl http://localhost:5000/api/todo/all`

