import pytest

from api.team_member import TeamMemberMethods


class TestMembers:
    @pytest.fixture
    def api(self):
        api = TeamMemberMethods()
        return api

    def test_status_code(self, api):
        assert api.get_team_member_status_code() == 200

    def test_content_type(self, api):
        assert api.get_team_member_content_type() == 'application/json; charset=UTF-8'

    def test_members_type(self, api):
        assert isinstance(api.get_team_member_data(), dict)
