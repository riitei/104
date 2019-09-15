import time


class JobCategoryMenu:

    # 經營╱人資類_ALL
    def business_personnel(self, driver, name="all"):
        driver.find_element_by_id('ijob').click()
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_0').click()
            self.job_category_list_close(driver)
        return driver

    # 行政╱總務╱法務類
    def administration_generalAffairs_legalAffairs(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_1').click()
            self.job_category_list_close(driver)

        return driver

    # 行銷╱企劃╱專案管理類
    def marketing_planning_projectManagement(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_2').click()
            self.job_category_list_close(driver)
            return driver
        else:
            driver.find_element_by_xpath('//*[@id="e104menu2011_m_i_2"]/a').click()
            time.sleep(2)

        # 行銷類人員
        if name == '行銷類人員':
            driver.find_element_by_id('e104menu2011_m_cb_2_0').click()
            self.job_category_list_close(driver)
            return driver
        # 產品企劃類人員
        if name == '產品企劃類人員':
            driver.find_element_by_id('e104menu2011_m_cb_2_1').click()
            self.job_category_list_close(driver)
            return driver
        # 專案／產品類管理人員
        if name == '專案/產品類管理人員':
            driver.find_element_by_id('e104menu2011_m_cb_2_2').click()
            self.job_category_list_close(driver)
            return driver

    # 客服╱門市╱業務╱貿易類
    def customerService_tuenMun_business_trade(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_3').click()
            self.job_category_list_close(driver)

        return driver

    #  餐飲╱旅遊 ╱美容美髮類
    def foodBeverage_tourism_beautySalon(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_4').click()
            self.job_category_list_close(driver)

        return driver

    # 資訊軟體系統類
    def information_software_system(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_5').click()
            self.job_category_list_close(driver)
            return driver
        else:
            driver.find_element_by_xpath('//*[@id="e104menu2011_m_i_5"]/a')
            time.sleep(2)

        # 軟體/工程類人員
        if name == '軟體/工程類人員':
            driver.find_element_by_id('e104menu2011_m_cb_5_0').click()
            self.job_category_list_close(driver)
            return driver

        # MIS/網管類人員
        if name == 'MIS/網管類人員':
            driver.find_element_by_id('e104menu2011_m_cb_5_1').click()
            self.job_category_list_close(driver)
            return driver

    # 操作╱技術╱維修類
    def operation_technology_maintenance(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_6').click()
            self.job_category_list_close(driver)
            return driver
        else:
            driver.find_element_by_xpath('//*[@id="e104menu2011_m_i_6"]/a').click()
            time.sleep(2)
        # 操作技術類人員
        if name == "操作技術類人員":
            driver.find_element_by_id('e104menu2011_m_cb_6_0').click()
            self.job_category_list_close(driver)
            return driver

        # 維修/技術服務類人員
        if name == "維修/技術服務類人員":
            driver.find_element_by_id('e104menu2011_m_cb_6_1').click()
            self.job_category_list_close(driver)
            return driver
        else:
            # FAE
            if name == "FAE":
                driver.find_element_by_id('e104menu2011_m_cb_6_1_15').click()
                self.job_category_list_close(driver)
                return driver
        #

    # 資材╱物流╱運輸類
    def materials_logistics_transportation(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_7').click()
            self.job_category_list_close(driver)
        return driver

    # 營建╱製圖類
    def construction_drawing(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_8').click()
            self.job_category_list_close(driver)

        return driver

    # 傳播藝術╱設計類
    def communication_artDesign(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_9').click()
            self.job_category_list_close(driver)
        return driver

    # 文字╱傳媒工作類
    def text_mediaWork(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_10').click()
            self.job_category_list_close(driver)
        return driver

    # 醫療╱保健服務類
    def medical_careService(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_11').click()
            self.job_category_list_close(driver)
        return driver

    # 學術╱教育╱輔導類
    def academic_education_counseling(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_12').click()
            self.job_category_list_close(driver)
        return driver

    # 研發相關類
    def rd_related(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_13').click()
            self.job_category_list_close(driver)
        return driver

    # 生產製造╱品管╱環衛類
    def manufacturing_qualityControl_sanitation(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_14').click()
            self.job_category_list_close(driver)
            return driver
        else:
            driver.find_element_by_xpath('//*[@id="e104menu2011_m_i_14"]/a').click()
            time.sleep(2)

        # 生產管理類人員
        if name == '生產管理類人員':
            driver.find_element_by_id('e104menu2011_m_cb_14_0').click()
            self.job_category_list_close(driver)
            return driver
        # 製程規劃人員
        if name == '製程規劃人員':
            driver.find_element_by_id('e104menu2011_m_cb_14_1').click()
            self.job_category_list_close(driver)
            return driver
        # 品保/品管類人員
        if name == '品保/品管類人員':
            driver.find_element_by_id('e104menu2011_m_cb_14_2').click()
            self.job_category_list_close(driver)
            return driver
        else:
            # 測試人員
            if name == '測試人員':
                driver.find_element_by_id('e104menu2011_m_cb_14_2_4').click()
                self.job_category_list_close(driver)
                return driver

        # 環境安全衛生類人員
        if name == '環境安全衛生類人員':
            driver.find_element_by_id('e104menu2011_m_cb_14_3').click()
            self.job_category_list_close(driver)
            return driver

    #  軍警消╱保全類
    def military_police_security(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_15').click()
            self.job_category_list_close(driver)
        return driver

    # 財會╱金融專業類
    def finance_finance(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_16').click()
            self.job_category_list_close(driver)
        return driver

    # 其他職類
    def other_categories(self, driver, name='all'):
        time.sleep(2)
        if name == 'all':
            driver.find_element_by_id('e104menu2011_m_cb_17').click()
            self.job_category_list_close(driver)
        return driver

    # 關閉工作分類小視窗
    def job_category_list_close(self, driver):
        time.sleep(1)
        driver.find_element_by_class_name('e104menu2011_txt_normal').click()
        time.sleep(1)
