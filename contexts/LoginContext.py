from robot.api.deco import keyword

from LoginPage import LoginPage


class LoginContext:
    loginPage = LoginPage()

    @keyword(name="User Logs In With Username ${username} And Password ${password}")
    def user_login(self, username, password):
        self.loginPage.enter_username(username)
        self.loginPage.enter_password(password)
        self.loginPage.click_the_login_button()
