from selenium import webdriver

def test():
    try:
        dr = webdriver.Chrome('/usr/bin/chromedriver')
        dr.get('arguscarhire.com')
        c = dr.find_element_by_class_name("mostpopular")
        print 'ccccc'
        print c
        #c.click()
        #print dr.title
        dr.quit()
    except Exception as e:
        print(e)
        dr.quit()