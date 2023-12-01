package web.testing;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class AuthFrame {

    private WebDriver driver;
    private String frameCs = "ag-popup__frame__layout__iframe";
    private String inputLogin = "//input[contains(@name,'username')]";
    private String inputPassword = "//input[contains(@name, 'password')]";
    private String nextStep = "//span[text()='Ввести пароль']";
    private String lastStep = "//span[text()='Войти']";

    public AuthFrame(WebDriver driver) {
        this.driver = driver;
    }

    public void auth(String login, String password) {
        WebElement authFrame = this.driver.findElement(By.className(this.frameCs));
        this.driver.switchTo().frame(authFrame);
        getInputAndSendKeys(By.xpath(this.inputLogin), login);
        this.driver.findElement(By.xpath(this.nextStep)).click();
        getInputAndSendKeys(By.xpath(this.inputPassword), password);
        this.driver.findElement(By.xpath(this.lastStep)).click();
        this.driver.switchTo().defaultContent();
    }

    private void getInputAndSendKeys(By by, String keys) {
        WebElement input = this.driver.findElement(by);
        input.clear();
        input.sendKeys(keys);
    }
}
