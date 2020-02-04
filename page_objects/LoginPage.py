from PageObjectLibrary import PageObject, PageObjectLibraryKeywords


class LoginPage(PageObject):
    PAGE_URL = "/core/index.php/login"
    PAGE_TITLE = "ownCloud"

    _locators = {
        "username": "id=user",
        "password": "id=password",
        "form_id": "login",
        "login_form_xpath": "//form[@name='%s']"
    }

    # def _is_current_page(self):
    #     # this site uses the same title for many pages,
    #     # so we can't rely on the default implementation
    #     # of this function. Instead, we'll check the page
    #     # location, and raise an appropriate error if
    #     # we are not on the correct page
    #     location = self.selib.get_location()
    #     if not location.endswith(self.PAGE_URL):
    #         message = "Expected location to end with " + \
    #                   self.PAGE_URL + " but it did not"
    #         raise Exception(message)
    #     print("exist")
    #     return True

    def enter_username(self, username):
        """Type the given text into the username field """
        self.selib.input_text(self.locator.username, username)

    def enter_password(self, password):
        """Type the given text into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_login_button(self):
        """Clicks the submit button on the form

        For illustrative purposes, this uses the low level selenium
        functions for submitting the form
        """
        form = self.driver.find_element_by_xpath( self.locator.login_form_xpath % self.locator.form_id)
        form.submit()

