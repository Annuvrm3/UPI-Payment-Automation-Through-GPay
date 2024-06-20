import traceback
import socket
from appium.options.android import UiAutomator2Options
from appium import webdriver
import time
import logging
from appium.webdriver.common.appiumby import AppiumBy

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_available_ports(from_port: int, to_port: int) -> int:
    """
    Get an available port in a certain range.

    :param from_port: Lower limit.
    :param to_port: Upper limit.
    :return: An available port.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(from_port, to_port):
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()


class GPayAutomation:
    def __init__(self):
        OPTIONS = UiAutomator2Options()

        OPTIONS.platform_name = "Android"
        OPTIONS.device_name = "10BD1H0YHE00154"
        OPTIONS.platform_version = "14.0"
        OPTIONS.app_package = "com.google.android.apps.nbu.paisa.user"
        OPTIONS.app_activity = "com.google.nbu.paisa.flutter.gpay.app.LauncherActivity"

        OPTIONS.no_reset = True
        OPTIONS.ensure_webviews_have_pages = True
        OPTIONS.native_web_screenshot = True
        OPTIONS.new_command_timeout = 3600
        OPTIONS.connect_hardware_keyboard = True
        OPTIONS.clear_system_files = True
        OPTIONS.is_headless = False
        OPTIONS.system_port = get_available_ports(8100, 8200)

        SERVER_URL = "http://127.0.0.1:4723"
        
        logger.info("Initializing Appium driver...")
        try:
            self.driver = webdriver.Remote(SERVER_URL, options=OPTIONS)
            logger.info("Appium driver initialized successfully.")
        except Exception as e:
            logger.error("Failed to initialize Appium driver.")
            logger.error(e)
            raise
        
        # Define locators
        # self.payPhoneNumber = "//android.widget.Button[@content-desc='Pay phone number']"
        # self.phoneNumberField = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText"
        # self.resultPeople = "//android.widget.Button[@content-desc='SOUMYA PRAKASH SATAPATHY 7377164377@paytm']"
        # self.continueButton = "//android.widget.Button[@content-desc='Continue']"
        # self.payButton = "//android.widget.Button[@content-desc='Pay']"
        #continue from hear for soumya's number
        self.PayContacts = "//android.widget.Button[@content-desc='Pay anyone on UPI, Pay friends and merchants, Pay by name or phone number']"
        self.searchField = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText"
        self.name = "//android.widget.Button[@content-desc='Ashish Jajoria']"
        self.messageBox = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText"
        self.send = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.Button"
        self.pin1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TextView[1]"
        self.pin2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TextView[2]"
        self.pin3 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TextView[3]"
        self.pin4 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.TextView[1]"
        self.pin5 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.TextView[2]"
        self.pin6 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.TextView[3]"
        self.pin7 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.TextView[1]"
        self.pin8 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.TextView[2]"
        self.pin9 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.TextView[3]"

    def click_element(self, locator, by="xpath"):
        if by == "xpath":
            self.driver.find_element(by=AppiumBy.XPATH,value=locator).click()
        # Add other locators types if needed (id, class_name, etc.)

    def send_keys(self, text, locator, by="xpath"):
        if by == "xpath":
            self.driver.find_element(by=AppiumBy.XPATH,value=locator).send_keys(text)
        # Add other locators types if needed (id, class_name, etc.)

    def send_message(self):
        try:
            # self.click_element(self.PayContacts, "xpath")
            # self.send_keys(number, self.searchField, "xpath")
            self.click_element(self.name, "xpath")
            self.click_element(self.messageBox, "xpath")
            self.send_keys("1", self.messageBox, "xpath")
            self.click_element("//android.widget.Button[@content-desc='Pay Ashish ₹1']", "xpath")
            self.click_element("//android.widget.Button[@content-desc='Pay ₹1']", "xpath")

            self.click_element(self.pin8, "xpath")
            self.click_element(self.pin7, "xpath")
            self.click_element(self.pin5, "xpath")
            self.click_element(self.pin7, "xpath")
            self.click_element(self.pin3, "xpath")
            self.click_element(self.pin1, "xpath")

            self.click_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[4]/android.widget.ImageView[2]", "xpath")
            # self.click_element(self.send, "xpath")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            print(f"Following exception found: \n{e}")

    def __main__(self):
        self.send_message()
        time.sleep(5)  # Wait for app to load
        self.driver.quit()


if __name__ == "__main__":
    try:
        automation = GPayAutomation()
        automation.__main__()
    except Exception as e:
        logger.error("Failed to execute automation script.")
        logger.error(e)
