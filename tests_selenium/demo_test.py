import justpy as jp
import asyncio
from test_harness import setup as setup_test_harness

async def click_demo():
    wp = jp.WebPage()
    d = jp.Button(
        text="Not clicked yet",
        a=wp,
        classes="w-48 text-xl m-2 p-1 bg-blue-500 text-white",
    )
    clickCount  = 0
    
    async def onDivClick(self, msg):
        """
        handle a click on the Div
        """
        nonlocal clickCount
        clickCount += 1
        d.text = f"I was clicked {clickCount} times"
    d.on("click", onDivClick)
    return wp

# def verify_page_htmlcontent_on_browser():
#     divs = self.browser.find_elements(By.TAG_NAME, "div")
#     # get the clickable div
#     div = divs[1]
#     self.assertEqual("Not clicked yet", div.text)
#     for i in range(5):
#         div.click()
#         await asyncio.sleep(self.server.sleep_time)
#         self.assertEqual(f"I was clicked {i+1} times", div.text)
#     self.browser.close()
#     await asyncio.sleep(self.server.sleep_time)
#     await self.server.stop()
    
#     pass


async def demo_test():
    server_control_panel, browser, driver = await setup_test_harness()
    server  = server_control_panel.getServer()
    app = server.app()
    app.add_route("/", click_demo)
    url = app.get_url("/")
    browser.get(url)
    asyncio.sleep(server.sleep_time)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(demo_test())
print ("all completed task")
loop.close()
