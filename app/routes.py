from flask import Blueprint, redirect, url_for, Flask, jsonify, render_template, flash, render_template_string, request,g, session

main = Blueprint('main', __name__)

@main.route('/')
def index():

    text = ""
    char_count = 0
    byte_count = 0

    if request.method == "POST":
        text = request.form.get("text", "")
        char_count = len(text)
        byte_count = len(text.encode("utf-8"))

    return render_template(
        "index.html",
        text=text,
        char_count=char_count,
        byte_count=byte_count
    )
