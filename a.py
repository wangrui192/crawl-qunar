# coding=utf-8
from selenium import webdriver
import time;
browser = webdriver.Chrome()

browser.get('https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E6%88%90%E9%83%BD&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2017-10-08&searchArrivalTime=2017-09-25&nextNDays=0&startSearch=true&fromCode=CTU&toCode=SHA&from=qunarindex&lowestPrice=null')
time.sleep(1)
#按价格排序
browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/span').click()
time.sleep(1.5)
#选中第一个价格
browser.find_element_by_class_name('mb-10').find_element_by_class_name('m-airfly-lst').find_element_by_css_selector('.b-airfly').click()
time.sleep(2)
#获取最低价供应商
price_list = browser.find_elements_by_class_name('e-ota-outer')
mix_price = price_list[0].find_element_by_css_selector('.m-center.g-clear').find_element_by_css_selector('.col-prc.g-clear').find_element_by_css_selector('.prc').find_element_by_tag_name('span').get_attribute("innerText")
mix_price = int(mix_price)
target_price = price_list[0]
for price in price_list:
    price_detail = price.find_element_by_css_selector('.m-center.g-clear')
    price_detail = price_detail.find_element_by_css_selector('.col-prc.g-clear')
    price_detail = price_detail.find_element_by_css_selector('.prc').find_element_by_tag_name('span')
    now_price = price_detail.get_attribute("innerText")
    now_price = int(now_price)
    if mix_price > now_price:
        target_price = price
        mix_price = now_price
if mix_price > 1000:
    target_price = 0

fo = open("/mnt/hgfs/price", "ab+")
fo.write('python price is '+ str(mix_price)+'\n')
fo.close()

target_price.click()
handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
# 切换窗口（下单页同时填数据）
time.sleep(1.5)
for handle in handles:# 切换窗口
    if handle!=browser.current_window_handle:
        print 'switch to ',handle
        browser.switch_to_window(handle)
        str = "王瑞".decode('utf-8')
        browser.find_element_by_class_name('js-passenger-name').send_keys(str)
        browser.find_element_by_class_name('js-cert-number').send_keys('身份证')
        browser.find_element_by_class_name('js-passenger-phone').send_keys('18328416607')
        browser.find_element_by_class_name('contact-name').send_keys(str)
        browser.find_element_by_class_name('js-contact-phone').send_keys('18328416607')
        #取消延误险
        browser.find_element_by_xpath('//*[@id="m-insure"]/div[2]/div/div/div[2]/div[2]/div[1]').click()
        browser.find_element_by_xpath('//*[@id="m-insure"]/div[2]/div/div/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        tip_list = browser.find_elements_by_css_selector('.gray-button.js-tips-close')
        tip_list[0].click()
        #取消航易险
        browser.find_element_by_xpath('//*[@id="m-insure"]/div[2]/div/div/div[1]/div[2]/div[1]').click()
        browser.find_element_by_xpath('//*[@id="m-insure"]/div[2]/div/div/div[1]/div[2]/div[2]').click()
        time.sleep(1)
        tip_list = browser.find_elements_by_css_selector('.gray-button.js-tips-close')
        tip_list[0].click()
        #下单！
        browser.find_element_by_xpath('//*[@id="js-submit"]').click()
