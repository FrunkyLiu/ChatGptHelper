from SeleniumAdapter.Action import BaseAction
from SeleniumAdapter.ExceptConditions import Conditions
import time
import typing as tp


class LoginPage(BaseAction):

    def toGPTHome(self):
        self.driver.visit_web(self.config_toGPTHome['url'])
        
    def click_login_button(self):
        login_button = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_click_login_button['by']), 
            self.config_click_login_button['element']
            )
        self.driver.click_element(login_button)
    
    def enter_username(self, username: str):
        username_input = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_enter_username['by']), 
            self.config_enter_username['element']
            )
        self.driver.send_keys(username_input, username)

    def enter_password(self, password: str):
        password_input = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_enter_password['by']), 
            self.config_enter_password['element']
            )
        self.driver.send_keys(password_input, password)

    def click_account_button(self):
        submit_button = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_click_account_button['by']), 
            self.config_click_account_button['element']
            )
        self.driver.click_element(submit_button)
        
    def click_password_button(self):
        submit_button = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_click_password_button['by']), 
            self.config_click_password_button['element']
            )
        self.driver.click_element(submit_button)
        
    def main(self, username:str, password:str):
        self.toGPTHome()
        self.click_login_button()
        self.enter_username(username)
        self.click_account_button()
        self.enter_password(password)
        self.click_password_button()
        

class GPTMainPage(BaseAction):
        
    def enter_message(self, message: str):
        testarea = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_enter_message['by']), 
            self.config_enter_message['element']
            )
        self.driver.clear_value(testarea)
        script = self.config_enter_message['script'].format(message)
        self.driver.execute_script(script, element=testarea)
        self.driver.send_keys(testarea, ' ')

    def click_send_button(self):
        send_button = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_click_send_button['by']), 
            self.config_click_send_button['element'],
            )
        self.driver.click_element(send_button)
    
    
    def get_GPT_ans(self, timeout=None) -> str:
        if timeout is None:
            timeout = self.timeout
            
        conversion = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_get_GPT_ans['by_conversion']), 
            self.config_get_GPT_ans['element_conversion'],
            )
        
        speaker = self.driver.find_element(
            self.get_by(self.config_get_GPT_ans['by_speaker']), 
            self.config_get_GPT_ans['element_speaker'], 
            web_element=conversion)
        
        speaker = self.driver.get_text(speaker)
        if speaker == self.config_get_GPT_ans['speaker']:
            _ = self.driver.wait_for_element(
                self.condition,
                self.get_by(self.config_get_GPT_ans['by_wait_target']), 
                self.config_get_GPT_ans['element_wait_target'], 
                web_element=conversion, 
                timeout=timeout)
            
            response_area = self.driver.wait_for_element(
                self.condition,
                self.get_by(self.config_get_GPT_ans['by_response_area']), 
                self.config_get_GPT_ans['element_response_area'], 
                web_element=conversion)
        else:
            print(f"Error: Unexpected speaker detected. Actual speaker: {speaker}, Expected speaker: {self.config_get_GPT_ans['speaker']}")
        text = self.driver.get_text(response_area)
        return text
    
    def logout(self):
        if self.driver.find_elements(
            self.get_by(self.config_logout['by_side_menu']), 
            self.config_logout['element_side_menu']):
            button_side_menu = self.driver.find_element(
                self.get_by(self.config_logout['by_side_menu']), 
                self.config_logout['element_side_menu'])
            self.driver.click_element(button_side_menu)

        button_user = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_logout['by_user']), 
            self.config_logout['element_user']
            )
        self.driver.click_element(button_user)
        
        self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_logout['by_wait_user_menu']),
            self.config_logout['element_wait_user_menu']
        )

        elements = []
        while not elements:
            elements = self.driver.find_elements(
            self.get_by(self.config_logout['by_logout']), 
            self.config_logout['element_logout']
            )

        for element in elements:
            if self.config_logout['keyword_logout'] in self.driver.get_text(element).lower():
                self.driver.click_element(element)
    
    def delete_current_chat(self):

        if self.driver.find_elements(
            self.get_by(self.config_logout['by_side_menu']), 
            self.config_logout['element_side_menu']):
            button_side_menu = self.driver.find_element(
                self.get_by(self.config_logout['by_side_menu']), 
                self.config_logout['element_side_menu'])
            self.driver.click_element(button_side_menu)
        
        current_url = self.driver.get_current_url()
        chat_id = '/' + '/'.join(current_url.split('/')[-2:])
        element_chat = self.config_delete_current_chat['element_chat'].format(chat_id)
        for element in self.driver.find_elements(
            self.get_by(self.config_delete_current_chat['by_group']),
            self.config_delete_current_chat['element_group']):
            if self.driver.find_elements(
                self.get_by(self.config_delete_current_chat['by_chat']), element_chat, element):
                pop_menu_btn = self.driver.find_element(
                    self.get_by(self.config_delete_current_chat['by_pop_menu']), 
                    self.config_delete_current_chat['element_pop_menu'],
                    element)
                self.driver.click_element(pop_menu_btn)
                break
        
        keyword_delete = self.config_delete_current_chat['keyword_delete']
        for element in self.driver.find_elements(
            self.get_by(self.config_delete_current_chat['by_delete']),
            self.config_delete_current_chat['element_delete']):
            
            tag = self.driver.get_text(element).lower()
            if keyword_delete in tag:
                self.driver.click_element(element)
                break
        
        dialog = self.driver.wait_for_element(
            self.condition,
            self.get_by(self.config_delete_current_chat['by_dbcheck_dialog']),
            self.config_delete_current_chat['element_dbcheck_dialog']
        )

        keyword_delete_dbcheck = self.config_delete_current_chat['keyword_delete_dbcheck']
        for element in self.driver.find_elements(
            self.get_by(self.config_delete_current_chat['by_delete_dbcheck']),
            self.config_delete_current_chat['element_delete_dbcheck'],
            dialog):
            
            tag = self.driver.get_text(element).lower()
            if keyword_delete_dbcheck in tag:
                self.driver.click_element(element)
                break


    def main(self, message: str):
        self.enter_message(message)
        self.click_send_button()
        time.sleep(1)
        text = self.get_GPT_ans(self.config_get_GPT_ans['timeout'])
        return text