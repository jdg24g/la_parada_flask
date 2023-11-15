from app import app

#controladores
from app.controllers.index import *
from app.controllers.auth import *
from app.controllers.cities_company import *
from app.controllers.bus_schedule import *

if __name__ == '__main__':
    app.run()
