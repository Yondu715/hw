package appium.wiki.core.ui;

import org.openqa.selenium.By;

import io.appium.java_client.AppiumDriver;

public class StartPage extends MainPageObject {

    private String skipBtn = "//*[contains(@text, 'Пропустить')]";

    public StartPage(AppiumDriver driver) {
        super(driver);
    }

    public void skipPage() {
        this.waitForElementAndClick(By.xpath(skipBtn), "Невозможно нажать на кнопку Пропустить", 15);
    }
    
}
