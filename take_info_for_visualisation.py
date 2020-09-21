#burger_with_urls = driver.find_element_by_class_name("icon-chevron-down")
#    burger_with_urls.click()
#    soup = get_site_code(driver)
#    urls = soup.find_all('a')
#    categoryes_names_and_urls = []
#    for url in urls:
#        if 'category' in url['href']:
#            category_name = url.text.strip()
#            categoryes_names_and_urls.append((category_name, 'https://shop.silpo.ua' + url['href']))
#    
#    print(categoryes_names_and_urls)
#    return categoryes_names_and_urls
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
