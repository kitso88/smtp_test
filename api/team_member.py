import random

import requests
from allure import step
from pytest_schema import schema

from api.conf.config import BASE_URL, GET_MEMBER, GET_MEMBERS


class TeamMemberMethods:
    @step
    def get_member_random_id(self):
        res = requests.get(BASE_URL + GET_MEMBERS)
        members = res.json()
        total_records = len(members['data']['members'])
        random_number = random.randint(0, total_records - 1)
        return members['data']['members'][random_number]['ID']

    @step
    def get_team_member_status_code(self):
        res = requests.get(BASE_URL+GET_MEMBER+"/"+self.get_member_random_id())
        return res.status_code

    @step
    def get_team_member_content_type(self):
        res = requests.get(BASE_URL+GET_MEMBER+"/"+self.get_member_random_id())
        return res.headers['Content-type']

    @step
    def get_team_member_data(self):
        res = requests.get(BASE_URL+GET_MEMBER+"/"+self.get_member_random_id())
        member = res.json()
        return member['data']

    @step
    def member_schema_validation(self):
        member_schema = {
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
        member_data = self.get_team_member_data()
        return schema(member_schema) == member_data
