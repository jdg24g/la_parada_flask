from app.config.connect_to_mysql import connect_to_mysql


class City:
    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.city = data["city"]

    @classmethod
    def create(cls, data: dict):
        query = "INSERT INTO cities (city) VALUES (%(city)s);"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def update(cls, data: dict):
        query = "UPDATE cities SET city=%(city)s WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def delete(cls, data: dict):
        query = "DELETE FROM cities WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cities;"
        results = connect_to_mysql().query_db(query)
        cities = []
        if results:
            for city in results:
                cities.append(cls(city))
            return cities
        return None

    @classmethod
    def get_by_id(cls, data: dict):
        query = "SELECT * FROM cities WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        if results:
            return City(results[0])
        return None
    

    @classmethod
    def check_city(cls,data:dict):
        query = "SELECT * FROM cities WHERE city= %(city)s;"
        results = connect_to_mysql().query_db(query,data)
        if results:
            return True
        return False


class Company:
    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.company = data["company"]

    @classmethod
    def create(cls, data: dict):
        query = "INSERT INTO companies (company) VALUES (%(company)s);"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def update(cls, data: dict):
        query = "UPDATE companies SET company=%(company)s WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def delete(cls, data: dict):
        query = "DELETE FROM companies WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM companies;"
        results = connect_to_mysql().query_db(query)
        companies = []
        if results:
            for company in results:
                companies.append(cls(company))
            return companies
        return None

    @classmethod
    def get_by_id(cls, data: dict):
        query = "SELECT * FROM companies WHERE id=%(id)s;"
        results = connect_to_mysql().query_db(query, data)
        if results:
            return Company(results[0])
        return None
    
    @classmethod
    def check_company(cls,data:dict):
        query = "SELECT * FROM companies WHERE company= %(company)s;"
        results = connect_to_mysql().query_db(query,data)
        if results:
            return True
        return False
