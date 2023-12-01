package web.testing;

import java.time.Duration;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class MailTest {
    private WebDriver driver;
    private String siteUrl = "https://mail.ru/";
    private AuthFrame authFrame;
    private StartPage startPage;

    @Before
    public void setUp() {
        this.driver = new ChromeDriver();
        this.authFrame = new AuthFrame(this.driver);
        this.startPage = new StartPage(this.driver);
    }

    @After
    public void tearDown() {
        this.driver.quit();
    }

    @Test
    public void test() {
        this.driver.get(this.siteUrl);
        this.startPage.openAuthFrame();
        timeout(10);
        this.authFrame.auth("test_e.xpert", "test$1218");
        timeout(30);
        Assert.assertTrue(this.startPage.checkUsername("Тестовый Тестич"));
        this.startPage.logout();
        timeout(10);
        Assert.assertTrue(this.startPage.checkLoginButton());
    }

    private void timeout(long seconds) {
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(seconds));
    }
}
