from time import sleep

from selenium import webdriver
import argparse


def changelicense(driver=None, license=None):
    el_dropbox = driver.find_element_by_class_name('ui-dropdown-closed').click()
    for e_license in driver.find_elements_by_tag_name('li'):
        if e_license.get_attribute('data-text') == license:
            e_license.click()
            break


def clickNext(driver=None):
    for e in driver.find_elements_by_tag_name('a'):
        if e.get_attribute('data-track') == "nextPhotoButtonClick":
            e.click()
            break


parser = argparse.ArgumentParser(description="Change multiple photo's license in Flickr")
parser.add_argument('email', type=str, help='e-mail')
parser.add_argument('password', type=str, help='password')
parser.add_argument('license', type=str, help='license')

# Public Domain Work
# Public Domain Dedication (CC0)
# Attribution
# Attribution-ShareAlike
# Attribution-NoDerivs
# Attribution-NonCommercial
# Attribution-NonCommercial-ShareAlike
# Attribution-NonCommercial-NoDerivs

args = parser.parse_args()

driver = webdriver.Firefox(executable_path="./geckodriver")

driver.get("https://identity.flickr.com/login")
driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(args.email)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/form/button/span').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(args.password)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/form/button').click()

sleep(5)
driver.find_element_by_link_text('You').click()
sleep(5)
driver.find_element_by_link_text('Albums').click()

sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/a/div/div/div[1]/h4').click()

sleep(5)
num_photos = driver.find_element_by_class_name("photo-counts").text
num_photos = int(num_photos.replace(" photos", ""))

# first picture
sleep(5)
driver.find_elements_by_class_name('photo-list-photo-interaction')[0].click()

i = 0
while i < num_photos:
    sleep(5)
    changelicense(driver=driver, license=args.license)
    clickNext(driver=driver)
    i = i + 1

