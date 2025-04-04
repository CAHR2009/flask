from flask import Flask, url_for
application = Flask(__name__)



@application.route("/results/<nickname>/<int:level>/<float:rating>")
def simple(nickname, level, rating):
    return f'''
<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/style.css">
    <title>Результаты</title>
  </head>
  <body>
    <h1>Результаты отбора</h1>
    <h3>Претендента на участие в миссии {nickname}</h3>
    <div class="alert alert-success" role="alert">
        <h3>Поздравляем! ваш рейтинг после {level} этапа отбора</h3>
    </div>
    <h3>Составляет {rating}!</h3>
    <div class="alert alert-warning" role="alert">
        <h3>Желаем удачи!</h3>
    </div>
  </body>
</html>
'''


if __name__ == '__main__':
    application.run(host="127.0.0.1", port=8080)
