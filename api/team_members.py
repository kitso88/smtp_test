import requests
from allure import step

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
        return members['data']['members']
