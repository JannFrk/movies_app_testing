from appium import webdriver


def driver_instance():
    """ Create a session appium server """
    desired_caps = {
        "platformName": "Android",
        "platfromVersion": "10",
        "deviceName": "Pixel3",
        "appPackage": "com.merqueo.debug",
        "appActivity": "com.merqueo.debug.activity.SplashActivity",
        "automationName": "UIAutomator2"
    }

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
