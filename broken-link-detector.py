################################################################################
"""
Broken Link Detector for Stanley Solutions Blogsite
"""
################################################################################

import sys
import time
import requests
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sitemaps = [
    "https://blog.stanleysolutionsnw.com/sitemap.xml",
]


def find_broken_resources(html_text):
    """
    Find broken resources on a single page:
    * images (<img> tag)
    * links (<a> tag)
    * video posters (<video> tag)
    * videos (<source> tag)
    """
    failures = []

    # Set root domain.
    root_domain = "stanleysolutionsnw.com"
    
    # Internal function for validating HTTP status code.
    def _validate_url(url):
        r = requests.head(url)
        if r.status_code == 404:
            print("    Broken Link!\n    " + url)
            failures.append(url)
    
    # Parse HTML from request.
    soup = BeautifulSoup(html_text, features="html.parser")
    
    # Create a list containing all links with the root domain.
    links = [l.get("href") for l in soup.find_all("a", href=True) if f"{root_domain}" in l.get("href")]
    imgs = [i.get("src") for i in soup.find_all("img", src=True) if f"{root_domain}" in i.get("src")]
    vid_posters = [v.get("poster") for v in soup.find_all("video") if f"{root_domain}" in v.get("poster")]
    vids = [v.get("src") for v in soup.find_all("source") if f"{root_domain}" in v.get("src")]
    
    # Loop through links checking for 404 responses.
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(_validate_url, links)
    
    # Loop through images checking for 404 responses.
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(_validate_url, imgs)
    
    # Loop through videos checking for 404 responses.
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(_validate_url, vid_posters)
    
    # Loop through videos checking for 404 responses.
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(_validate_url, vids)
        
    if len(failures) > 0:
        for failed_url in failures:
            print(f"  Failed to access resource: {failed_url}")
        return True


def check_sitemap_urls(sitemap, limit=100):
    """Attempts to resolve all urls in a sitemap and returns the results

    Args:
        sitemap (str): A URL
        limit (int, optional): The maximum number of URLs to check. Defaults to 50.
            Pass None for no limit.

    Returns:
        list of tuples: [(status_code, history, url, msg)].
            The history contains a list of redirects.
    """
    success = True
    res = requests.get(sitemap)
    doc = etree.XML(res.content)

    # xpath query for selecting all element nodes in namespace
    query = "descendant-or-self::*[namespace-uri()!='']"
    # for each element returned by the above xpath query...
    for element in doc.xpath(query):
        # replace element name with its local name
        element.tag = etree.QName(element).localname

    # get all the loc elements
    links = doc.xpath(".//loc")
    for i, link in enumerate(links, 1):
        url = link.text
        if "/tag/" in url or "/category/" in url:
            break # Don't go over all the tags or categories
        load_fail = False
        for _ in range(10):
            try:
                print(f"{i}. Checking {url}")
                r = requests.get(url)

                # Locate any broken resources on the page
                success &= not find_broken_resources(html_text=r.text)

                load_fail = False
                break

            except Exception as e:
                print(f"Retry... caused by: {e}")
                load_fail = True
                time.sleep(2)
        if load_fail:
            print("    Failed to load page:\n    " + url)
            success = False

        if limit and i >= limit:
            break
    return success


def main():
    success = True
    for sitemap in sitemaps:
        success &= check_sitemap_urls(sitemap)
    if not success:
        sys.exit(1)

main()