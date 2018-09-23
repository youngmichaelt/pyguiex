from tkinter import Menu
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
##import ttk
import tkinter as tk
from selenium import webdriver
import selenium.webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
from bs4 import BeautifulSoup as BSoup
import _thread
import threading

def start_bot_thread():
        print('starting bot')
        threading.Thread(target=bot).start()
        



def bot():
        
##        options = Options()
##        options.add_argument("--headless")
        option = webdriver.ChromeOptions()
##        option.add_argument('--incognito')


        
##        caps = DesiredCapabilities().FIREFOX
##        caps['pageLoadStrategy'] = 'eager'
##        firefox_profile = webdriver.FirefoxProfile()
##        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        
        driver = webdriver.Firefox(executable_path=r'C:\Users\mikey\Desktop\geckodriver-v0.20.1-win64\geckodriver.exe')
##        driver = webdriver.Chrome(chrome_options=option, executable_path=r'C:\Users\mikey\Desktop\chromedriver_win32\chromedriver.exe')

        bs_obj = BSoup(driver.page_source, 'html.parser')
        BaseSize = 580
        #Base Size is for Shoe Size 6.5
##        size = 8

        def write(string):
                text_box.insert('end', string + '\n')
                text_box.see('end')
        
        size = sizebox.get()
        print(size)
##        model = 'CQ0022' CQ3168
        model = skubox.get()
        ##model = 'AQ1230'
        ShoeSize = float(size) - 6.5
        ShoeSize = ShoeSize * 20
        RawSize = ShoeSize + BaseSize
        ShoeSizeCode = int(RawSize)
        
        URL = 'http://www.adidas.com/us/' + model + '.html?forceSelSize=' +(model) + '_' + str(ShoeSizeCode)

##        write('Attempting to load ' + URL)
        time.sleep(5)    
        driver.get(URL)

        write('Success')
        

        time.sleep(6)

        wait = WebDriverWait(driver, 999)
                 
##        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-auto-id='add-to-bag']"))).click()
        driver.find_element_by_css_selector('.add_to_bag_container___1BPg9 > button:nth-child(1)').click()
        def random_delay(min_delay=0.25, max_delay=1.4):
            time.sleep(random.uniform(min_delay, max_delay))
            
        random_delay()
        time.sleep(3)
        driver.get("https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show")
        wait.until(EC.visibility_of_element_located((By.ID, 'dwfrm_cart_checkoutCart'))).click()
        time.sleep(2)

        def send_keys_delay_random(first_name, keys, min_delay=0.05, max_delay=0.25):
            for key in keys:
                first_name.send_keys(key)
                time.sleep(random.uniform(min_delay, max_delay))

        
                
        first_name_input = first_name_box.get()
        last_name_input = last_name_box.get()
        state_input = state_box.get()
        shipping_address_input = shipping_address_box.get()
        city_input = city_box.get()
        postal_input = postal_box.get()
        phone_input = phone_box.get()
        email_input = email_box.get()
        credit_card_input = credit_card_box.get()
        month_input = month_box.get()
        year_input = year_box.get()
##        security_code_input = security_code_box.get()
        
        time.sleep(4)        
        first_name = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_firstName')
        
        last_name = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_lastName')

        shipping_address = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_address1')

        city = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_city')

        postal_code = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_postalCode')

        phone = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_phone')

        email_address = driver.find_element_by_xpath("//*[@id='dwfrm_shipping_email_emailAddress']")

        

##        security_code = driver.find_element_by_id('dwfrm_payment_creditCard_cvn')
        
      
        send_keys_delay_random(first_name, first_name_input)
     

        random_delay()

        send_keys_delay_random(last_name, last_name_input)


        random_delay()

        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[2]/div/div[6]/div[1]/div[1]").click()

        random_delay()

