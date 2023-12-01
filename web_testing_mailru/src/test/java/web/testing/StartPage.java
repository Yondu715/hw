package web.testing;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class StartPage {
    private WebDriver driver;
    private String loginButton = "//button[@class='resplash-btn resplash-btn_primary resplash-btn_mailbox-big iimegem-de8k2m']";
    private String userAvatar = "//*[@class='ph-avatar-img svelte-dfhuqc']";
    private String userName = "//*[@class='ph-name svelte-1popff4']";
    private String logoutButton = "//*[text()='Выйти']";

    public StartPage(WebDriver driver) {
        this.driver = driver;
    }

    public void openAuthFrame() {
        this.driver.findElement(By.xpath(this.loginButton)).click();
    }

    public void logout() {
        this.driver.findElement(By.xpath(this.logoutButton)).click();
    }

    public boolean checkUsername(String username) {
        this.driver.findElement(By.xpath(this.userAvatar)).click();
        String userName = this.driver.findElement(By.xpath(this.userName)).getText();
        return userName.equals(username);
    }

    public boolean checkLoginButton() {
        return this.driver.findElement(By.xpath(this.loginButton)).isDisplayed();
    }
}
