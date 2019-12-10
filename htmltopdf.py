from pyppeteer import launch, connect
from configuration import CHROMIUM_PATH
import logging

class HtmlToPdf(object):
    """Convert HTML To PDF Using Pyppeteer"""

    def __init__(self):
        self.browser = None

    def set_session(self, browser):
        """
        Set browser's session
        :return:
        """
        pass

    async def html_to_pdf(self, url, options):
        """

        :param url: (string) url of the website
        :param options: (dict) {path: , width: , height: }
        :return: (int) response status
        """
        _logger = logging.getLogger('quart.serving')
        page = None
        try:
            if self.browser and self.browser._connection._connected:
                _logger.info("Using Existing Browser")
                self.browser = await connect({"browserWSEndpoint": self.browser.wsEndpoint})
            else:
                _logger.info("Lunching Browser")
                opts = {
                    "headless": True,
                    "args": [
                        "--proxy-server='direct://'",
                        "--proxy-bypass-list=*"
                    ],
                    "executablePath": CHROMIUM_PATH
                }
                self.browser = await launch(opts)
            _logger.info("Opening New Page")
            page = await self.browser.newPage()
            _logger.info("Going to: %s." % url)
            response = await page.goto(url, {"waitUntil": 'networkidle0'})
            await page.pdf(options)
            _logger.info("Closing Page")
            await page.close()
            _logger.info("Done: %s" % response.status)
            return response.status
        except Exception as e:
            if page:
                await page.close()
            _logger.info(e)
            return e


converter = HtmlToPdf()
