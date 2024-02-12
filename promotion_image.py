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
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <p>Вот она какая красная планета!</p>
                  </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    br_list = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]

    url_pic = url_for('static', filename='image/mars.webp')
    url_style = url_for('static', filename='css/style.css')

    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="Нет картинки"/>
                    <div class="alert alert-dark" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert alert-dark" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <br><h2>{}</h2>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <br><h2>{}</h2>
                    </div>
                  </body>
                </html>""".format(url_style, url_pic, *br_list)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")