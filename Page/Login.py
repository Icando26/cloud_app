from Base.InitDiver import init_driver
from Base.Base import Base
from selenium.webdriver.common.by import By


class Login(Base):
    def __init__(self, driver):
        # 搜索按钮
        self.s_b = (By.ID, "com.android.settings:id/search")
        # 搜索输入框
        self.s_i = (By.ID, "android:id/search_src_text")
        # 返回按钮
        self.s_r = (By.CLASS_NAME, "android.widget.ImageButton")
        # 实例化Base类
        self.base_obj = Base(driver)

    # 使用方法,业务操作
    def click_search(self):
        # 点击搜索按钮
        self.base_obj.click_element(self.s_b)
