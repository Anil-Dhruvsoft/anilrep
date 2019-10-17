from flask import Flask
app=application=Flask(__name__)


@application.route('/<name>')
def hello(name):

	return 'Hello world this your %s.' %name

@application.route('/')
def h():
	return "Hello world! This is Anil."
    


if __name__ == '__main__':
   app.run(debug = True)