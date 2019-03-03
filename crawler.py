from selenium import webdriver
import time
import csv

article = []

# [create csv file, open]
f = open('test.csv', 'w', encoding='utf-8_sig',  newline='')
csv_writer = csv.writer(f)

# [Chrome driver set] You have to modify path.
path="C:\\Users\\dongho\\Desktop\\driver\\chromedriver"
driver = webdriver.Chrome(path)

'''
# [login_info]
username = input("Input ID : ")
password = input("Input PWD : : ")
'''

search = input("Input HASHTAG : ")

# [brower_on]
driver.get("https://www.instagram.com/explore/tags/" + search)

'''
# [login]
id = driver.find_element_by_name('username')
id.send_keys(username)
pw = driver.find_element_by_name('password')
pw.send_keys(password)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button').click()

driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
'''

'''
# [serch]
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
driver.implicitly_wait(5)
'''
driver.implicitly_wait(3)
article_count = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/header/div[2]/div[2]/span/span").text
article_count = article_count.replace(',', '')
article_count = int(article_count)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()

print(article_count, " article crawling ...\n")

# [contents save]
for i in range (0, article_count-1) :

    hash_list = []
    date_text = []

    time.sleep(1.0)

    try :
        writer = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a")
        contests = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div/span")
        hash = driver.find_elements_by_css_selector("a[href^='/explore/tags']")
        date = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/article/div[2]/div[2]/a/time")

        writer_text = writer.text
        text_text = contests.text

        for item in hash:
            hash_list.append(item.text)

        date_text = date.get_attribute('datetime')

        csv_writer.writerow([writer_text, text_text, hash_list,date_text])

        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()

    except :
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()

print("complete!!")

f.close()
driver.close()
