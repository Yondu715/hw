package appium.wiki.core.ui;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import io.appium.java_client.AppiumDriver;

public class ReadListPage extends MainPageObject {

    private String actionListElement = "//*[@content-desc='Ещё']";
    private String deleteActionElement = "//*[@resource-id='org.wikipedia:id/title' and @text='Удалить список']";
    private String submitActionElement = "//*[@resource-id='android:id/button1']";
    private String readListElement = "//*[@resource-id='org.wikipedia:id/item_title' and @text='{SUBSTRING}']";

    public ReadListPage(AppiumDriver driver) {
        super(driver);
    }

    private String getReadList(String substring) {
        return readListElement.replace("{SUBSTRING}", substring);
    }

    public ReadListPage deleteReadList() {
        this.waitForElementAndClick(By.xpath(actionListElement), "Невозможно нажать на кнопку Еще", 10);
        this.waitForElementAndClick(By.xpath(deleteActionElement), "Невозможно нажать на кнопку Удалить список", 10);
        this.waitForElementAndClick(By.xpath(submitActionElement), "Невозможно нажать на кнопку ОК", 10);
        return this;
    }

    public Boolean checkReadList(String name) {
        String readListXpath = getReadList(name);
        List<WebElement> webElements = driver.findElements(By.xpath(readListXpath));
        return webElements.size() == 0 ? false : true;
    }

 

}
