package appium.wiki.core.ui;

import org.openqa.selenium.By;

import io.appium.java_client.AppiumDriver;

public class ArticleDetailsPage extends MainPageObject {
    private String saveElement = "//*[@content-desc='Сохранить']";
    private String addToListElement = "//*[@resource-id='org.wikipedia:id/snackbar_action']";
    private String inputListNameElement = "//*[@resource-id='org.wikipedia:id/text_input']";
    private String submitCreateListElement = "//*[@resource-id='android:id/button1']";
    private String checkReadListElement = "//*[@resource-id='org.wikipedia:id/snackbar_action']";

    public ArticleDetailsPage(AppiumDriver driver) {
        super(driver);
    }

    public ArticleDetailsPage addArticleToNewReadList(String articleName) {
        this.waitForElementAndClick(By.xpath(saveElement), "Невозможно нажать на кнопку Сохранить", 10);
        this.waitForElementAndClick(By.xpath(addToListElement), "Невозможно нажать на кнопку Добавить", 10);
        this.waitForElementAndSendKeys(By.xpath(inputListNameElement), articleName, "Невозможно найти поле ввода", 10);
        this.waitForElementAndClick(By.xpath(submitCreateListElement), "Невозможно нажать на кнопку ОК", 10);
        return this;
    }

    public ArticleDetailsPage goReadList() {
        this.waitForElementAndClick(By.xpath(checkReadListElement), "Невозможно нажать на кнопку Посмотреть список", 10);
        return this;
    }
    
}
