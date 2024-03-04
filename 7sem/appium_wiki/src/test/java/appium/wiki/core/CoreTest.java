package appium.wiki.core;

import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;

public class CoreTest {
    protected AppiumDriver driver;
    private final String AppiumURL = "http://127.0.0.1:4723/";

    public void setUp() throws Exception {
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability(AppiumCapabilities.PLATFORM_NAME, "Android");
        capabilities.setCapability(AppiumCapabilities.DEVICE_NAME, "emulator-5554");
        capabilities.setCapability(AppiumCapabilities.PLATFORM_VERSION, "11");
        capabilities.setCapability(AppiumCapabilities.AUTOMATION_NAME, "UiAutomator2");
        capabilities.setCapability(AppiumCapabilities.APP_PACKAGE, "org.wikipedia");
        capabilities.setCapability(AppiumCapabilities.APP_ACTIVITY, "org.wikipedia.main.MainActivity");
        driver = new AndroidDriver(new URL(AppiumURL), capabilities);
    }

    public void tearDown() {
        driver.quit();
    }

}
