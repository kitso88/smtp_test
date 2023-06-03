import random

import requests
from allure import step

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
