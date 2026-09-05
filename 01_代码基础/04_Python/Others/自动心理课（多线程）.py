from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

def process_url(t_url, start, ulist):
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    web = Chrome(options=options)
    web.get(url_main)
    # Load cookies
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        web.add_cookie(cookie)
    wait = WebDriverWait(web, 10)  # Wait up to 10 seconds
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "登录")]')))
    element.click()
    print(t_url)
    print(start, "of", len(ulist))
    web.execute_script("window.open('', '_blank');")
    web.switch_to.window(web.window_handles[-1])
    web.get(t_url)
    while 1:
        try:
            web.find_element(By.XPATH, '//*[@class="prism-big-play-btn"]').click()
        except:
            time.sleep(1)
        else:
            break
    while 1:
        if web.find_element(By.XPATH,'//*[@class="tips-completion"]').text=="已完成":
            break
    web.close()
    web.switch_to.window(web.window_handles[0])

if __name__ == '__main__':
    url_login = 'https://lms.sysu.edu.cn/enrol/index.php?id=3379'
    url_main =  'https://lms.sysu.edu.cn/course/view.php?id=3379'
    link_element = '//li[contains(@class, "activity fsresource modtype_fsresource")]//a[contains(@class, ' \
                   '"aalink stretched-link")]'
    options = ChromeOptions()
    web = Chrome(options=options)
    web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
                """
    })
    web.get(url_login)
    input("please login")
    # Save cookies
    pickle.dump(web.get_cookies(), open("cookies.pkl", "wb"))

    elements = web.find_elements(by=By.XPATH, value=link_element)
    ulist = [element.get_attribute('href') for element in elements]
    print(ulist)

    web.quit()  # Close the browser

    start = int(input("start from: ")) - 1
    max_process = int(input("how many process do you want to start: "))

    # Use a ThreadPoolExecutor to process the URLs in parallel
    with ThreadPoolExecutor(max_workers=max_process) as executor:
        for i in range(start, len(ulist)):
            executor.submit(process_url, ulist[i], i, ulist)