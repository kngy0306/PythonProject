import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# webdriverのオプション設定
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

print('ブラウザを立ち上げ中...')
driver = webdriver.Chrome(options=options)

# 1. Qiita の Chanmoro のプロフィールページにアクセスする
try:
    driver.get('https://qiita.com')
    print(driver.current_url)
    time.sleep(0.5)

    # 検索ボタンをクリックする
    driver.find_element(
        By.XPATH, '//input[@class="st-RenewalHeader_searchInput"]').send_keys('Python')

    # "Pythonを入力し検索"
    driver.find_element(
        By.XPATH, '//form[@class="st-RenewalHeader_searchModal"]').submit()
    time.sleep(0.5)

    # 1つ目の記事のタイトル、URL取得
    article_links = driver.find_elements(
        By.XPATH, '//h1[@class="searchResult_itemTitle"]/a')
    print(article_links[0].text)
    print(article_links[0].get_attribute('href'))
    article_links[0].click()

    driver.quit()

except Exception as e:
    print(e)
    driver.quit()
