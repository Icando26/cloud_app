import sys, os, allure

sys.path.append(os.getcwd())

from Page.Page import Page_Obj
from Base.InitDiver import init_driver
from Base.Read_Data import ret_yaml_data
import pytest


def yaml_data():
    data_list = []
    data = ret_yaml_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test"), data.get(i).get("expect_data")))
    return data_list


class Test_Search_Page:
    def setup_class(self):
        self.driver = init_driver()

        self.search_obj = Page_Obj(self.driver).return_search()
        self.search_obj.click_search_btn()

    def teardown_class(self):
        self.search_obj.search_return()
        self.driver.quit()

    #@pytest.mark.parametrize("test_num,text,expect_data", yaml_data())
    #@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('测试搜索')
    @allure.issue('http://www.baidu.com','Test')
    def test_input_text(self):
        print("用例编号:")
        allure.attach('描述',"执行测试步骤")
        self.search_obj.search_input("你好")
        #self.driver.get_screenshot_as_file("./screen/%s.png" % )
        # assert expect_data == 456
