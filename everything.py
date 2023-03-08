import os
import undetected_chromedriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from test_dataset import *


os.environ['PATH'] += r'C:/SeleniumDrivers'
driver = undetected_chromedriver.Chrome()
wait = WebDriverWait(driver, 10)
action_chains = ActionChains(driver)

# Open browser
driver.get('https://id.atlassian.com/login')
driver.maximize_window()
driver.implicitly_wait(10)

class User:
    def __init__(self, email, password, logged=False):
        self.email = email
        self.password = password
        self.logged = logged


    def login(self):
        driver.implicitly_wait(10)
        email_field = driver.find_element(By.ID, 'username')
        email_field.send_keys(self.email)
        continue_button = driver.find_element(By.ID, 'login-submit')
        continue_button.click()

        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(self.password)
        continue_button.click()


    def go_to_jira_project(self, domain_href, project_href):
        driver.implicitly_wait(10)
        jira_domain = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, domain_href)))
        jira_domain.click()
        jira_project = driver.find_element(By.CSS_SELECTOR, project_href)
        jira_project.click()


    def create_issue(self, issue_type=None, summary=None, labels=None, priority=None, create_another=None):
        issue_types = ['Epic', 'Story', 'Task', 'Bug']

        def open_issue_window(self):
            try:
                create_button_to_open_window = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/header/nav/div[2]/div[7]/span/div/button[1]')))
                create_button_to_open_window.click()
                return
            except:
                pass
            
            try:
                create_button_to_open_window = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/header/nav/div[2]/div[7]/span/div/button[1]')))
                create_button_to_open_window.click()
                return
            except:
                pass

            try:
                create_button_to_open_window = wait.until(EC.element_to_be_clickable((By.ID, 'createGlobalItem')))
                create_button_to_open_window.click()
                return
            except:
                pass
            
            try:
                create_button_to_open_window = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createGlobalItem"])')))
                create_button_to_open_window.click()
                return
            except:
                pass

        def submit_issue_creation(self):
            try:
                create_issue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div[2]/div/div[3]/div/div/section/div[3]/button')))
                create_issue_button.click()
                return
            except:
                pass

            try:
                create_issue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[form="issue-create.ui.modal.create-form"]')))
                create_issue_button.click()
                return
            except:
                pass

            try:
                create_issue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-ryxqcb')))
                create_issue_button.click()
                return
            except:
                pass

            try:
                create_issue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="issue-create.ui.modal.create-form"]/div[3]/div/div[3]/div/div/section/div[3]/button')))
                create_issue_button.click()
                return
            except:
                pass

        def check_if_summary_is_empty(self):
            try:
                summary_field = driver.find_element(By.ID, 'summary-field')
                if summary_field.text == '':
                    try:
                        cancel_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="css-1m7s2s2"]')))
                        cancel_button.click()
                        return True
                    except:
                        pass
                else:
                    return False
            except:
                return False

        def change_issue_type(self):
            if issue_type in issue_types:
                try:
                    issue_type_field = driver.find_element(By.ID, 'issue-create.ui.modal.create-form.type-picker.issue-type-select')
                    action_chains.move_to_element(issue_type_field).perform()
                    action_chains.move_to_element(issue_type_field).click().send_keys(issue_type).send_keys(Keys.RETURN).perform()
                except:
                    return
            elif issue_type == None:
                pass
            else:
                print(f'Invalid issue type {issue_type}. Please choose one of the following: {issue_types}')

            if issue_type == 'Epic':
                try:
                    epic_name_field = driver.find_element(By.ID, 'customfield_10011-field')
                    epic_name_field.send_keys('Test epic')
                except:
                    return

        def add_summary(self):
            if summary != None:
                try:
                    summary_field = wait.until(EC.element_to_be_clickable((By.ID, 'summary-field')))
                    summary_field.send_keys(summary)
                except:
                    pass

        def change_priority(self):
            try:
                if priority != None and priority != 'Medium':
                    priority_field = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-9-input')))
                    action_chains.move_to_element(priority_field).click().send_keys(priority).perform()
                    action_chains.move_to_element(priority_field).send_keys(Keys.RETURN).perform()
                
                    if priority == 'High':
                        action_chains.move_to_element(priority_field).click().send_keys(priority).perform()
                        action_chains.move_to_element(priority_field).send_keys(Keys.RETURN).perform()
            except:
                pass

            try:
                if priority != None and priority != 'Medium':
                    priority_field = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-7-input')))
                    action_chains.move_to_element(priority_field).click().send_keys(priority).perform()
                    action_chains.move_to_element(priority_field).send_keys(Keys.RETURN).perform()
            
                if priority == 'High':
                    action_chains.move_to_element(priority_field).click().send_keys(priority).perform()
                    action_chains.move_to_element(priority_field).send_keys(Keys.RETURN).perform()
            except:
                pass

        def add_labels(self):
            if labels != None:
                label_field = driver.find_element(By.XPATH, '//*[@id="react-select-10-input"]')
                for label in labels:
                    action_chains.move_to_element(label_field).click().send_keys(label).perform()
                    time.sleep(1)
                    action_chains.move_to_element(label_field).send_keys(Keys.RETURN).perform()

        open_issue_window(self)
        change_issue_type(self)
        add_summary(self)
        change_priority(self)
        add_labels(self)
        submit_issue_creation(self)
        check_if_summary_is_empty(self)


class TestSet:
    def __init__(self, tests):
        self.tests = tests

    def run(self):
        for test in self.tests:
            test()

def test_issue_type(user, issue_type_dataset):
    for key in issue_type_dataset:
        issue_type_data = issue_type_dataset[key]['issue_type']
        issue_summary_data = issue_type_dataset[key]['summary']
        user.create_issue(issue_type=issue_type_data, summary=issue_summary_data)
        
def test_issue_summary(user, issue_summary_dataset):
    for key in issue_summary_dataset:
        issue_summary_data = issue_summary_dataset[key]['summary']
        user.create_issue(summary=issue_summary_data)

        if issue_summary_data == '':
            driver.refresh()
        elif issue_summary_data == '    ':
            discard_issue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[23]/div[3]/div/div[3]/div/div/section/div[3]/button[2]')))
            discard_issue_button.click()

def test_issue_priority(user, issue_priority_dataset):
    for key in issue_priority_dataset:
        issue_summary_data = issue_priority_dataset[key]['summary']
        issue_priority_data = issue_priority_dataset[key]['priority']
        user.create_issue(summary=issue_summary_data, priority=issue_priority_data)

def test_issue_label(user, issue_label_dataset):
    for key in issue_label_dataset:
        issue_summary_data = issue_label_dataset[key]['summary']
        issue_label_data = []
        issue_label_data.append(issue_label_dataset[key]['label'])
        user.create_issue(summary=issue_summary_data, labels=issue_label_data)
        

jira_domain_link = 'a[href="https://id.atlassian.com/login?login_hint=test900@int.pl&prompt=none&continue=https://test-900.atlassian.net/secure/BrowseProjects.jspa?selectedProjectType=software"]'
jira_project_link = 'a[href="/browse/TES"]'

user_test900 = User('test900@int.pl', 'password1')
user_test900.login()
user_test900.go_to_jira_project(jira_domain_link, jira_project_link)

testset_01 = TestSet(tests=[
            test_issue_type(user_test900, issue_type_dataset),
            test_issue_priority(user_test900, issue_priority_dataset),
            test_issue_summary(user_test900, issue_summary_dataset),
            test_issue_label(user_test900, issue_label_dataset)])
testset_01.run()
