from app import app

#controladores
from app.controllers.index import *

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)