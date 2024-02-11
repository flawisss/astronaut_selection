from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div class="text-center">
                              <h1>Анкета претендента<h1>
                              <h2>На участие в миссии<h2>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                      <input type="text" class="form-control" id="surname" placeholder="Введите фамилию">
                                      <input type="text" class="form-control" id="name" placeholder="Введите имя"></br>
                                      <input type="text" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Общее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <class="form-group form-check">
                                        <label for="form-group form-check">Какие у Вас есть профессии?</label>
                                        <div>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="engineer-explorer">
                                          <label class="form-check-label" for="acceptRules">Инженер-исследователь</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="engineer-builder">
                                          <label class="form-check-label" for="acceptRules">Инженер-строитель</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="pilot">
                                          <label class="form-check-label" for="acceptRules">Пилот</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="meteorologist">
                                          <label class="form-check-label" for="acceptRules">Метеоролог</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="life-engineer">
                                          <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="nuclear-engineer">
                                          <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="doctor">
                                          <label class="form-check-label" for="acceptRules">Врач</label></br>
                                          <input type="checkbox" class="form-check-input" id="jobs" name="biologist">
                                          <label class="form-check-label" for="acceptRules">Экзобиолог</label></br>
                                        </div>
                                    <div class="form-group">
                                        </br><label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    </br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы оставаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
