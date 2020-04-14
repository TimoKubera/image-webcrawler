from selenium import webdriver;
from selenium.webdriver import ChromeOptions;
from selenium.webdriver import ActionChains;
import os;
import sys;
import pip._vendor.requests;
import shutil;

MIN_ARG_LEN = 2;
FLAG = 1;

# The path needs to be updated according to your installation path of the chromedriver.
chromedriver = "/usr/local/bin/chromedriver";
opts = ChromeOptions();
opts.headless = True;
driver = webdriver.Chrome(executable_path = chromedriver, options = opts);

# Searches for and prints the images.
dl = False;

def crawl(i):
    print("crawling " + sys.argv[i] + " ...");
    driver.get(sys.argv[i]);
    images = driver.find_elements_by_tag_name("img");
    # j counts the img elements
    j = 0;
    for ele in images:
        if ele.get_attribute("src"):
            print(ele.get_attribute("src"));
        else:
            continue;
        # Optionally download the images.
        if dl == True:
            download(ele.get_attribute("src"), i, j);
            # In the next step, 'save image as' needs to be selected,
            # which does not work using selenium.
            j += 1;
    print("");

# Downloads the images
def download(url, i , j):
    print("Downloading " + str(url) + " ...");
    response = pip._vendor.requests.get(url, stream = True);
    save_image(response, i, j);
    del response;

# Saves the images in the local downloads folder.
def save_image(img, i, j):
    with open((os.getcwd() + "/downloads/url_{i}_img_{j}").format(i = i - MIN_ARG_LEN, j = j), "wb") as out_file:
        shutil.copyfileobj(img.raw, out_file);


if len(sys.argv) < MIN_ARG_LEN:
    print("Please enter at least one valid URL!");
# Optionally download the images.
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