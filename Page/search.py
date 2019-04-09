from selenium.webdriver.common.by import By
from Base.Base import Base
import pytest


class Search_Page:
    def __init__(self, driver):
        # 搜索按钮
        self.s_b = (By.ID, "com.android.settings:id/search")
        # 搜索输入框
        self.s_i = (By.ID, "android:id/search_src_text")
        # 返回按钮
        self.s_r = (By.CLASS_NAME, "android.widget.ImageButton")
        # 实例化Base类
        self.base_obj = Base(driver)

    def click_search(self):
        # 点击搜索按钮
        self.base_obj.click_element(self.s_b)

    def search_input(self, input_text):
        # 输入搜索内容
        self.base_obj.input_element(self.s_i, input_text)

    def click_return(self):
        # 点击返回按钮
        self.base_obj.click_element(self.s_r)

    def search_text(self, text):
        # 点击搜索按钮
        self.base_obj.click_element(self.s_b)
        # 输入内容
        self.base_obj.input_element(self.s_i, text)
        # 点击返回按钮
        self.base_obj.click_element(self.s_r)
