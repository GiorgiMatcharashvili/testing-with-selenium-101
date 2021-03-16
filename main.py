from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''

Warning: If you don't know Html, Just leave.

1) What is selenium?

2) What is Webdriver_manager

3) Why we need Webdriver_manager

4) Example of bad webdriver import
'''

# https://chromedriver.chromium.org/downloads

# PATH = "C:\Program Files (x86)\chromedriver.exe
# driver = webdriver.Chrome(PATH)


'''
Explain good Webdriver import
'''

# import selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager                # Chrome
# from webdriver_manager.firefox import GeckoDriverManager                # Firefox
# from webdriver_manager.opera import OperaDriverManager                  # Opera

"""
What is cross browser testing ?

Where should we start?

rule 0: Everything starts with driver
"""


# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# driver = webdriver.Opera(executable_path=OperaDriverManager().install())

"""
What is .get(url)?

driver.get("https://www.youtube.com/") or driver.get(url)
"""

# url = "https://www.youtube.com/"
#
# driver.get(url)

"""
rule 1: Be friend with F12(Developers' tool)

rule 2: Ask important questions:
    1) What is element?
    2) Where is element?
    3) How to find?
    4) What should we do with an element?
    
What is Xpath and css_Selector?

Warn about Problems with xpath

/html/body/div/div/section/section/div/div/div/div/div[2]/div[2]/div[2]/ul/li[1]/a/span
a[@href="/ka/chven-shesakheb"]


How to find element?

"""


# element = driver.find_element_by_css_selector('[id="hover-overlays"]')
# element = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/ytd-thumbnail/a/div[3]")
# element = driver.find_element_by_id("hover-overlays")


"""
Did you see the problem?

solve this with Json

rule 3: Be friend with Json

rule 4: make good names
"""

# selectors = {
#     "Trending_button" : "/html/body/ytd-app/div/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a",
#     "Trending" : "/html/body/ytd-app/div/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a",
#     "Youtube_Website_trending_page_Button_for_click" : "/html/body/ytd-app/div/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a",
#     "Search_input" : "search",
#     "Search_Button" : "search-icon-legacy",
#     "First_searched_text" : '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'
# }

#Trending_button = driver.find_element_by_xpath(selectors["Trending_button"])


"""
Note: find was the hardest part.

What should we do after find the element?

Well you can click, get a text, wait for a element and add your text.

Classic example of input your text:

"""


# driver.find_element_by_id(selectors["Search_input"]).send_keys("hello darkness")


"""
Classic example of Click:
"""


# driver.find_element_by_id(selectors["Search_Button"]).click()


"""
Classic example of wait:
It needs delay, selector's type and selector.
"""


# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selectors["First_searched_text"])))



"""
Classic example of getting a text:
always give it to the variable
"""


# FirstSearchedText = driver.find_element_by_xpath(selectors["First_searched_text"]).text
# print("First recommended Video's Title: ",FirstSearchedText)

"""

Warning: Always clean your mess and close driver

"""

#driver.close()

"""
Rule 5: Be friend with Errors

The Last Rule: If you need help just search it.

https://selenium-python.readthedocs.io/

Tutorials:
https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

Tutorials in hindi:
https://www.youtube.com/watch?v=mOAXEQevCAE&list=PLhW3qG5bs-L_s9HdC5zNshE5Ti8jABwlU
"""