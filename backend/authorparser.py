from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import csv
import pathlib
import os
import traceback


# URL, URL_Authors, DELAY, AUTHORS_NO, EMAIL, PASSWORD = GUI.start_operation()
# DELAY = int(DELAY)
# AUTHORS_NO = int(AUTHORS_NO)
print("Created")

#        GUI.update_progress("err0")
#        GUI.window.update()
#        GUI.update_progress(0)
#        GUI.window.update()

""" driver.get(URL)
try:
    myElem = WebDriverWait(driver, DELAY).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'secondaryLink')))
except:
    time.sleep(DELAY)

GUI.update_progress(1)
GUI.master.update()
time.sleep(8)
numbers = driver.find_elements_by_class_name("secondaryLink")
titles = driver.find_elements_by_css_selector(
    "div.col-md-9.text-nowrap.ellipsisOverflow")
try:
    basic = driver.find_element_by_id("rolledupCard")
    flag = 1
except:
    flag = 0

for j in titles:
    pass
   # print(j.text)


invalid = []
counter0 = 0

for f in numbers:
    number = f.text.replace(",", "")
    # print(number)
    if (number).isdigit() == False:
        invalid.append(f)
        continue
    if counter0 == 0 and flag == 1:
        data_affiliation["Documents, whole institution"] = number
        invalid.append(f)
        counter0 +=1
        continue
    elif counter0 == 0 and flag == 0:
        data_affiliation["Documents, affiliation only"] = number
        invalid.append(f)
        counter0 +=1
        continue
    if counter0 == 1 and flag == 1:
        data_affiliation["Documents, affiliation only"] = number
        invalid.append(f)
        counter0 +=1
        continue
    elif counter0 == 1 and flag == 0:
        data_affiliation["Authors"] = number
        invalid.append(f)
        counter0+=2
    if counter0 == 2:
        data_affiliation["Authors"] = number
        invalid.append(f)
        counter0 +=1

for x in invalid:
    print(x.text)
    if x in numbers:
        numbers.remove(x)

counter = 0
for i in numbers:
    try:
        number = i.text.replace(",", "")
        print(number)
        data_affiliation[str(titles[counter].text)] = number
        counter += 1
    except:
        pass

print(data_affiliation) """


def author_parse(URL_Authors, DELAY, AUTHORS_NO, Headless, EMAIL, PASSWORD, option1=1, option2=1, option3=1):

    def close_overlay():
        time.sleep(DELAY)
        try:
            close_overlay = driver.find_element_by_class_name(
                "_pendo-close-guide")
        except:
            close_overlay = driver.find_element_by_class_name(
                "_pendo-close-guide_")
        close_overlay.click()

    options = Options()
    START = 2021
    END = 1969

    options.headless = Headless
    PATH = os.path.dirname(os.path.realpath(__file__))
    PATH2 = "\Output\Authors" + \
        str(datetime.now())[:-7].replace(":", " ") + ".csv"

