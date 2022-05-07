import time
import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        elements = homepage_nav.get_nav_links_text()
        assert elements == homepage_nav.NAV_LINK_TEXT_WIDTH_GT1000, 'Headers are not equal'
        homepage_nav.get_nav_link_by_name('brands').click()
        time.sleep(5)