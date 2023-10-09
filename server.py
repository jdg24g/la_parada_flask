from app import app

#controladores
from app.controllers.index import *
from app.controllers.auth import *
from app.controllers.cities_company import *

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)