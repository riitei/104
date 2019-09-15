from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
from log_mess import log
# from job_category​_menu import JobCategoryMenu
from job_category_menu import JobCategoryMenu
from access_job_file import Access_job_file
from job_ltem import Job_item


# 104 Login in
class Job:
    url = "https://www.104.com.tw/jobs/main/"


    def __init__(self):
        self.log_mess = log()

    def chrome(self, url):
        # ip = proxy_ip().get_proxy_ip()
        # options = webdriver.ChromeOptions()
        # options.add_argument("--no-sandbox")
        # options.add_argument('--headless')
        # options.add_argument('disable-infobars')
        # options.add_argument('--proxy-server={0}'.format(ip))
        # driver = webdriver.Chrome(chrome_options=options)
        # html_status = requests.get(url).status_code
        # s = requests.session()
        # s.keep_alive = False
        # requests.DEFAULT_RETRIES = 999999999

        # if html_status == 200:
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.get(url)
        self.log_mess.main("連線成功")
        return driver
        # else:
        #     self.log_mess.main("連線失敗")
        #     exit()
        #     return None


    # selenium
    def search_job_name_and_city(self, driver):
        # try:

        driver.find_element_by_id("icity").click()
        time.sleep(2)
        # 台北
        driver.find_element_by_id("e104menu2011_m_cb_0_0").click()
        # 大陸
        driver.find_element_by_id("e104menu2011_m_cb_1").click()
        # 大陸
        # driver.find_element_by_xpath('//*[@id="e104menu2011_m_i_1"]/a').click()
        # 地區確認
        js = 'javascript:obj_e104menu2011.sendBack();'
        driver.execute_script(js)
        time.sleep(2)

        time.sleep(2)
        # except:
        #     self.log_mess.main("搜尋失敗")
        #     driver.quit()
        #     exit()

        return driver

    def job_list(self, driver):
        #
        jobs = driver.find_elements_by_css_selector(".b-block--top-bord.job-list-item.b-clearfix.js-job-item")
        for num, job in enumerate(jobs):
            job_now_time = job.find_element_by_class_name("b-tit__date").text
            if job_now_time != "":
                # 公司名稱
                job_name = job.get_attribute('data-cust-name')
                # 公司職務
                job_position = job.get_attribute('data-job-name')
                # 職務簡介
                try:
                    job_introduction = job.find_element_by_css_selector(".job-list-item__info.b-clearfix.b-content").text
                except:
                    job_introduction  = ""
                # 公司求職內容網址
                url = job.find_element_by_class_name("js-job-link").get_attribute("href")
                li_obj = job.find_element_by_css_selector(
                    ".b-list-inline.b-clearfix.job-list-intro.b-content").find_elements_by_tag_name("li")
                try:
                    # 工作城市
                    job_city = li_obj[0].text
                except:
                    job_city = ''
                try:
                    # 經歷
                    job_experience = li_obj[1].text
                except:
                    job_experience = ''
                try:

                    # 學歷
                    job_education = li_obj[2].text
                except:
                    job_education = ''
                try:
                    # 此資料可有可無，沒元素就是沒資料
                    span_obj = job.find_element_by_css_selector(".job-list-tag.b-content")
                    # 薪水
                    job_salary = span_obj.find_elements_by_tag_name("span")[0].text
                except:
                    job_salary = ''
                now = time.strftime("%m/%d", time.localtime())
                #
                # print("%d => %s" % (num, url))
                # print("公司名稱 => %s" % job_name)
                # print("求職職務 => %s" % job_position)
                # print("求職簡介=> %s" % job_introduction)
                #
                # print("工作城市 => %s" % job_city)
                # print("經歷 => %s" % job_experience)
                # print("學歷=> %s" % job_education)
                #
                # print("薪資=> %s" % job_salary)

                job_time = str(job_now_time).split("/")
                if int(job_time[0]) < 10:
                    job_time[0] = "0%s" % job_time[0]
                job_now_time = "%s/%s" % (job_time[0], job_time[1])
                print(job_now_time)
                # ======== 測試資料
                # if now == job_now_time:
                #     print("===> 今日職缺")
                #     # 查詢是否投遞過公司職務url
                #     search_reslut = Access_job_file().search_job_list(url)
                #     if (search_reslut == False):
                #         print("job_url.list_沒記錄__")
                #         Job_item(url).start()
                #         # time.sleep(40)
                #     else:
                #         # 測試用
                #         print("job_url.list_有記錄__")
                #     time.sleep(40)
                #
                # else:
                #     print(" 非 今日職缺")
                # ======== 測試資料

                # 紀錄公司基本資料，日後查詢公司是否經常聘用人
                # 記錄公司資料

                file_name = time.strftime("%Y%m%d", time.localtime())
                # 開檔案
                data_dict = Access_job_file().job_log_read_dict(file_name)
                # 寫檔案
                now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
                data_dict[now_time] = [
                    {"job_position": job_position},
                    {"job_name": job_name},
                    {"job_introduction": job_introduction},
                    {"job_addr": job_city},
                    {"job_experience": job_experience},
                    {"job_education": job_education},
                    {"job_salary": job_salary},
                    {"job_url": url},
                    {"job_time": job_time}
                ]
                print(data_dict)
                # 記錄工作職務內容
                Access_job_file().job_log_write_dict(file_name, data_dict)
                #
                search_reslut = Access_job_file().search_job_list(url)

                if (search_reslut == False):
                    print("job_url.list_沒記錄__")
                    # 開 Thread
                    Job_item(url).start()
                    time.sleep(5)
                else:
                    # 測試用
                    print("job_url.list_有記錄__")

            time.sleep(5)
            print("---------------------------------")

            # driver.quit()
            # exit()

    def search_condition(self, driver):
        css_name = '.b-tabs__txt.js-tab-title'
        # 更新日期
        # driver.find_elements_by_css_selector(css_name)[0].click()
        # 經歷要求
        driver.find_elements_by_css_selector(css_name)[3].click()
        # 經歷一年
        xpath = '//*[@id="js-sub-filter"]/div/div[4]/label[1]/span'
        driver.find_element_by_xpath(xpath).click()
        time.sleep(1)
        # 經歷1-3年
        xpath = '//*[@id="js-sub-filter"]/div/div[4]/label[2]/span'
        driver.find_element_by_xpath(xpath).click()
        # 日期排序
        id = 'js-sort'
        select_id = driver.find_element_by_id(id)
        Select(select_id).select_by_index(1)

        return driver

    def main(self):
        # try:
        driver = self.chrome(self.url)
        # 進入登入頁面
        # driver = self.login(driver)
        # 查詢工作內容、地區
        driver = self.search_job_name_and_city(driver)
        """
        # 職務類別
        driver.find_element_by_id('ijob').click()
        time.sleep(2)
        #       學術╱教育╱輔導類
        driver = JobCategoryMenu().academic_education_counseling(driver)
        #       FAE
        driver = JobCategoryMenu().operation_technology_maintenance(driver, "FAE")
        #      資訊軟體系統類
        driver = JobCategoryMenu().information_software_system(driver, )
        #       測試人員
        driver = JobCategoryMenu().manufacturing_qualityControl_sanitation(driver, "測試人員")
     
        # 職務類別 確定
        js = 'javascript:obj_e104menu2011.sendBack();'
        driver.execute_script(js)
        """
        #       關鍵字 (例如: 工作職稱)

        driver.find_element_by_id("ikeyword").send_keys("")
        time.sleep(2)
        # 搜尋
        driver.find_element_by_css_selector(".btn.btn-primary.js-formCheck").click()
        time.sleep(2)

        # 查詢 工作條件 (經歷要求、日期排序)
        driver = self.search_condition(driver)

        time.sleep(1)
        # 查詢後有幾筆頁面
        option_page_count = \
            driver.find_element_by_css_selector('.page-select.js-paging-select.gtm-paging-top'). \
                find_elements_by_tag_name("option").__len__()

        print("全部共 %d 頁" % option_page_count)
        for i in range(1, option_page_count + 1):
            print("第 %d 頁" % i)
            #
            self.job_list(driver)
            time.sleep(5)
            # 換頁
            if i < option_page_count:
                # 換下一頁
                Select(driver.find_element_by_css_selector(
                    '.page-select.js-paging-select.gtm-paging-top')).select_by_index(i)
            time.sleep(2)
            print("-----------------------------------")

        driver.quit()
        # exit()

    # time.sleep(100000)
    # except:
    #     self.log_mess.main("error")
    #     print("error")
    # finally:
    #     time.sleep(10)
    #     self.log_mess.main("結束")

    # // *[ @ id = "js-job-content"] / article[1] / div[1] / h2 / a
    # // *[ @ id = "js-job-content"] / article[20] / div[1] / h2 / a


if __name__ == "__main__":
    Job().main()
