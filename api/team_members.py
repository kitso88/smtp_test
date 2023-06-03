import requests
from allure import step
from pytest_schema import schema

from api.conf.config import BASE_URL, GET_MEMBERS


class TeamMembersMethods:

    @step
    def get_team_members_status_code(self):
        res = requests.get(BASE_URL+GET_MEMBERS)
        return res.status_code

    @step
    def get_team_members_content_type(self):
        res = requests.get(BASE_URL+GET_MEMBERS)
        return res.headers['Content-type']

    @step
    def get_team_members_data(self):
        res = requests.get(BASE_URL+GET_MEMBERS)
        members = res.json()
        return members

    @step
    def members_schema_validation(self):
        members_schema = {
            "status": str,
            "data": {
                "members": [
                    {
                        "position": str,
                        "level": str,
                        "first_name": str,
                        "last_name": str,
                        "day_birth": int,
                        "hr_department": str,
                        "email": str,
                        "mobile": int,
                        "probation_period": int,
                        "ID": str
                    }
                ]
            }
        }
        members_data = self.get_team_members_data()
        return schema(members_schema) == members_data