##        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[2]/div/div[6]/div[1]/div[2]/div[37]").click()
        
        if state_input == 'NY':
            state_input = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[2]/div/div[6]/div[1]/div[2]/div[37]'
           
        driver.find_element_by_xpath(state_input).click()
        
        send_keys_delay_random(shipping_address, shipping_address_input)

        random_delay()

        send_keys_delay_random(city, city_input)

        random_delay()

        send_keys_delay_random(postal_code, postal_input)

        random_delay()

        send_keys_delay_random(phone, phone_input)

        random_delay()

        send_keys_delay_random(email_address, email_input)

        random_delay()

        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[2]/ng-form/div[6]/div/button").click()

        random_delay()

        credit_card = wait.until(EC.visibility_of_element_located((By.ID, 'dwfrm_payment_creditCard_number')))

        send_keys_delay_random(credit_card, credit_card_input)

        driver.find_element_by_id('dwfrm_payment_creditCard_month_display_field').click()

        random_delay()

        if month_input == 'January':
            month_input = '.expanded > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)'

        driver.find_element_by_css_selector(month_input).click()
##            driver.find_element_by_css_selector('.expanded > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)').click()
        random_delay()
        driver.find_element_by_id('dwfrm_payment_creditCard_year_display_field').click()
        random_delay()

        if year_input == '2018':
            year_input = '.year > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)'

        driver.find_element_by_css_selector(year_input).click()
        
##        driver.find_element_by_css_selector('.year > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)').click()
##        security_code = driver.find_element_by_id('dwfrm_payment_creditCard_cvn')
        random_delay()
##        send_keys_delay_random(security_code, '719')
       
def GUI(): 
    window = Tk()

    window.style = Style()
    window.style.theme_use('clam')

    ##style = ttk.Style()
    ##current_theme = style.theme_use()
    ##style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [20, 5]}}})


    ##frame = tk.Frame(window)
    ##
    ##frame.grid(row=0, column=0, sticky='nsew')

    ##window.config(bg = '#828481')
            
    window.geometry('750x750')


    n = ttk.Notebook(window)

    f1 = ttk.Frame(n, width = 750, height = 750)
    f2 = ttk.Frame(n, width = 750, height = 750)
    f3 = ttk.Frame(n, width = 750, height = 750)
    n.add(f1, text='Start')
    n.add(f2, text='Shipping')
    n.add(f3, text='Billing')
    n.grid()
    ##f1.grid(row=5, column=5)
    ##n.grid_propagate(False)
    f1.grid_propagate(False)
    f2.grid_propagate(False)
    f3.grid_propagate(False)

    global sizebox
    global skubox
    global first_name_box
    global last_name_box
    global shipping_address_box
    global city_box
    global state_box
    global postal_box
    global phone_box
    global email_box
    global credit_card_box
    global month_box
    global year_box


    

    size_lbl = Label(f1, text='Size: ')
    size_lbl.grid(column=0, row=0, padx = 20)
    sizebox = Entry(f1, width=15)
    sizebox.grid(column=1, row=0, pady=5)


    sku_lbl= Label(f1, text='SKU: ')
    sku_lbl.grid(column=0, row=2)
    skubox = Entry(f1, width=15)
    skubox.grid(column=1, row=2, padx=10, pady=10)


    def saved():
        size = sizebox.get()
        model = skubox.get()
        
        
    enterbtn = Button(f1, text='save changes', command = saved)
    enterbtn.grid(column=1, row=3, padx=10, pady=10)


    btn = Button(f1, text='start', command=start_bot_thread)
