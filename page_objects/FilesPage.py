from PageObjectLibrary import PageObject


class FilesPage(PageObject):
    PAGE_URL = "/core/index.php/apps/files/"
    PAGE_TITLE = "Files - ownCloud"

    # def _is_current_page(self):
    #     # this site uses the same title for many pages,
    #     # so we can't rely on the default implementation
    #     # of this function. Instead, we'll check the page
    #     # location:
    #     with self._wait_for_page_refresh():
    #         location = self.selib.get_location()
    #         url = location.split('?')[0]
    #         if not url.endswith(self.PAGE_URL):
    #             message = "Expected location to end with " + \
    #                       self.PAGE_URL + " but it did not"
    #             raise Exception(message)
    #         return True
