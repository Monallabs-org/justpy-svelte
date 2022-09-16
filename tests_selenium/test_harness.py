from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 

import aiohttp
import time
from jpcore.justpy_app import JustpyServer

#driver = webdriver.Chrome("/usr/bin/chromium-browser")
def get_browser(browser_type="firefox"):
    browser = None
    if browser_type == "firefox":
        options = FirefoxOptions()
        options.headless = True
        browser = webdriver.Firefox(options=options)

    if browser_type == "chrome":
        # unable to install webdriver_manager
        options = ChromeOptions()
        options.headless = True
        #chrome_executable = ChromeDriverManager(cache_valid_range=365).install()
        service = ChromeService()
        browser = webdriver.Chrome("/usr/bin/chromium-browser",
                                   service=service,
                                   options=options)
    return browser


def get_driver(browser, timeout: float = 5.0):
    driver = WebDriverWait(browser, timeout)
    return driver


async def launch_webapp_server(host="127.0.0.1",
                         port=8123,
                         debug=False,
                         profile=True,
                         mode=None):
    """
    launches a webapp server and returns a controlPanel function-object
    """
    # fireup here
    sleep_time = 2.0
    server = JustpyServer(
        port=port, host=host, sleep_time=sleep_time, mode=mode, debug=debug
    )
    starttime = time.time()
    await server.start()
    def controlPanel():
        def tear_down():
            if server is not None:
                server.stop()
            controlPanel.elapsed = time.time() - starttime
            pass

        def getUrl(path):
            url = f"http://{self.server.host}:{self.server.port}{path}"
            return url
        
        def getServer():
            return server
        
        async def getResponseHtml(path):
            async with aiohttp.ClientSession() as session:
                url = getUrl(path)
                async with session.get(url) as resp:
                    rawhtml = await resp.content.read()
                    status = resp.status
            return status, rawhtml

        controlPanel.getServer = getServer
        controlPanel.tear_down = tear_down
        controlPanel.getUrl = getUrl
        controlPanel.getResponseHtml = getResponseHtml
    controlPanel()
    return controlPanel


def setup(timeout: float = 5.0):
    """
    setup for test: launch webapp server and then get the browser
    """
    browser = get_browser()
    driver = WebDriverWait(browser, timeout)
    server_control_panel = launch_webapp_server()
    return server_control_panel, browser, driver


# def do_test():
#     # start the webapp server
#     server_control_panel, browser, driver = setup()
#     server_control_panel.start()
#     url = server_control_panel.server.get_url("/")
#     self.browser.get(url)
#     await asyncio.sleep(self.server.sleep_time)

#     # now you do your thing of finding what you need from the webpage.
#     browser.find_elements(By.TAG_NAME, "button")
#     # click the button
#     buttons[buttonIndex].click()
    
    


