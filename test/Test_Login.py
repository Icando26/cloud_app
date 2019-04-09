from Base.InitDiver import init_driver
from Page.Login import Login
import pytest

class Test_login:

    def setup_class(self):
        #
        self.driver = init_driver()
        #
        self.login = Login(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_001(self):
        self.login.click_search()

if __name__ == '__main__':
    pytest.main()