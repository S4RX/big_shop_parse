from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from full_silpo_shop_adress import full_silpo_shop_adress as fssa 
from selenium.webdriver.common.by import By
import change_info_in_silpo_db as db_control
import create_db

def choose_pickup(driver):
    driver.get('https://shop.silpo.ua/home')
    time.sleep(2) 
    delivery_btn = driver.find_element_by_class_name('button-switch-item.active')#кнопка доставки
    choose_ur_btn = driver.find_elements_by_class_name('button-switch-item')#2 кнопки: доставка и самовывоз
    pickup_btn = choose_ur_btn[1]
    pickup_btn.click()#выбрать самовывоз из магазина
    time.sleep(2)

def select_store_adress(driver):
    
    for adress in fssa:
        if adress == ('м. Київ', 'вул. Милославська, 10а'):
            is_stock = True
            choose_pickup(driver)
            set_city_and_adress(driver, adress)
            aply_button_el = driver.find_element_by_class_name('change-supermarket__btn')#кнопка подтверждения адреса нужного магазина
            aply_button_el.click()#нажать на aply_button_el
            time.sleep(2)
        
        else: 
            is_stock = False
            location_btn = driver.find_element_by_class_name("header-info-item.location")
            location_btn.click()
            time.sleep(1)
            set_city_and_adress(driver, adress)
            change_supermarket__btn = driver.find_element(By.XPATH, '//button[text()="Зберегти зміни"]')
            change_supermarket__btn.click()
            time.sleep(3)
        view_all_page_by_category(driver, adress, is_stock)

def set_city_and_adress(driver, adress):
    city_el = driver.find_element_by_class_name('store-select__city ')#меню выбора города на 1 странице
    city_el.click()#раскрыть city_list
    time.sleep(2)   # хардкодное ожидание
    city_el.click()
    city_el.send_keys(Keys.CONTROL, "a")
    city_el.send_keys(Keys.BACKSPACE)
    city_el.send_keys(adress[0], Keys.ENTER)#вставить в поле города нужный город магазина
    time.sleep(2)
    street_el = driver.find_element_by_class_name('store-select__store ')#поле адреса магазинов
    street_el.click()#раскрыть street_el
    time.sleep(2)
    street_el.send_keys(adress[1], Keys.ENTER)#ввести адрес нужного магазина в поле

def get_site_code(driver): #получить код сайта сейчас
    res = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res, 'lxml')
    return soup

def get_product_url(driver, soup): #получить ссылки на товар
    product_urls = soup.find_all("a", class_ = "product-title") #выбрать все места, где есть ссылки
    urls_list = []#место для хранения всех ссылок
    for product_url in product_urls: #перебрать список, полученный из супа
        clean_url = product_url.get('href') #очищаем первоначальный текст и достаём только ссылку
        full_url = 'https://shop.silpo.ua' + clean_url  #дополняем ссылку до целостного вида 
        urls_list.append(full_url) #добавляем в список 
    return urls_list

def get_title(driver, soup):
    title_list = []
    products_titles = soup.find_all('a',class_ = "product-title")#название товара 
    for title in products_titles:
        clean_title = title.text.strip()#только название товара, без разметки
        title_list.append(clean_title)
    return title_list    

def get_product_weight(driver, soup): # получаем вес товара
    product_weights = soup.find_all('div', class_ = 'product-weight')# выбрать все места, в которых есть вес
    weights_list = [] #создаем список для хранения веса всех товаров с страницы
    for product_weight in product_weights: #разбираем полученный список весов
        clean_weight = product_weight.text.strip() #очищаем каждый полученный вес от ненужной инфы  
        weights_list.append(clean_weight) #добавляем в список весов
    return weights_list

def get_price(driver, soup):
    hryvnias_list = []#список гривен из цен с 1 страницы
    kopecks_list = []#список копеек из цен с 1 страницы
    price = []#список нормализованных цен 
    for (hryvnias, kopecks) in soup:
    
        hryvnias = soup.find_all('div',class_ = "current-integer")#найти все гривневые значения из цены
        for hryvnia in hryvnias:
            hryvnias_list.append(hryvnia.text.strip())#добавить в список гривен чистое число  
    
        kopecks = soup.find_all('div',class_ = "current-fraction")#найти все копеечные значения из цены
        for kopeck in kopecks:
            kopecks_list.append(kopeck.text.strip())#добавить в список копеек чистое число
    
    for pair in zip(hryvnias_list,kopecks_list):#соеденить гривневое значение с копеечным значением 
        price.append(pair)#передать нормализованную цену в список 

    return price

def get_best_view(driver, is_stock):
    soup = get_site_code(driver)
    title = get_title(driver, soup)
    new_price = get_price(driver, soup)
    old_price = get_old_price(driver, soup)
    new_prices = []
    old_prices = []
    for item in new_price:
        beautiful_price = str(item[0]) + ',' + str(item[1]) + 'грн.'
        new_prices.append(beautiful_price)
    for item in old_price:
        beautiful_price = str(item[0]) + ',' + str(item[1]) + 'грн.'
        old_prices.append(beautiful_price)
    product_weight = get_product_weight(driver, soup)
    product_url = get_product_url(driver, soup)
    product_availability = get_availability(driver)
    image_urls = get_image(driver)
    full_data_els = []
    if is_stock == True:
        for pair in zip(title, new_prices, old_prices, product_weight, product_url, image_urls, product_availability):
            full_data_els.append(pair)
    else:
        for pair in zip(title, beautiful_prices, product_weight, product_url, image_urls, product_availability):
            full_data_els.append(pair)
    return full_data_els

