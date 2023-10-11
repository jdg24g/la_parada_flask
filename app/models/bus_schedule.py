from app.config.connect_to_mysql import connect_to_mysql

class Schedule:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.city_id = data['city_id']
        self.company_id = data['company_id']
        self.schedule = data['schedule']

    @classmethod
    def create(cls, data: dict):
        query = "INSERT INTO schedules (city_id, company_id, schedule) VALUES (%(city_id)s, %(company_id)s, %(schedule)s);"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def update(cls, data: dict):
        query = "UPDATE schedules SET city_id = %(city_id)s, company_id = %(company_id)s, schedule = %(schedule)s WHERE id = %(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def delete(cls, data: dict):
        query = "DELETE FROM schedules WHERE id = %(id)s;"
        results = connect_to_mysql().query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = """
                SELECT s.id, s.city_id, s.company_id, s.schedule, c.city AS city_name, com.company AS company_name FROM schedules s 
                JOIN cities c ON s.city_id = c.id
                JOIN companies com ON s.company_id = com.id;
                """
        results = connect_to_mysql().query_db(query)
        schedules = []
        if results:
            for schedule in results:
                schedules.append(cls(schedule))
            return schedules
        return None

    @classmethod
    def get_by_id(cls, data: dict):
        query = """SELECT s.id, s.city_id, s.company_id, s.schedule, c.city AS city_name, com.company AS company_name FROM schedules s " \
                JOIN cities c ON s.city_id = c.id 
                JOIN companies com ON s.company_id = com.id
                WHERE s.id = %(id)s;"""
        results = connect_to_mysql().query_db(query, data)
        if results:
            return Schedule(results[0])
        return None