##    btn = Button(f1, text='start', command=_thread.start_new_thread(bot()))
    btn.grid(column = 3, row= 3)


    #tab2

    first_name_lbl = Label(f2, text='First Name: ')
    first_name_lbl.grid(column=0, row=0, sticky=W, padx = 10)
    first_name_box = Entry(f2, width=15)
    first_name_box.grid(column=1, row=0, pady=10, sticky=W)


    last_name_lbl = Label(f2, text= 'Last name: ')
    last_name_lbl.grid(column=2, row=0, sticky=W, padx=10)
    last_name_box = Entry(f2, width=15)
    last_name_box.grid(column=3, row=0, sticky=W)


    shipping_address_lbl = Label(f2, text='Shipping Address: ')
    shipping_address_lbl.grid(column=0, row=1, sticky=W, padx = 10)
    shipping_address_box = Entry(f2, width=25)
    shipping_address_box.grid(column=1, row=1, pady=10, sticky=W)


    city_lbl = Label(f2, text= 'City: ')
    city_lbl.grid(column=2, row=1, sticky=W, padx=10)
    city_box = Entry(f2, width=15)
    city_box.grid(column=3, row=1, sticky=W, )


    state_lbl = Label(f2, text='State: ')
    state_lbl.grid(column=0, row=2, padx=10, sticky=W)
    states = ['Choose State', 'NY', 'NJ', 'PN']
    state_box = StringVar(window)
    state_box.set(states[0])
    s = OptionMenu(f2, state_box, *states)
    s.grid(column=1, row=2, pady=10, sticky=W)

    postal_lbl = Label(f2, text="Postal Code: ")
    postal_lbl.grid(column=2, row=2, sticky=W, padx=10)
    postal_box = Entry(f2, width=15)
    postal_box.grid(column=3, row=2, sticky=W, pady=10)


    phone_lbl= Label(f2, text='Phone: ')
    phone_lbl.grid(column=0, row=3, sticky=W, padx=10)
    phone_box = Entry(f2, width=15)
    phone_box.grid(column=1, row=3, sticky=W, pady=10)

    email_lbl = Label(f2, text='Email: ')
    email_lbl.grid(column=2, row=3, sticky=W, padx=10)
    email_box = Entry(f2, width=15)
    email_box.grid(column=3, row=3, sticky=W, pady=10)



    f2enterbtn = Button(f2, text='save changes', command = saved)
    f2enterbtn.grid(column =1, row=6, pady=10, sticky=W)

    #tab3

    credit_card_lbl = Label(f3, text='Credit Card: ')
    credit_card_lbl.grid(column=0, row=0, sticky=W, padx=10)
    credit_card_box = Entry(f3, width=20)
    credit_card_box.grid(column=1, row=0, sticky=W, pady=10)

    month_lbl = Label(f3, text='Month: ')
    month_lbl.grid(column=2, row=0, sticky=W, padx=10)
    months = ['Choose Month','January', 'Febuary', 'March', 'April']
    month_box = StringVar(window)
    month_box.set(months[0])
    m = OptionMenu(f3, month_box, *months)
    m.grid(column=3, row=0, sticky=W, pady=10)

    year_lbl = Label(f3, text='Year: ')
    year_lbl.grid(column=0, row=1, sticky=W, padx=10)
    years = ['Choose Year', '2018', '2019', '2020']
    year_box = StringVar(window)
    year_box.set(years[0])
    y = OptionMenu(f3, year_box, *years)
    y.grid(column=1, row=1, sticky=W, pady=10)

    global text_box




    text_box = Text(f1)
    
    text_box.grid(row=5, column=5, columnspan=1)

    ##def write(string):
    ##    text_box.insert('end', string + '\n')
    ##    text_box.see('end')



    window.mainloop()
    
        

##GUI()

threading.Thread(target=GUI).start()




































  ##driver = webdriver.Chrome(executable_path=r'C:\Users\mikey\Desktop\chromedriver_win32\chromedriver.exe')
##        def URLGen():
##            global URL
##            BaseSize = 580
##        #Base Size is for Shoe Size 6.5
##            size = 8
##            model = 'CQ0022'
##        ##model = 'AQ1230'
##            ShoeSize = size - 6.5
##            ShoeSize = ShoeSize * 20
##            RawSize = ShoeSize + BaseSize
##            ShoeSizeCode = int(RawSize)
##            URL = 'http://www.adidas.com/us/' + model + '.html?forceSelSize=' +(model) + '_' + str(ShoeSizeCode)
##            
##        URLGen()
