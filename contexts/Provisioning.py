import requests
from robot.api.deco import keyword
from robot.api import logger


class Provisioning:

    def __init__(self, admin_usename, admin_password, backend_url):
        self.admin_username = admin_usename
        self.admin_password = admin_password
        self.backend_url = backend_url
        self.createdUsers = {}

    @keyword(name="a user has been created with username ${username} and password ${password}")
    def create_user(self, username, password):
        url = self.backend_url + "/ocs/v2.php/cloud/users?format=json"
        params = {'userid':username, 'password':password}
        session = requests.Session()
        session.auth = (self.admin_username, self.admin_password)
        r = session.post(url=url, data=params)
        if r.status_code < 200 or r.status_code > 400:
            raise Exception("Failed while creating a new user")
        self.createdUsers[username] = {
            "password": password
        }

    def delete_user(self, username):
        url = self.backend_url + "/ocs/v2.php/cloud/users/" + username
        session = requests.Session()
        session.auth = (self.admin_username, self.admin_password)
        r = session.delete(url=url)
        if r.status_code < 200 or r.status_code > 400:
            raise Exception("Failed while creating a new user")

    @keyword(name="Delete All Created Users")
    def delete_all_created_users(self):
        for user in self.createdUsers:
            self.delete_user(user)
