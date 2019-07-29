from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    my_foods = ["puree batata", "lasagna", "cheese fries"]
    return render_template(
    	"index.html",
    	foods = my_foods)

if __name__ == '__main__':
   app.run(debug = True)