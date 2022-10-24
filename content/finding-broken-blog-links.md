Title: Finding Broken Blog Links
Date: 2022-10-24 16:00
Modified: 2022-10-24 16:00
Tags: Python, Blogging, Automation, GitHub, Github-Actions, CI/CD, Continuous-Integration, Continuous-Deployment
Category: Blogging
Slug: finding-broken-blog-links
Authors: Joe Stanley
Summary: Well, I just recently converted to a new Nextcloud instance at home. Gosh, I sure hope I wasn't using any of those links externally on any important websites like a blog, or anything... Oh. I was? Awkward...

It's something of a solved problem, but I thought I'd share the way that I solved it...

That's right, finding dead links is a common practice with hosting websites of any form, or fashion. Just a matter of determining how they should be checked, right?
Since I'm hosting my blog site from a GitHub-Pages GitHub-Action based deployment, I thought it would make the most sense to perform a little sanity check by way of
another GitHub Action. If you'd like to go see it's source, you can check it out
[here](https://github.com/engineerjoe440/stanley-solutions-blog/blob/master/.github/workflows/broken-link-detector.yml).

Or you could just look at the code... that's an option, too.

```yml
name: Broken Link Detector
on:
  schedule:
    # Runs every day at 1:00AM
    - cron: '0 1 * * *'
  workflow_dispatch:

jobs:
  find-broken-links:
    name: Find Broken Links
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.10
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install --upgrade lxml beautifulsoup4 requests
    - name: Find Broken Links
      run: |
        python broken-link-detector.py
```

But that doesn't *actually* find the dead links, it just runs the script responsible for finding them. We leave that little bit up to Python!

> What else would you have expected me to use. I mean, c'mon... really?!

I'll admit, I had some pretty helpful resources to lean on for ideas!

* https://brianli.com/2021/06/how-to-find-broken-links-with-python/
* https://www.webucator.com/article/checking-your-sitemap-for-broken-links-with-python/

I took those resources and made a couple of functions to help me out...

#### Checking for Dead Resources on a Page

I need to look at a few things to verify whether they point at valid resources:

* Links (`<a>` tags)
* Images (`<img>` tags)
* Videos (posters with `<video>` tags and video files with `<source>` tags)

This, with a little help from one of those other resources I mentioned, helped me to make a handy-dandy little function to find broken links on a page.

```python
def find_broken_resources(html_text):
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
        
    return len(failures) > 0
```

But that only finds broken resources on a single page. How am I going to do the whole website?

#### Checking Each URL from the Sitemap

So, there's a function for that, I got this one started up so that it could find all of the pages from the sitemap, and use that to parse each page.

```python
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
        if "/tag/" in url:
            break # Don't go over all the tags
        load_fail = False
        for _ in range(10):
            try:
                print(f"{i}. Checking {url}")
                r = requests.get(url)

                # Locate any broken resources on the page
                success &= find_broken_resources(html_text=r.text)

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
```

##### Closing Thoughts

So... Like I said. This isn't a new problem, or one that hasn't been solved before. But it's how *I* did it. Thanks for reading!