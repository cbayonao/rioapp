import json
import mechanicalsoup

from flask import Flask

app = Flask(__name__)


def login_municipality_rionegro() -> str:
    url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'

    try:
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url=url)
        browser.get_current_page()
        browser.select_form()

        # fill-in the form
        browser['login:_t61'] = '1032448740'
        browser['login:j_idt65'] = 'c4m1l0'

        browser.submit_selected()
    except Exception as error:
        return str(error)

    return 'Success'


def create_account_municipality_rionegro() -> str:
    url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
    url_create_account = 'http://entidadesintegradas.co/Registro/faces/CrearCuenta.xhtml'

    try:
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url=url)
        browser.open(url=url_create_account)

        browser.select_form()

        # Fill-in the form
        browser['crearCuenta:_t50'] = '1'
        browser['crearCuenta:_t61'] = '1098707951'
        browser['crearCuenta:_t65'] = '123456'
        browser['crearCuenta:_t69'] = '123456'
        browser['crearCuenta:_t73'] = 'Daniel Mauricio'
        browser['crearCuenta:_t74'] = 'Sandoval'
        browser['crearCuenta:_t75'] = 'Vargas'
        browser['crearCuenta:_t79'] = 'M'
        browser['crearCuenta:_t86'] = 'derhks@gmail.com'
        browser['crearCuenta:_t90'] = '60000000'
        browser['crearCuenta:_t94'] = '3000000000'
        browser['crearCuenta:_t98'] = '5'
        browser['crearCuenta:direccion'] = 'CL 46 # 52 - 77'
        browser['crearCuenta:_t110'] = '02'
        browser['crearCuenta:_t143'] = '02'
        browser['crearCuenta:_t157'] = '1987'
        browser['crearCuenta:_t163'] = None
        browser['crearCuenta:_t167'] = 'rojo'
        browser['crearCuenta:_t171'] = None
        browser['crearCuenta:_t175'] = 'bogota'
        browser['crearCuenta:_t177'] = 'on'

        browser.submit_selected()
    except Exception as error:
        return str(error)

    return 'Success'


def mainpage_municipality_rionegro() -> str:
    try:
        browser = mechanicalsoup.StatefulBrowser()
        url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
        browser.open(url=url)
        browser.get_current_page()
    except Exception as error:
        return str(error)

    return 'Success'


@app.route('/', methods=['GET'])
def main_page():
    response = mainpage_municipality_rionegro()

    return {
        'statusCode': 200 if response == 'Success' else 500,
        'body': json.dumps(response)
    }


@app.route('/create_account', methods=['POST'])
def create_account():
    response = create_account_municipality_rionegro()

    return {
        'statusCode': 200 if response == 'Success' else 500,
        'body': json.dumps(response)
    }


@app.route('/login', methods=['POST'])
def login():
    response = login_municipality_rionegro()

    return {
        'statusCode': 200 if response == 'Success' else 500,
        'body': json.dumps(response)
    }
