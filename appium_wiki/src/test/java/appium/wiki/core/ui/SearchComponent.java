package appium.wiki.core.ui;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import io.appium.java_client.AppiumDriver;

public class SearchComponent extends MainPageObject {

    private String searchElement = "//*[contains(@text, 'Поиск по Википедии')]";
    private String searchResult = "//*[@resource-id='org.wikipedia:id/page_list_item_description' and @text='{SUBSTRING}']";

    public SearchComponent(AppiumDriver driver) {
        super(driver);
    }

    private String getResultSearchElement(String substring) {
        return searchResult.replace("{SUBSTRING}", substring);
    }

    public SearchComponent initSearchInput() {
        this.waitForElementAndClick(By.xpath(searchElement), "Невозможно нажать", 10);
        this.waitForElementPresent(By.xpath(searchElement), "Невозможно получить", 10);
        return this;
    }

    public SearchComponent typeSearchLine(String search) {
        this.waitForElementAndSendKeys(By.xpath(searchElement), search, "Невозможно найти поле ввода", 10);
        return this;
    }

    public SearchComponent waitForSearchResultAndClick(String result) {
        String searchResultXpath = getResultSearchElement(result);
        System.out.println("2312331231 " + searchResultXpath);
        WebElement searchResult = this.waitForElementPresent(By.xpath(searchResultXpath), "Невозможно найти " + result, 5);
        searchResult.click();
        return this;
    }
    
}
