from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route("/")
def page():
    return "миссия колонизации марса"


@app.route("/index")
def index():
    return "и на марсе будут яблоки цвести"


@app.route("/promotion")
def promotion():
    br_list = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return "<br>".join(br_list)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <h1>Жди нас марс!</h1>
                    <img src="{url_for('static', filename='mars.webp')}" alt="Нет картинки"/>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <p>Вот она какая красная планета!</p>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")