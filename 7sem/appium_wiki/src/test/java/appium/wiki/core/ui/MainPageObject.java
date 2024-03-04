package appium.wiki.core.ui;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.appium.java_client.AppiumDriver;

public class MainPageObject {
    protected AppiumDriver driver;

    public MainPageObject(AppiumDriver driver) {
        this.driver = driver;
    }

    protected WebElement waitForElementPresent(By by, String error_msg, long timeoutInSeconds) {
        WebDriverWait webDriverWait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
        webDriverWait.withMessage(error_msg + '\n');
        return webDriverWait.until(ExpectedConditions.presenceOfElementLocated(by));
    }

    protected WebElement waitForElementAndClick(By by, String error_msg, long timeoutInSeconds) {
        WebElement webElement = waitForElementPresent(by, error_msg, timeoutInSeconds);
        webElement.click();
        return webElement;
    }

    protected WebElement waitForElementAndSendKeys(By by, String value, String error_msg, long timeoutInSeconds) {
        WebElement webElement = waitForElementPresent(by, error_msg, timeoutInSeconds);
        webElement.sendKeys(value);
        return webElement;
    }

    protected WebElement waitForElementAndClear(By by, String error_msg, long timeoutInSeconds) {
        WebElement webElement = waitForElementPresent(by, error_msg, timeoutInSeconds);
        webElement.clear();
        return webElement;
    }

    protected WebElement waitForElementAndHold(By by, String error_mgs, long timeoutInSeconds) {
        WebElement webElement = waitForElementPresent(by, error_mgs, timeoutInSeconds);
        Actions actions = new Actions(driver);
        actions.clickAndHold(webElement).perform();;
        return webElement;
    }
}