def get_old_price(driver, soup):
    hryvnias_list = []#список гривен из цен с 1 страницы
    kopecks_list = []#список копеек из цен с 1 страницы
    price = []#список нормализованных цен 
    for (hryvnias, kopecks) in soup:
    
        hryvnias = soup.find_all('div',class_ = "old-integer")#найти все гривневые значения из цены
        for hryvnia in hryvnias:
            hryvnias_list.append(hryvnia.text.strip())#добавить в список гривен чистое число  
    
        kopecks = soup.find_all('div',class_ = "old-fraction")#найти все копеечные значения из цены
        for kopeck in kopecks:
            kopecks_list.append(kopeck.text.strip())#добавить в список копеек чистое число
    
    for pair in zip(hryvnias_list,kopecks_list):#соеденить гривневое значение с копеечным значением 
        price.append(pair)#передать нормализованную цену в список 

    return price

def get_pagination_number(driver):
    soup = get_site_code(driver)#получаем код открывшейся страницы
    pagination_numbers_list = []#создаем список для будущих чисел из кнопок пагинации
    pagination_numbers = soup.find_all('div', class_ = "pagination-link")#ищем все кнопки пагинации
    for pagination_number in pagination_numbers:#разбираем полученный список пагинационных чисел
        time.sleep(1)
        clean_number = pagination_number.text.strip()#очищаем числа от мусора 
        pagination_numbers_list.append(clean_number)#добавляем числа пагинации в список для удобства
    if pagination_numbers_list != []:
        page_by_category = max(pagination_numbers_list)
        return page_by_category     
    else: 
        skip = ''
        return skip

def get_image(driver):
    soup = get_site_code(driver)
    image_urls = soup.find_all('a', class_ = "product-list-item__image")
    image_urls_list = []
    for image_url in image_urls:
        clean_url = image_url['style'].strip('background-image: url("')
        if 'https://content.silpo' in clean_url:
            image_urls_list.append(clean_url.strip('");'))
    return image_urls_list

def get_category_urls(driver): #получить ссылки на категории товаров
    burger_with_category = driver.find_element_by_class_name("icon-chevron-down")#присваиваем элемент, который при нажатии открывает список
    burger_with_category.click()# производим "нажатие" для открытия списка с категориями
    soup = get_site_code(driver)#получаем код страницы на данный момент 
    urls = soup.find_all('a')#ищем все возможные ссылки
    categoryes_urls = []# создаем список для будущих ссылок на категории
    category_names = []
    #category_names_and_urls = []
    for url in urls: # разбираем полученный список ссылок
        if 'category' in url['href']: # проверяем относится ли ссылка к ссылкам на категории 
            category_name = url.text.strip()
            categoryes_urls.append('https://shop.silpo.ua' + url['href'])# отправляем в список полные ссылки на категории
            category_names.append(category_name)

    return categoryes_urls, category_names #categoryes_urls, category_names

def view_all_page_by_category(driver, adress, is_stock):
    if '/' in adress[1]:
        fir_adr = adress[0]
        sec_adr = adress[1].replace('/', '-')
        adress = fir_adr + sec_adr
    path_to_db = r"db\\" + str(adress) + ".db"
    #create_db.create_new_db(path_to_db)
    categoryes_names_and_urls = get_category_urls(driver)#[0]
    if is_stock == True:
        stock_page = "https://shop.silpo.ua/all-offers?filter_PROMO=(18324__19969__27656)"
        db_control.create_table_for_category("Stock db", path_to_db, is_stock)
        driver.get(stock_page)#открываем ссылку категории
        time.sleep(1)
        max_page_by_category = get_pagination_number(driver)
        for page in range(2, int(max_page_by_category) + 1):
            driver.get(stock_page  + '?to=' + str(page) + '&from=' + str(page))
            time.sleep(1)
            data = get_best_view(driver, is_stock)
            for data_el in data:
                db_control.set_new_row_data("Stock db", data_el, path_to_db, is_stock)
        brute_force_all_page(driver, category_names_and_urls, is_stock)
    else:
        brute_force_all_page(driver, category_names_and_urls, is_stock)



def brute_force_all_page(driver, category_names_and_urls, is_stock):
    for full_adress in zip(categoryes_names_and_urls[0], categoryes_names_and_urls[1]):#выполняем проход по категориям
        db_control.create_table_for_category(full_adress[1], path_to_db, is_stock)
        driver.get(full_adress[0])#открываем ссылку категории
        time.sleep(1)
        max_page_by_category = get_pagination_number(driver)
        if max_page_by_category != "":
            for page in range(1, int(max_page_by_category) + 1):
                driver.get(str(full_adress[0]) + '?to=' + str(page) + '&from=' + str(page))
                time.sleep(1)
                data = get_best_view(driver)
                
                for data_el in data:
                    db_control.set_new_row_data(full_adress[1], data_el, path_to_db, is_stock)

        elif max_page_by_category == "":
            data = get_best_view(driver)
            for data_el in data:
                db_control.set_new_row_data(full_adress[1], data_el, path_to_db)

def get_availability(driver):
    soup = get_site_code(driver)
    products_avaliable_list = []
    products_wrappers = soup.find_all('li', class_ = 'product-list-item-wrapper')
    for product_wrapper in products_wrappers:
        avaliability = False
        try:
            if product_wrapper['class'][1] == 'not-available':
                products_avaliable_list.append(avaliability)
        except IndexError:
            avaliability = True
            products_avaliable_list.append(avaliability)        
    return products_avaliable_list


def main():
    driver = webdriver.Chrome()
    select_store_adress(driver)
 
if __name__ == '__main__':
    main()