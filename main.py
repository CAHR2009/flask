from flask import Flask, url_for

application = Flask(__name__)



@application.route("/promotion_image")
def simple():
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/style.css">
    <title>Привет, Яндекс!</title>
  </head>
  <body>
    <img src="{url_for('static', filename='img/mars.png')}">
    <h1>Привет, Яндекс!</h1>
    <div class="alert alert-secondary" role="alert">
        <br><b>Человечество вырастает из детства.</b>
    </div>
    <div class="alert alert-success" role="alert">
        <br><b>Человечеству мала одна планета.</b>
    </div>
    <div class="alert alert-secondary" role="alert">
        <br><b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
    </div>
    <div class="alert alert-warning" role="alert">
        <br><b>И начнем с Марса!</b>
    </div>
    <div class="alert alert-danger" role="alert">
        <br><b>Присоединяйся!</b>
    </div>
  </body>
</html>
'''


if __name__ == '__main__':
    application.run(host="127.0.0.1", port=8080)
