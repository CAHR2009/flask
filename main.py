from flask import Flask, url_for

application = Flask(__name__)



@application.route("/astronaut_selection")
def simple():
    return f'''
<!doctype html>
<html lang="en">    
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="static/css/style.css">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Отбор Астронавтов</title>
  </head>
  <body>
    <main>
      <h1>Анкета претендента</h1>
      <h3>на участие в миссии</h3>
      <section class="form">
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">Введите фамилию</label>
        </div>
        <div class="form-floating mb-5">
          <input type="text" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Введите имя</label>
        </div>
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Введите адрес почты</label>
        </div>
        <p>Какое у вас образование</p>
        <select class="form-select form-select-lg mb-3" aria-label="Large select example">
          <option value="1">Начальное</option>
          <option value="2">Среднее</option>
          <option value="3">Высшее</option>
        <p>Какие к вас есть профессии?</p>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkDefault">
            Инженер-исследователь
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Инженер-строитель
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Пилот
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Метеоролог
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Инженер ро жизнеобеспеченью
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Инженер по радиационной защите
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Врач
          </label>
        </div>
        <div class="form-check mb-4">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Магистр по поеданию печенек
          </label>
        </div>
        <p>Укажите пол</p>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radioDefault" id="radioDefault1" checked>
          <label class="form-check-label" for="radioDefault1">
            Мужской
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="radioDefault" id="radioDefault2">
          <label class="form-check-label" for="radioDefault2">
            Женский
          </label>
        </div>
        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label">Почему вы решили принять участие в миссии?</label>
          <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <div class="mb-3">
          <input type="file" class="form-control" aria-label="file example" required>
        <div class="invalid-feedback">Выберите файл</div>
        </div>
        <div class="form-check mb-4">
          <input class="form-check-input" type="checkbox" value="" id="checkDefault">
          <label class="form-check-label" for="checkChecked">
            Готовы остаться на марсе?
          </label>
        </div>
        <div class="mb-3">
          <button class="btn btn-primary" type="submit">Отправить</button>
        </div>
      </section>
    </main>
  </body>
</html> 
'''


if __name__ == '__main__':
    application.run(host="127.0.0.1", port=8080)
