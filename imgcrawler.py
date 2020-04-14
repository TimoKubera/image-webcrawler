from selenium import webdriver;
from selenium.webdriver import ChromeOptions;
from selenium.webdriver import ActionChains;
import sys

MIN_ARG_LEN = 2;
FLAG = 1;

# The path needs to be updated according to your installation path of the chromedriver.
chromedriver = "/usr/local/bin/chromedriver"
opts = ChromeOptions();
opts.headless = False;
driver = webdriver.Chrome(executable_path = chromedriver, options = opts);

# Searches for and prints the images.
dl = False;

def crawl(url):
    print("crawling " + sys.argv[url] + " ...");
    driver.get(str(sys.argv[url]));
    images = driver.find_elements_by_tag_name("img");
    for ele in images:
        print(ele.get_attribute("src"));
        # To do: Optionally download the images.
        if dl == True:
            ActionChains(driver).context_click(ele).perform();
            # In the next step, 'save image as' needs to be selected,
            # which does not work using selenium.
    print("");

if len(sys.argv) < MIN_ARG_LEN:
    print("Please enter at least one valid URL!");
# To do: Optionally download the images.
elif sys.argv[FLAG] == "-dl":
    dl = True;
    if len(sys.argv) < MIN_ARG_LEN + FLAG:
        print("Please enter at least one valid URL!");
    else:
        for i in range(2, len(sys.argv)):
            crawl(i);
# Search for the images.
else:
    for i in range(1, len(sys.argv)):
        crawl(i);

driver.close();