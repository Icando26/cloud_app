from selenium.webdriver.common.by import By
from Base.Base import Base

class Send_Sms:
    def __init__(self, driver):
        # 实例化Base
        self.base_obj = Base(driver)
        # 添加信息按钮
        self.add_sms = (By.ID, "com.android.mms:id/action_compose_new")
        # 接受者
        self.accept_user = (By.ID, "com.android.mms:id/recipients_editor")
        # 输入信息
        self.input_sms = (By.ID, "com.android.mms:id/embedded_text_editor")
        # 发送按钮
        self.send_button = (By.ID, "com.android.mms:id/send_button_sms")

    def add_sms_btn(self):
        # 添加信息按钮
        self.base_obj.click_element(self.add_sms)

    def accept_user_input(self, phone):
        # 输入接收人
        self.base_obj.input_element(self.accept_user, phone)
        
    def send_sms_input(self, text):
        # 输入发送内容
        self.base_obj.input_element(self.input_sms, text)
        # 点击发送按钮
        self.base_obj.click_element(self.send_button)