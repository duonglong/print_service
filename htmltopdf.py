from pyppeteer import launch, connect
from configuration import CHROMIUM_PATH
import logging
import psutil


class HtmlToPdf(object):
    """Convert HTML To PDF Using Pyppeteer"""

    def __init__(self):
        self.browser = None
        self.browser_pid = None

    def set_session(self, browser):
        """
        Set browser's session
        :return:
        """
        pass

    async def ainit(self):
        _logger = logging.getLogger('quart.serving')
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
        self.browser_pid = self.browser.process.pid

    async def html_to_pdf(self, url, options):
        """

        :param url: (string) url of the website
        :param options: (dict) {path: , width: , height: }
        :return: (int) response status
        """

        page = None
        _logger = logging.getLogger('quart.serving')
        try:
            if self.browser_pid and psutil.pid_exists(self.browser_pid):
                _logger.info("Using Existing Browser")
                # Browser's connection becomes stale after few second ?
                self.browser = await connect({"browserWSEndpoint": self.browser.wsEndpoint})
            else:
                await self.ainit()
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

