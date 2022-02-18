from flask import Flask, render_template, url_for, request, redirect, Blueprint
import build_map

app = Flask(__name__)
open('templates/my_map.html', 'w').close()
errors = Blueprint('errors', __name__)

@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        user_name = request.form["nm"]
        open('templates/my_map.html', 'w').close()
        return redirect(url_for("user_name", usr=user_name))
    else:
        return render_template('home.html')


@app.route("/<usr>")
def user_name(usr):
    build_map.total_info(usr)
    return render_template(f'{usr}.html')

# @errors.app_errorhandler(500)
# def error_500(error):
#     return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)


