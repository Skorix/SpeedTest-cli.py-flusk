from flask import Flask
from speedtest import Speedtest
import shelve
app = Flask(__name__)

db = shelve.open('db')


st = Speedtest()
db['dw'] = st.download()


dw = db['dw']
db.close()
dwMbait = int(str(dw)[:2])/8
dwMbit = int(str(dw)[:2])


@app.route('/')
def index():
    return f'Загрузка = {dwMbait} мегабайт или {dwMbit} мегабит, а выдаваемое значение {dw}'





if __name__ == '__main__':
    app.run(debug=True)