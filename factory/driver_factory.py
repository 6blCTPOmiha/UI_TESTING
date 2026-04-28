from selenium import webdriver


class DriverFactory:

    @staticmethod
    def create_driver(browser: str, remote: bool = False, grid_url: str = None):

        if remote:
            return DriverFactory._create_remote_driver(browser, grid_url)

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            return webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _create_remote_driver(browser, grid_url):

        if browser == "chrome":
            options = webdriver.ChromeOptions()

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()

        elif browser == "edge":
            options = webdriver.EdgeOptions()

        else:
            raise ValueError("Unsupported browser for Grid")

        return webdriver.Remote(command_executor=grid_url, options=options)
