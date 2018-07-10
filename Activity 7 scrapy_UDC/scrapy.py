import sys

from settings import driver, get_element


def login():
    code, password = sys.argv[1:]
    driver.find_element_by_id('codprs').send_keys(code[7:])
    driver.find_element_by_id('pswprs').send_keys(password[7:])
    driver.find_element_by_name('btnLogin').submit()


def get_notes_session():
    consult = get_element(path="//*[@id='ulMenu']/li[3]/a/span").click()
    students = get_element(path="//*[@id='ulMenu']/li[3]/ul/li/a").click()
    get_element(path="//*[@id='ulMenu']/li[3]/ul/li/ul/li[2]/a").click()
    get_element(path="//*[@id='liveclock']").click()


login()
get_notes_session()
