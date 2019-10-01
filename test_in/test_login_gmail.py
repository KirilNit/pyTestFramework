from pages import logging_page


class Test_Loging_():

    def test_login_gmail(self, invoke):
        login = "ptest9695@gmail.com"
        password = "test01#21"
        loggin_page = logging_page.LoggingPage(invoke)
        loggin_page.go_to_logging_page()
        loggin_page.do_login(login, password)
