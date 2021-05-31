from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from tkinter.ttk import Progressbar
import csv
import pathlib
import os
import traceback

options = Options()
#URL, URL_Authors, DELAY, AUTHORS_NO, EMAIL, PASSWORD = GUI.start_operation()
DOCUMENTS_URL = "https://0810579vq-1103-y-https-www-scopus-com.mplbci.ekb.eg/results/results.uri?sort=plf-f&src=s&sid=031e69493870eb4af1d0676d03b75236&sot=aff&sdt=a&sl=15&s=AF-ID%2860013750%29&origin=AffiliationProfile&editSaveSearch=&txGid=2a61ed52f45f6d8549e428040be71c7e"
DELAY1 = 4
YEAR_NO = 14
AUTHOR_NO_DOC = 40
SUBJECT_NO = 20
KEYWORD_NO = 30
FUNDING_NO = 30
COUNTRY_NO = 40


def document_parse(DOCUMENTS_URL, DELAY1, YEAR_NO, AUTHOR_NO_DOC, SUBJECT_NO, KEYWORD_NO, FUNDING_NO, COUNTRY_NO, PATH, EMAIL, PASSWORD, START, CMD, Headless, option_type, option_keyword, option_fund, option_country, bar, window):
    def click_overlay(button):
        time.sleep(DELAY1)
        try:
            button.click()
        except:
            try:
                try:
                    close_overlay = driver.find_element_by_class_name(
                        "_pendo-close-guide")
                except:
                    close_overlay = driver.find_element_by_class_name(
                        "_pendo-close-guide_")
                close_overlay.click()
                button.click()
            except:
                ActionChains(driver).move_to_element(button).click().perform()

    def parse(input_str, no=0):
        if no == 1:
            str_inp = input_str.text.split("\n")
            invalid = []
            titles = []
            for x in str_inp:
                l = x.strip("()")
                if l.isdigit() != True:
                    invalid.append(x)
                elif x.isdigit():
                    titles.append(x)
            for x in invalid:
                if x in str_inp:
                    str_inp.remove(x)
            for x in titles:
                if x in str_inp:
                    str_inp.remove(x)
            return str_inp, titles
        else:
            str_inp = input_str.text.split("\n")
            invalid = []
            titles = []
            for x in str_inp:
                l = x.strip("()")
                if l.isdigit() != True and "Show" not in l:
                    titles.append(x)
                elif l.isdigit() != True and "Show" in l:
                    invalid.append(x)
            for x in invalid:
                if x in str_inp:
                    str_inp.remove(x)
            for x in titles:
                if x in str_inp:
                    str_inp.remove(x)
            return str_inp, titles

    def get_data(id1, css_selector2, css_selector3, id4, id5=0, button_no=0):
        element1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, id1)))
        toggle = element1.get_attribute("aria-expanded")
        if toggle == "true":
            pass
        elif toggle == "false":
            click_overlay(element1)
        time.sleep(DELAY1)
        try:
            try:
                element2 = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector2)))
                click_overlay(element2)
            except:
                btnn = driver.find_element_by_css_selector(css_selector2)
                click_overlay(btnn)
            time.sleep(DELAY1)
        except:
            pass
        if css_selector3 != "":
            try:
                element3 = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector3)))
                click_overlay(element3)
                time.sleep(DELAY1)
                data = driver.find_element_by_id(id4)
                data_titles, data_count = parse(data)
                close_btn = driver.find_elements_by_css_selector(
                    "button.close")
                click_overlay(close_btn[button_no])
            except:
                data = driver.find_element_by_id(id5)
                data_titles, data_count = parse(data)
        else:
            data = driver.find_element_by_id(id4)
            data_titles, data_count = parse(data)
        return data_titles, data_count

    options = Options()
    options.headless = Headless
    all_data = []
    YEAR_NO = int(YEAR_NO)
    AUTHOR_NO_DOC = int(AUTHOR_NO_DOC)
    DELAY1 = int(DELAY1)
    SUBJECT_NO = int(SUBJECT_NO)
    KEYWORD_NO = int(KEYWORD_NO)
    FUNDING_NO = int(FUNDING_NO)
    COUNTRY_NO = int(COUNTRY_NO)
    START = 2021 - int(START)
    START_Fixed = START

    driver = webdriver.Firefox(
        options=options, executable_path=PATH + r'\geckodriver.exe')
    driver.get(DOCUMENTS_URL)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, '_58_login')))
    login = driver.find_element_by_id("_58_login")
    login.send_keys(EMAIL)
    login2 = driver.find_element_by_id("_58_password")
    login2.send_keys(PASSWORD)
    login_button = driver.find_element_by_css_selector(
        "button.btn.btn-default.mb-2.btn-primary")
    login_button.click()

    driver.get(DOCUMENTS_URL)
    show_more = driver.find_element_by_css_selector("a#viewMoreLink_PUBYEAR")
    click_overlay(show_more)
    show_all = driver.find_element_by_css_selector("a#viewAllLink_PUBYEAR")
    click_overlay(show_all)
    time.sleep(DELAY1)
    years_elem = driver.find_element_by_id("overlayBody_PUBYEAR")
    years, str_years = parse(years_elem, 1)
    flag1 = 0
    driver.get(DOCUMENTS_URL)
    while(START < YEAR_NO + START_Fixed):
        bar['value'] = ((START - 1)/(YEAR_NO) * 100)
        window.update()
        try:
            driver.get(DOCUMENTS_URL)
            try:
                show_more = driver.find_element_by_css_selector(
                    "a#viewMoreLink_PUBYEAR")
                click_overlay(show_more)
            except:
                pass
            show_all = driver.find_element_by_css_selector(
                "a#viewAllLink_PUBYEAR")
            click_overlay(show_all)
            time.sleep(DELAY1)
            button = driver.find_element_by_css_selector(
                "li#li_160" + str(2021 - START) + ".checkbox")
            click_overlay(button)
            button2 = driver.find_element_by_name("limitTo")
            action = webdriver.common.action_chains.ActionChains(driver)
            action.move_to_element_with_offset(button2, 2, 2)
            action.click()
            action.perform()
            btn = driver.find_element_by_css_selector(
                "input.btn.btn-primary.btn-sm.limitToButton.btnLmtExcEnable")
            click_overlay(btn)

            try:
                author_but1 = driver.find_element_by_css_selector(
                    "a#viewMoreLink_AUTHOR_NAME_AND_ID")
                click_overlay(author_but1)
            except:
                pass
            author_but2 = driver.find_element_by_css_selector(
                "a#viewAllLink_AUTHOR_NAME_AND_ID")
            click_overlay(author_but2)
            time.sleep(DELAY1)
            authors = driver.find_element_by_id(
                "overlayBody_AUTHOR_NAME_AND_ID")
            author_count, author_names = parse(authors)
            close_btn = driver.find_elements_by_css_selector("button.close")
            click_overlay(close_btn[2])

            try:
                subj_but1 = driver.find_element_by_css_selector(
                    "a#viewMoreLink_SUBJAREA")
                click_overlay(subj_but1)
            except:
                pass
            subj_but2 = driver.find_element_by_css_selector(
                "a#viewAllLink_SUBJAREA")
            click_overlay(subj_but2)
            time.sleep(DELAY1)
            subjects = driver.find_element_by_id("overlayBody_SUBJAREA")
            subject_count, subject_titles = parse(subjects)
            close_btn = driver.find_elements_by_css_selector("button.close")
            click_overlay(close_btn[3])

            type_count, type_titles = get_data(
                "collapse_DOCTYPE_link", "a#viewMoreLink_DOCTYPE", "", "clusterAttribute_DOCTYPE")
            keyword_count, keyword_titles = get_data("collapse_EXACTKEYWORD_link", "a#viewMoreLink_EXACTKEYWORD",
                                                     "a#viewAllLink_EXACTKEYWORD", "overlayBody_EXACTKEYWORD", "clusterAttribute_EXACTKEYWORD", 7)
            funding_count, funding_titles = get_data("collapse_FUND-SPONSOR_link", "a#viewMoreLink_FUND-SPONSOR",
                                                     "a#viewAllLink_FUND-SPONSOR", "overlayBody_FUND-SPONSOR", "clusterAttribute_FUND-SPONSOR", 9)
            country_count, country_titles = get_data("collapse_COUNTRY_NAME_link", "a#viewMoreLink_COUNTRY_NAME",
                                                     "a#viewAllLink_COUNTRY_NAME", "overlayBody_COUNTRY_NAME", "clusterAttribute_COUNTRY_NAME", 10)
            if CMD != "":
                args = CMD.split(",")
                custom_count, custom_titles = get_data(
                    args[0], "a#" + str(args[1]), "a#" + str(args[2]), args[3], args[4], int(args[5]))
            output = []
            output.append(str_years[START])
            output.append(years[START].strip("()"))
            for q in range(AUTHOR_NO_DOC):
                try:
                    output.append(author_names[q])
                    output.append(author_count[q].strip("()"))
                except:
                    for k in range(2):
                        output.append("")
            for q in range(SUBJECT_NO):
                try:
                    output.append(subject_titles[q])
                    output.append(subject_count[q].strip("()"))
                except:
                    for k in range(2):
                        output.append("")
            if option_type == True:
                for q in range(10):
                    try:
                        output.append(type_titles[q])
                        output.append(type_count[q].strip("()"))
                    except:
                        for k in range(2):
                            output.append("")
            if option_keyword == True:
                for q in range(KEYWORD_NO):
                    try:
                        output.append(keyword_titles[q])
                        output.append(keyword_count[q].strip("()"))
                    except:
                        for k in range(2):
                            output.append("")
            if option_fund == True:
                for q in range(FUNDING_NO):
                    try:
                        output.append(funding_titles[q])
                        output.append(funding_count[q].strip("()"))
                    except:
                        for k in range(2):
                            output.append("")
            if option_country == True:
                for q in range(COUNTRY_NO):
                    try:
                        output.append(country_titles[q])
                        output.append(country_count[q].strip("()"))
                    except:
                        for k in range(2):
                            output.append("")
            if CMD != "":
                for q in range(20):
                    try:
                        output.append(custom_titles[q])
                        output.append(custom_count[q].strip("()"))
                    except:
                        for k in range(2):
                            output.append("")
            print(output)
            if flag1 == 0:
                print("Adding Heads")
                with open(PATH + "\Output\Documents.csv", "w+", encoding="utf-8") as doc_output:
                    writer = csv.writer(doc_output)
                    heads = ["Year", "No."]
                    for m in range(1, AUTHOR_NO_DOC + 1):
                        heads.append("Author" + str(m))
                        heads.append("AuthorNo" + str(m))
                    for m in range(1, SUBJECT_NO + 1):
                        heads.append("Subject" + str(m))
                        heads.append("SubjectNo" + str(m))
                    # CHANGE TO TYPES
                    for m in range(1, 11):
                        heads.append("Type" + str(m))
                        heads.append("TypeNo" + str(m))
                    for m in range(1, KEYWORD_NO + 1):
                        heads.append("Keyword" + str(m))
                        heads.append("KeywordNo" + str(m))
                    for m in range(1, FUNDING_NO + 1):
                        heads.append("Funding" + str(m))
                        heads.append("FundingNo" + str(m))
                    for m in range(1, COUNTRY_NO + 1):
                        heads.append("Country" + str(m))
                        heads.append("CountryNo" + str(m))
                    writer.writerow(heads)
                    flag1 = 1
            if flag1 == 1:
                print("Appending...")
                with open(PATH + "\Output\Documents.csv", "a", encoding="utf-8") as doc_output:
                    writer = csv.writer(doc_output)
                    writer.writerow(output)
                    all_data.append(output)
            START += 1
            print(START)
        except:
            print(traceback.format_exc())
            print(str(2021 - START) + " Failed\n Retrying...")
            pass
    driver.close()
    return all_data
