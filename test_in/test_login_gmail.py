from pages import logging_page


class Test_Loging_():
    # @classmethod
    # def setUpClass(cls):
    #     cls.login = "ptest9695@gmail.com"
    #     cls.password = "test01#21"
    #     super(Test_Loging_,cls)

    def test_login_gmail(self, invoke):
        '''

        :param invoke:
        :return:
        '''
        login = "ptest9695@gmail.com"
        password = "test01#21"

        loggin_page = logging_page.LoggingPage(invoke)
        loggin_page.go_to_logging_page()
        loggin_page.do_login(login, password)

        #1

    #3

