import os.path

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilites import randomeString
from utilites import readProperties
from utilites.customLogger import LogGen
from utilites.readProperties import ReadConfig


class Test_001_AccountReg:
    # baseURL = "https://demo-opencart.com/"
    baseURL = ReadConfig.getApplicationURL()  # thr url will  come from readproperties.py file which is have
    # ReadConfig class
    logger = LogGen.loggen()  # logger object is comes from customLogger.py file loggen is static method
    
    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("****** test_001AccountRegistration stated *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("****** Launching application *********")
        
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        self.hp = HomePage(self.driver)
        self.logger.info("****** Cliking on my accout *********")
        
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("****** started entering registration details *********")
        
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("****** Providing detauls *********")
        
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        # self.regpage.setEmail("abcdkjf@gmail.com")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("6565656553")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        # self.driver.close()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("****** test__AccoutRegistration Passed *********")
            
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshorts\\" + "test_accountreg3.png")
            self.logger.error("****** test__AccoutRegistration Failed *********")
            
            self.driver.close()
            assert False
        self.logger.info("****** test_001AccountRegistration finished *********")
