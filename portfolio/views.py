from flask import Blueprint, render_template, request, redirect
import smtplib
import ssl
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


@portfolio.route("/contactForm", methods=["POST"])
def contact():
    port = 465  # For SSL
    sender_email = "cameronDwebmail@gmail.com"
    receiver_email = "cameron.deweerd@gmail.com"
    name = request.form.get("contact-name")
    sender = request.form.get("contact-email")
    text = request.form.get("contact-message")
    org = request.form.get("contact-org")

    print(request.form.get("contact-name"))

    if org:
        name = f"{name} at {org}"


    message = f"""Subject: New message from {name}

    {name} sends the following:
    {text}

    reply back at: {sender}"""

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "mailService123")
        server.sendmail(sender_email, receiver_email, message)

    return redirect("/")
