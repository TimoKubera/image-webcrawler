from selenium import webdriver;
from selenium.webdriver import ChromeOptions;
import sys

# The path needs to be updated according to your installation path of the chromedriver.
chromedriver = "/usr/local/bin/chromedriver"
opts = ChromeOptions();
opts.headless = True;
driver = webdriver.Chrome(executable_path = chromedriver, options = opts);

# Searches for and prints the images.
if len(sys.argv) <=1:
    print("Please enter at least one valid URL!");
else:
    for i in range(1, len(sys.argv)):
        print("crawling " + sys.argv[i] + " ...");
        driver.get(str(sys.argv[i]));
        images = driver.find_elements_by_tag_name("img");
        for ele in images:
            print(ele.get_attribute("src"));
        print("");

driver.close();