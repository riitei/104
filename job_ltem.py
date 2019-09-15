from selenium import webdriver
from access_job_file import Access_job_file
from selenium.webdriver.support.ui import Select
import requests
import threading
import time
from log_mess import log


class Job_item(threading.Thread):
    # id = ""
    # pw = ""

    def __init__(self, url):
        super().__init__()
        self.log_mess = log()

        self.__url = url

    def chrome(self, url):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--no-sandbox")
        # options.add_argument('--headless')
        # options.add_argument('disable-infobars')
        # options.add_argument('--proxy-server={0}'.format(ip))
        # driver = webdriver.Chrome(chrome_options=options)
        html_status = requests.get(url).status_code
        if html_status == 200:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(url)
            self.log_mess.main("連線成功")
            driver.get_cookies()
            # print(driver.get_cookies())
            # print(driver.session_id)
            return driver
        else:
            self.log_mess.main("連線失敗")
            exit()
            return None

    def login(self, driver):
        try:
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a').click()
            driver.find_element_by_id("username").send_keys(self.id)
            time.sleep(5)
            driver.find_element_by_id("password").send_keys(self.pw)
            time.sleep(5)
            driver.find_element_by_id("submitBtn").click()
            time.sleep(10)
            print("登入成功")
            return driver
        except:
            self.log_mess.main("登入失敗")
            # driver.quit()
            pass
            # exit()
            return "登入失敗"

    def run(self):
        job_item_driver = self.chrome(self.__url)
        # 更新時間
        # job_time = job_item_driver.find_element_by_class_name("update").text[5:]
        # 職務
        # job_position = job_item_driver.find_element_by_class_name("center").find_element_by_tag_name("h1").text
        # 公司
        # job_name = job_item_driver.find_element_by_class_name("cn").text
        # 地址
        # job_addr = job_item_driver.find_element_by_class_name("addr").text
        # 求職網址
        # job_url = self.__url
        # 記錄公司資料
        # file_name = time.strftime("%Y%m%d", time.localtime())
        # 開檔案
        # data_dict = Access_job_file().job_log_read_dict(file_name)
        # 寫檔案
        # now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # data_dict[now_time] = [
        #     {"job_position": job_position},
        #     {"job_name": job_name},
        #     {"job_addr": job_addr},
        #     {"job_url": job_url},
        #     {"job_time": job_time}
        # ]
        # 記錄工作職務內容
        # Access_job_file().job_log_write_dict(file_name, data_dict)
        #
        # if job_name == 'QNAP_威聯通科技股份有限公司':
        #     job_item_driver.quit()
        #     exit()
        #     登入帳號密碼
        time.sleep(2)
        job_item_driver = self.login(job_item_driver)
        #
        #
        try:
            time.sleep(1)
            # 投遞履歷
            job_item_driver.find_element_by_id("applyJobBtn").click()
            time.sleep(2)
            # 第幾份履歷
            # //resumeList0
            # //resumeList1
            job_item_driver.find_element_by_id("resumeList2").click()  # CODE
            # 推薦信
            # 系統預設
            # content = ""
            # job_item_driver.find_element_by_id("job_com_content").send_keys(content)
            # 推薦信 一
            Select(
                job_item_driver.find_element_by_class_name("recommendation-select")
            ).select_by_index(1)
            time.sleep(2)
            # 104職業適性測驗
            # 以後再寫
            #
            # 送交
            job_item_driver.find_element_by_id("btSend").click()
            time.sleep(2)
            #
            Access_job_file().job_list_result(self.__url)
            time.sleep(2)
            print("投遞成功")

        except:
            pass
            print("今日已投遞")

        finally:
            job_item_driver.quit()
