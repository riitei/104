from selenium import webdriver
import time
class Test:

    def test_dict(self, search_dict_key=""):
        dict = {
            "經營╱人資類": "e104menu2011_m_cb_0",
            "行政╱總務╱法務類": "e104menu2011_m_cb_1",
            "行銷╱企劃╱專案管理類": "e104menu2011_m_cb_2",
            "行銷類人員": "e104menu2011_m_cb_2_0",
            "產品企劃類人員": "e104menu2011_m_cb_2_1",
            "專案/產品類管理人員": "e104menu2011_m_cb_2_2",
            "客服╱門市╱業務╱貿易類": "e104menu2011_m_cb_3",
            "餐飲╱旅遊 ╱美容美髮類": "e104menu2011_m_cb_4",
            "資訊軟體系統類": "e104menu2011_m_cb_5",
            "軟體/工程類人員": "e104menu2011_m_cb_5_0",
            "MIS/網管類人員": "e104menu2011_m_cb_5_1",
            "操作╱技術╱維修類": "e104menu2011_m_cb_6",

            "操作技術類人員": "e104menu2011_m_cb_6_0",
            "維修/技術服務類人員": "e104menu2011_m_cb_6_1",
            "FAE": "e104menu2011_m_cb_6_1_15",

            "資材╱物流╱運輸類": "e104menu2011_m_cb_7",
            "營建╱製圖類": "e104menu2011_m_cb_8",
            "傳播藝術╱設計類": "e104menu2011_m_cb_9",
            "文字╱傳媒工作類": "e104menu2011_m_cb_10",
            "醫療╱保健服務類": "e104menu2011_m_cb_11",
            "學術╱教育╱輔導類": "e104menu2011_m_cb_12",
            "研發相關類": "e104menu2011_m_cb_13",
            "生產製造╱品管╱環衛類": "e104menu2011_m_cb_14",

            "生產管理類人員": "e104menu2011_m_cb_14_0",
            "製程規劃人員": "e104menu2011_m_cb_14_1",
            "品保/品管類人員": "e104menu2011_m_cb_14_2",
            "測試人員": "e104menu2011_m_cb_14_2_4",

            "軍警消╱保全類": "e104menu2011_m_cb_15",
            "財會╱金融專業類": "e104menu2011_m_cb_16",
            "其他職類": "e104menu2011_m_cb_17"

        }

        return dict[search_dict_key]


if __name__ == '__main__':
    t = Test().test_dict("生產管理類人員")
    print(t)
    driver = webdriver.Chrome()
    url = 'https://www.104.com.tw/jobs/main/'
    driver.get(url)
    # 職務類別
    driver.find_element_by_id('ijob').click()
    time.sleep(3)
    #       FAE
    driver.find_element_by_id('e104menu2011_m_cb_14_0').click()
    time.sleep(5)
    # 職務類別 確定
    js = 'javascript:obj_e104menu2011.sendBack();'
    driver.execute_script(js)
    time.sleep(5)
    driver.quit()