package appium.wiki.testCase;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import appium.wiki.core.CoreTest;
import appium.wiki.core.ui.ArticleDetailsPage;
import appium.wiki.core.ui.ReadListPage;
import appium.wiki.core.ui.SearchComponent;
import appium.wiki.core.ui.StartPage;

public class ReadList extends CoreTest {
    private SearchComponent searchComponent;
    private ArticleDetailsPage articleDetailsPage;
    private ReadListPage readListPage;
    private StartPage startPage;

    @Before
    public void setUp() throws Exception {
        super.setUp();
        searchComponent = new SearchComponent(this.driver);
        articleDetailsPage = new ArticleDetailsPage(this.driver);
        readListPage = new ReadListPage(this.driver);
        startPage = new StartPage(this.driver);
    }

    @After
    public void tearDown() {
        super.tearDown();
    }

    @Test
    public void testReadList() {
        startPage.skipPage();
        // Поиск нужной статьи
        searchComponent
                .initSearchInput()
                .typeSearchLine("Хоббит, или Туда и обратно")
                .waitForSearchResultAndClick("повесть английского писателя Джона Р. Р. Толкина");
        // Добавление статьи в список для чтения и переход на страницу списков
        articleDetailsPage
                .addArticleToNewReadList("Хоббит")
                .goReadList();

        // выбор списка для чтения и удаление статьи
        Boolean isVisible = readListPage
                .deleteReadList()
                .checkReadList("Хоббит");
        Assert.assertFalse(isVisible);
    }
}
