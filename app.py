from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    my_foods = ["puree batata", "lasagna", "cheese fries"]
    my_least_foods = {"cat", "dog", "girafee"}
    return render_template(
    	"index.html",
    	foods = my_foods,
    	bad_foods = my_least_foods,
    	opposite_day = True)

if __name__ == '__main__':
   app.run(debug = True)