#	GUI.update_progress(2)
#	GUI.window.update()
    time.sleep(3)

    all_data = []

    years = []
    for i in range(START, END, -1):
        years.append(i)
    types_tit = ["article", "conference paper", "book chapter",
                 "editorial", "review", "book", "erratum", "letter"]

    types_dict = {}
    flag1 = 0
    g = 0

    driver = webdriver.Firefox(
        options=options, executable_path=PATH + r'\geckodriver.exe')
    driver.get(URL_Authors)
    myElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, '_58_login')))
    login = driver.find_element_by_id("_58_login")
    login.send_keys(EMAIL)
    login2 = driver.find_element_by_id("_58_password")
    login2.send_keys(PASSWORD)
    login_button = driver.find_element_by_css_selector(
        "button.btn.btn-default.mb-2.btn-primary")
    login_button.click()

    while (g < AUTHORS_NO):
        flag = True
        author_data = []
        database_data = []
        types_dict = {}
        documents_dict = {}
        citations_dict = {}
        publications = []
        publications_data = []
        affil_dict = {}
        try:
            driver.get(URL_Authors)
            time.sleep(DELAY)
            affiliated_authors = driver.find_elements_by_class_name("docTitle")
            author = affiliated_authors[g].text
            try:
                affiliated_authors[g].click()
                time.sleep(DELAY)
            except:
                close_overlay()
                affiliated_authors[g].click()
                myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.tabLabel.button__text')))
                time.sleep(DELAY)
            label_elements = driver.find_elements_by_css_selector(
                "span.tabLabel.button__text")
            author_data_elements = driver.find_elements_by_class_name(
                "_1kYdpHTL20fs5Qk9XhXPVJ")
            if len(str(author)) < 2:
                raise Exception
            author_data.append(str(author))
            author_data.append(str(driver.current_url))
            database_data.append(str(author))
            database_data.append(str(driver.current_url))
            for i in author_data_elements:
                author_data.append(i.text)
                database_data.append(i.text)
            affiliations_button = driver.find_element_by_id(
                'scopus-author-profile-page-control-microui__scopus-author-general-information__showAllAuthorInfo')
            try:
                affiliations_button.click()
            except:
                close_overlay()
                affiliations_button.click()
            time.sleep(3)
            affiliations_table = driver.find_elements_by_class_name(
                'authorAffiliationHistory__table')[0]
            affiliations = affiliations_table.text.split('\n')[1:]
            for affiliation in affiliations:
                affiliation_elements = affiliation.split(' ')
                start_year = int(affiliation_elements[0])
                try:
                    end_year = int(affiliation_elements[2])
                    affiliation_name = ' '.join(affiliation_elements[3:])
                    affil_dict[affiliation_name] = list(
                        range(start_year, end_year+1))
                except:
                    affiliation_name = ' '.join(affiliation_elements[1:])
                    affil_dict[affiliation_name] = [start_year]
            database_data.append(affil_dict)
            print(affil_dict)
            for title in label_elements:
                if "Co-Authors" in title.text:
                    try:
                        title.click()
                    except:
                        close_overlay()
                        title.click()
                    time.sleep(DELAY)
                    table = driver.find_element_by_id("co-author-table")
                    coauthors_text = table.text.split('\n')
                    coauthors_text = coauthors_text[3:]
                    for element in coauthors_text:
                        element_components = element.split(' ')
                        author_data.append(' '.join(element_components[:-1]))
                        author_data.append(element_components[-1])
                    database_data.extend(coauthors_text)
                    if len(coauthors_text) < 8:
                        for x in range(8 - len(coauthors_text)):
                            author_data.append('No Coauthor')
                            database_data.append('No Coauthor')

                if (title.text) == "Topics":
                    try:
                        title.click()
                    except:
                        close_overlay()
                        title.click()
                    time.sleep(DELAY)
                    for i in range(5):
                        try:
                            id = "scopus-author-profile-page-control-microui__scopus-author-topics__topics-table--topic-name-button" + \
                                str(i)
                            topic = driver.find_element_by_id(id)
                            author_data.append(topic.text)
                            database_data.append(topic.text)
                        except Exception as e:
                            print(e)
                            author_data.append("No topic")
                            database_data.append('No topic')
                            # print("no topic")
                if "Documents" in title.text and flag == True:
                    try:
                        title.click()
                    except:
                        close_overlay()
                        title.click()
                    exportbutton = driver.find_element_by_id('export_results')
                    try:
                        exportbutton.click()
                    except:
                        close_overlay()
                        exportbutton.click()
                    time.sleep(DELAY)
                    textoption = driver.find_elements_by_class_name(
                        'radio-inline')
                    try:
                        textoption[6].click()
                    except:
                        close_overlay()
                        textoption.click()
                    window_before = driver.window_handles[0]
                    print(window_before)
                    export = driver.find_element_by_id('exportTrigger')
                    try:
                        export.click()
                    except:
                        close_overlay()
                        export.click()
                    window_after = driver.window_handles[1]
                    driver.switch_to.window(window_after)
                    time.sleep(DELAY)
                    body = driver.find_element_by_css_selector('body')
                    body_elements = body.text.split('\n')[2:]
                    for i in range(len(body_elements)):
                        if "source:" in body_elements[i].lower():
                            if ("source:" in body_elements[i-10].lower()) or (10 > i):
                                publications.append(
                                    ('##'.join(body_elements[i-8:i+1])).lstrip('##'))
                                # print(body_elements[i-8:i+1])
                                # print(
                                #    ('##'.join(body_elements[i-8:i+1])).lstrip('##'))
                                #e = input('ee')
                            elif ("source:" in body_elements[i-11].lower()) or (11 > i):
                                publications.append(
                                    ('##'.join(body_elements[i-9:i+1])).lstrip('##'))
                                # print(body_elements[i-9:i+1])
                                # print(
                                #    ('##'.join(body_elements[i-9:i+1])).lstrip('##'))
                                #e = input('ee')
                            elif ("source:" in body_elements[i-12].lower()) or (12 > i):
                                publications.append(
                                    ('##'.join(body_elements[i-10:i+1])).lstrip('##'))
                                # print(body_elements[i-10:i+1])
                                # print(
                                #    ('##'.join(body_elements[i-10:i+1])).lstrip('##'))
                                #e = input('ee')

                    for publication in publications:
                        # print(publication)
                        #e = input('--')
                        publication_elements = publication.split(
                            '##')
                        if publication_elements[0] == '' or publication_elements[0] == '\n':
                            print('here')
                            publication_elements = publication_elements[1:]
                        # print(publication_elements)
                        #e = input('---')
                        publ_dict = {}
                        publ_dict['Authors'] = publication_elements[0]
                        publ_dict['Author_ids'] = publication_elements[1]
                        publ_dict['Publication Title'] = publication_elements[2]
                        publ_dict['Journal'] = publication_elements[3]
                        publ_dict['Publication link'] = publication_elements[4]
                        if len(publication_elements) > 10:
                            publ_dict['DOI'] = publication_elements[6][publication_elements[6].find(
                                ':')+2:]
                            publ_dict['Type'] = publication_elements[7][publication_elements[7].find(
                                ':')+2:]
                            publ_dict['Stage'] = publication_elements[8][publication_elements[8].find(
                                ':')+2:]
                            publ_dict['Access'] = publication_elements[9][publication_elements[9].find(
                                ':')+2:]
                            publ_dict['Source'] = publication_elements[10][publication_elements[10].find(
                                ':')+2:]
                        elif len(publication_elements) > 9:
                            publ_dict['DOI'] = publication_elements[6][publication_elements[6].find(
                                ':')+2:]
                            publ_dict['Type'] = publication_elements[7][publication_elements[7].find(
                                ':')+2:]
                            publ_dict['Stage'] = publication_elements[8][publication_elements[8].find(
                                ':')+2:]
                            publ_dict['Access'] = 'N/A'
                            publ_dict['Source'] = publication_elements[9][publication_elements[9].find(
                                ':')+2:]
                        else:
                            publ_dict['DOI'] = 'N/A'
                            publ_dict['Type'] = publication_elements[6][publication_elements[6].find(
                                ':')+2:]
                            publ_dict['Stage'] = publication_elements[7][publication_elements[7].find(
                                ':')+2:]
                            publ_dict['Access'] = 'N/A'
                            publ_dict['Source'] = publication_elements[8][publication_elements[8].find(
                                ':')+2:]
                        publications_data.append(publ_dict)
                    database_data.append(publications_data)
                    with open(PATH + "\Output\#" + str(author) + "_Publications" +
                              str(datetime.now())[: -7].replace(":", " ") + ".csv", "a", encoding="utf-8") as authors_output:
                        writer = csv.writer(authors_output)
                        writer.writerow(["Authors", "Authors_ids", "Title", "Journal",
                                         "Link", "DOI", "Type", "Stage", "Access", "Source"])
                        for publication in publications_data:
                            writer.writerow(list(publication.values()))
                            print(list(publication.values()))
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    flag = False
            analyze_button = driver.find_element_by_css_selector(
                "button.button--link.button--small.margin-size-24-r ")
            try:
                analyze_button.click()
            except:
                close_overlay()
                analyze_button.click()
            classifications = []
            if option1 == 1:
                classifications.append("analyzeType-chart-mini")
            if option2 == 1:
                classifications.append("analyzeYear-miniChart")
            if option3 == 1:
                classifications.append("analyzeCitations-chart-mini")
            for k in classifications:
                if option3 == 1:
                    time.sleep(DELAY)
                    graph = driver.find_element_by_id(
                        "analyzeCitations-miniGraph")
                    driver.execute_script(
                        "arguments[0].scrollIntoView();", graph)
                by_button = driver.find_element_by_id(k)
                try:
                    by_button.click()
                except:
                    close_overlay()
                    by_button.click()
                elements = driver.find_element_by_id(k.split('-')[0]+'-table')
                elements_list = (elements.text).split('\n')[2:]
                print(elements_list)
                if k == "analyzeType-chart-mini":
                    for elementpair in elements_list:
                        elements = elementpair.split()
                        print(elements)
                        if len(elements) > 2:
                            title = str(elements[0]+' '+elements[1]).lower()
                            if (title) in types_tit:
                                types_dict[title] = elements[2]
                                print('here')
                        else:
                            if (elements[0].lower()) in types_tit:
                                types_dict[elements[0].lower()] = elements[1]
                                print('here2')
                    for title in types_tit:
                        print(title)
                        if title in types_dict:
                            author_data.append(types_dict[title])
                            database_data.append(types_dict[title])
                        else:
                            author_data.append('0')
                            database_data.append('0')
                elif k == "analyzeYear-miniChart":
                    for elementpair in elements_list:
                        elements = elementpair.split()
                        if int(elements[0]) in years:
                            documents_dict[elements[0]] = elements[1]
                    for year in years:
                        if str(year) in documents_dict:
                            author_data.append(documents_dict[str(year)])
                            database_data.append(documents_dict[str(year)])
                        else:
                            author_data.append('0')
                            database_data.append('0')
                elif k == "analyzeCitations-chart-mini":
                    for elementpair in elements_list:
                        elements = elementpair.split()
                        if int(elements[0]) in years:
                            citations_dict[elements[0]] = elements[1]
                    for year in years:
                        if str(year) in citations_dict:
                            author_data.append(citations_dict[str(year)])
                            database_data.append(citations_dict[str(year)])
                        else:
                            author_data.append('0')
                            database_data.append('0')
                print("-"*25)

            print(author_data)

            if flag1 == 0:
                print("Adding Heads")
                with open(PATH + PATH2, "w+", encoding="utf-8") as authors_output:
                    writer = csv.writer(authors_output)
                    heads = ["Name", "Link", "Documents",
                             "Citations", "H-index"]
                    for i in range(1, 9):
                        heads.append("Coauthor" + str(i))
                        heads.append("CoauthorNo" + str(i))
                    for i in range(1, 6):
                        heads.append("Topic" + str(i))
                    if option1 == 1:
                        for i in types_tit:
                            heads.append(str(i))
                    if option2 == 1:
                        for i in years:
                            heads.append("Publications" + str(i))
                    if option3 == 1:
                        for i in years:
                            heads.append("Citations" + str(i))
                    writer.writerow(heads)
                    flag1 = 1
            if flag1 == 1:
                print("Appending...")
                with open(PATH + PATH2, "a", encoding="utf-8") as authors_output:
                    writer = csv.writer(authors_output)
                    writer.writerow(author_data)
                    all_data.append(database_data)
            g += 1
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            print('-'*25)
            pass

    driver.close()
    return all_data
