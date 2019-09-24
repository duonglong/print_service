from pyppeteer import launch


class HtmlToPdf(object):
    """Convert HTML To PDF Using Pyppeteer"""

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
        browser = await launch()
        page = await browser.newPage()
        response = await page.goto(url)
        await page.pdf(options)
        await browser.close()
        return response.status


converter = HtmlToPdf()
