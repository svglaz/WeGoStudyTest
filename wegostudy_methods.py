import datetime
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# s = Service(executable_path='../chromedriver')
# driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------***--------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegostudy_url)
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f'Yey! {locators.app} website launched successfully')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.wegostudy_url:
        driver.find_element(By.LINK_TEXT, 'LOGIN').click()
        sleep(0.25)

        if driver.find_element(By.XPATH, '//div[contains(@class, "authentication_form")]').is_displayed():
            print(f'Pop up window is displayed.')
            sleep(0.25)
            driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
            sleep(0.25)
            driver.find_element(By.ID, 'user_password').send_keys(locators.user_password)
            sleep(0.25)
            driver.find_element(By.XPATH, '//input[contains(@value, "SIGN IN")]').click()
            sleep(1.5)

            if driver.current_url == locators.partner_home_page:
                assert driver.find_element(By.XPATH, '//div[contains(text(), "Signed in successfully.")]').is_displayed()
                assert driver.find_element(By.LINK_TEXT, locators.user_name).is_displayed()
                print(f'Signed in successfully at {datetime.datetime.now()}. Username: {locators.user_name}')
            else:
                print(f'Login is not successful. Check your code or website and try again.')


def log_out():
    # driver.find_element(By.XPATH, '//div[@id="toast-container"]').click()
    # sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
    sleep(0.5)
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    sleep(0.5)
    assert driver.current_url == locators.wegostudy_url
    assert driver.find_element(By.XPATH, '//div[contains(text(), "Signed out successfully.")]').is_displayed()
    print(f'Signed out successfully at {datetime.datetime.now()}')


def create_new_student():
    assert driver.current_url == locators.partner_home_page
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    assert driver.current_url == locators.partner_student_details_page
    assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(1)

    # _______________________________User Picture________________________________

    driver.find_element(By.ID, 'imageUpload').send_keys('C:/Users/Sveta/Desktop/WeGoStudyTest/StudentImage.png')
    sleep(0.5)

    # ____________________________Personal Information___________________________

    if driver.current_url == locators.partner_new_student_page:
        assert driver.current_url == locators.partner_new_student_page
        print(f'We are on new student page.')
        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').send_keys(locators.middle_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.preferred_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
        sleep(0.3)
        driver.find_element(By.XPATH, '//span[text()="Country of citizenship"]').click()
        sleep(0.3)
        c = random.randint(254, 500)
        driver.find_element(By.XPATH, f"//option[@data-select2-id='{c}']").click()
        sleep(0.3)
        driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
        sleep(0.3)
        driver.find_element(By.ID, 'phone_number').send_keys(locators.passport_number)
        sleep(0.3)

    # __________________________Contact Information_________________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_apartment_number').send_keys(locators.aprt_number)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.mailing_address)
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'Country').click()
        sleep(0.3)
        driver.find_element(By.XPATH, '//li[@data-option-array-index="21"]').click()
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'Province/State').click()
        sleep(0.3)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[2]').click()
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'City').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[3]').click()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postal_code)
        sleep(0.3)
        driver.find_element(By.ID, 'user_email').send_keys(locators.email_address)
        sleep(0.3)

        # ____________________________Education Information_______________________

        driver.find_element(By.LINK_TEXT, 'Credentials').click()
        sleep(0.5)
        driver.find_element(By.XPATH,
                           '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/ul/li[2]').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').send_keys('CCTB')
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').send_keys('ISAQM')
        sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'GPA Scale').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//div[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div[1]/ul[1]/li[5]').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').send_keys('75')
        sleep(0.5)
        driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-green-br ml-auto btn-xs form-group add_fields")]').click()
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='custom-select chosen-select']")).select_by_value('Certificate')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='School Name'])[1]").send_keys('CCTB')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Program'])[1]").send_keys('ISAQM')
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='form-control chosen-select']")).select_by_value('100')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='GPA'])[1]").send_keys('90')
        sleep(0.75)
        driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-red-br")]').click()
        sleep(0.5)

        # ________________________________Documents____________________________________

        driver.find_element(By.XPATH, '//i[@class="fa fa-question-circle"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//a[@data-toggle="tooltip"]').is_displayed()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_documents_attributes_0_file').send_keys('C:/Users/Sveta/Desktop/WeGoStudyTest/TestDocument_1.pdf')
        sleep(0.5)
        driver.find_element(By.XPATH,
                            '//a[contains(@class,"btn btn-green-br ml-auto btn-xs mb-3 add_fields")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '(//input[contains(@class, "form-control-file")])[2]').send_keys('C:/Users/Sveta/Desktop/WeGoStudyTest/TestDocument_2.pdf')
        sleep(2)
        driver.find_element(By.XPATH, '(//i[@class="fa fa-times"])[2]').click()
        sleep(0.5)

        # ___________________________Work Experience____________________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_type_of_industry').send_keys('Business')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_position_rank').send_keys('2')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_employer').send_keys('ABC')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_title').send_keys('Account Manager')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_job_description').send_keys(locators.job_description)
        sleep(0.3)
        driver.find_element(By.XPATH, '//a[contains(@class, "btn btn-green-br ml-auto btn-xs add_fields")]').click()
        sleep(0.3)
        driver.find_element(By.XPATH, "(//input[@placeholder='Industry'])[1]").send_keys('Commerce')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Rank'])[1]").send_keys('5')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Employer'])[1]").send_keys('Perl')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Title'])[1]").send_keys('Accountant')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//textarea[@placeholder='Job Description'])[1]").send_keys(locators.job_description)
        sleep(0.5)
        driver.find_element(By.XPATH, '(//a[contains(@class,"btn btn-red-br")])[2]').click()
        sleep(0.3)
        print(f'All fields are populated.')
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//div[contains(text(), "Student is created successfully.")]').is_displayed()
        sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Students').click()
        sleep(1)
        assert driver.current_url == locators.partner_student_details_page
        assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()
        if driver.find_element(By.XPATH, f'//h4[contains(., "{locators.full_name}")]').is_displayed():
            print(f'New student is created successfully.')

