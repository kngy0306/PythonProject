import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# webdriverのオプション設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')

print('connecting to remote browser...')
driver = webdriver.Chrome(options=options)

# 1. Qiita の Chanmoro のプロフィールページにアクセスする
try:
    driver.get('https://qiita.com/Chanmoro')
    print(driver.current_url)
    # > https://qiita.com/Chanmoro
    time.sleep(0.5)

    # 2. 「最近の記事」に表示されている記事一覧の 2 ページ目に移動する
    driver.find_element(By.XPATH, '//a[@rel="next"]').click()
    print(driver.current_url)
    # > https://qiita.com/Chanmoro?page=2

    time.sleep(0.5)
    # 3. 2 ページ目の一番最初に表示されている記事のタイトルを URL を取得する
    article_links = driver.find_elements(
        By.XPATH, '//h2[@class="css-1fhgjcy"]/a')
    print(article_links[0].text)
    # > Python - 関数を文字列から動的に呼び出す
    print(article_links[0].get_attribute('href'))
    # > https://qiita.com/Chanmoro/items/9b0105e4c18bb76ed4e9

    # x. ブラウザを終了する
    driver.quit()

except Exception as e:
    print(e)
    driver.quit()
