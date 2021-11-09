from flask import Blueprint, render_template, request, redirect
from .weight_check import *

portfolio = Blueprint('portfolio', __name__, template_folder='templates', static_folder='static')


@portfolio.route('/')
def index():
    return render_template("index.html")


@portfolio.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        targets = []
        for i in range(9):
            person = request.form.get(f"Person{i+1}")
            try:
                targets.append(int(person))
            except (ValueError, TypeError) as e:
                print(e)
        if not targets:
            return render_template("weight.html")
        print(targets)
        # targets = [120, 55, 110, 140, 90, 85, 85]     #for testing purposes
        final_group, final_options = make_groups(targets)


        return render_template("weight.html", final_group=final_group, final_options=final_options)
    else:
        return render_template("weight.html")
