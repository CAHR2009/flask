from flask import Flask, url_for

application = Flask(__name__)



@application.route("/choice/<planet_name>")
def simple(planet_name):
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
    <title>Варианты выбора</title>
  </head>
  <body>
    <h1>Мое предложение: {planet_name}</h1>
    <h3>Эта планета ближе к Земле</h3>
    <div class="alert alert-success" role="alert">
        <h3>На ней много необходимых ресурсов</h3>
    </div>
    <div class="alert alert-secondary" role="alert">
        <h3>На ней есть вода и атмосфера</h3>
    </div>
    <div class="alert alert-warning" role="alert">
        <h3>На ней есть небольшое магнитное поле</h3>
    </div>
    <div class="alert alert-danger" role="alert">
        <h3>Наконец, она просто красива!</h3>
    </div>
  </body>
</html>
'''


if __name__ == '__main__':
    application.run(host="127.0.0.1", port=8080)
