
class Locators():

    # ----------- FIRST SEGMENT ------------
    CHROME_EXECUTABLE_PATH = r'C:/Users/gabri/OneDrive/Área de Trabalho/chromedriver.exe'
    MAIN_PAGE = 'https://www.instagram.com/'
    MOBILE_ARGUMENT = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

    # ----------- IMPORTANT ----------------

    CLOSE_BLACK_BAR = '/html/body/div[1]/section/div[3]/div/p[2]/div/button/span'

    # ----------- Instagram Home Page ------

    MAIN_PAGE_ENTER_BUTTON = '/html/body/div[1]/section/main/article/div/div/div/div[2]/button'
    USERNAME_INPUT = '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input'
    PASSWORD_INPUT = '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input'
    ENTER_BUTTON_LOGIN = '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button'

    # ----------- SAVE LOGIN INFORMATION ------

    NOT_NOW = '/html/body/div[1]/section/main/div/div/div/button'
    DONT_INITIAL_PAGE = '/html/body/div[4]/div/div/div/div[3]/button[2]'

    # ----------- FILE UPLOAD -----------------

    BUTTON_TO_UPLOAD_A_FILE = '/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]'
    SEND_FILE = '/html/body/div[1]/section/nav[2]/div/div/form/input'
    ADVANCE_BUTTON = '/html/body/div[1]/section/div[1]/header/div/div[2]/button'
    LEGEND_INPUT = '/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea'
    SHARE_BUTTON = '/html/body/div[1]/section/div[1]/header/div/div[2]/button'