from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def setup():
    # Set up a new test (open browser to target URL).
    browser.get('https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag/')
    sleep(1)


def teardown():
    # Teardown completed test (close browser).
    browser.quit()

def enter_email_valid():
    # Enter a valid email address in the "E-Mail Adresse" field and try to continue to next page of form.
    setup()
    email_label = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[1]/div/div/div[2]/div[3]/label')
    email_text_box = browser.find_element(By.ID,"email")
    email_label_color = email_label.value_of_css_property("color")
    weiter_button = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[6]/div[2]/div/div[1]/button')
    assert email_label_color == "rgb(51, 51, 51)", "Email label is not grey, indicating input error to user."
    email_text_box.send_keys('email@domain.de')
    assert email_text_box.get_attribute("value") == 'email@domain.de'
    browser.execute_script("arguments[0].click();", weiter_button)
    sleep(1)
    email_label_color = email_label.value_of_css_property("color")
    assert email_label_color == "rgb(51, 51, 51)", "Email address is entered correctly, but email label color is not grey, indicating input error to user."


def enter_email_missing_domain():
    # Enter an email address in the "E-Mail Adresse" field without a domain and try to continue to next page of form.
    setup()
    email_label = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[1]/div/div/div[2]/div[3]/label')
    email_text_box = browser.find_element(By.ID, "email")
    email_label_color = email_label.value_of_css_property("color")
    weiter_button = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[6]/div[2]/div/div[1]/button')
    assert email_label_color == "rgb(51, 51, 51)", "Email label is not grey, indicating input error to user."
    email_text_box.send_keys('email')
    assert email_text_box.get_attribute("value") == 'email'
    browser.execute_script("arguments[0].click();", weiter_button)
    sleep(1)
    email_label_color = email_label.value_of_css_property("color")
    assert email_label_color == "rgb(240, 61, 63)", "Email address is missing domain, but input error is not highlighted to user."


def enter_email_invalid_domain():
    # Enter an email address in the "E-Mail Adresse" field with an invalid domain and try to continue to next page of form.
    setup()
    email_label = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[1]/div/div/div[2]/div[3]/label')
    email_text_box = browser.find_element(By.ID, "email")
    email_label_color = email_label.value_of_css_property("color")
    weiter_button = browser.find_element(By.XPATH, '//*[@id="wizard-content"]/div/div/form/div[6]/div[2]/div/div[1]/button')
    assert email_label_color == "rgb(51, 51, 51)", "Email label is not grey, indicating input error to user."
    email_text_box.send_keys('email@domain')
    assert email_text_box.get_attribute("value") == 'email@domain'
    browser.execute_script("arguments[0].click();", weiter_button)
    sleep(10)
    email_label_color = email_label.value_of_css_property("color")
    assert email_label_color == "rgb(240, 61, 63)", "Email address domain is invalid, but input error is not highlighted to user."


if __name__ == '__main__':
    browser = webdriver.Safari()
    enter_email_valid()
    enter_email_missing_domain()
    enter_email_invalid_domain()
    teardown()


