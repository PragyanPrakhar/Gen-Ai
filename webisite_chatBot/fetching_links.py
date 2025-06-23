# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse

# def get_internal_links(base_url):
#     response = requests.get(base_url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     print("Soaps are :-> ",soup);

#     base_domain = urlparse(base_url).netloc
#     links = set()

#     for a_tag in soup.find_all("a", href=True):
#         href = a_tag["href"]
#         full_url = urljoin(base_url, href)
#         if urlparse(full_url).netloc == base_domain:
#             links.add(full_url)
#     print(f"Found {len(links)} internal links on {base_url}",links)
#     return list(links)

# Replace this function with a manual list
def get_manual_links():
    return [
        "https://docs.chaicode.com/youtube/chai-aur-c/control-flow/",
        "https://docs.chaicode.com/youtube/chai-aur-c/data-types/",
        "https://docs.chaicode.com/youtube/chai-aur-c/functions/",
        "https://docs.chaicode.com/youtube/chai-aur-c/hello-world/",
        "https://docs.chaicode.com/youtube/chai-aur-c/introduction/",
        "https://docs.chaicode.com/youtube/chai-aur-c/loops/",
        "https://docs.chaicode.com/youtube/chai-aur-c/operators/",
        "https://docs.chaicode.com/youtube/chai-aur-c/variables-and-constants/",
        "https://docs.chaicode.com/youtube/chai-aur-c/welcome/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/nginx-rate-limiting/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/nginx-ssl-setup/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/node-logger/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/node-nginx-vps/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/postgresql-docker/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/postgresql-vps/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/setup-nginx/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/setup-vpc/",
        "https://docs.chaicode.com/youtube/chai-aur-devops/welcome/",
        "https://docs.chaicode.com/youtube/chai-aur-django/getting-started/",
        "https://docs.chaicode.com/youtube/chai-aur-django/jinja-templates/",
        "https://docs.chaicode.com/youtube/chai-aur-django/models/",
        "https://docs.chaicode.com/youtube/chai-aur-django/relationships-and-forms/",
        "https://docs.chaicode.com/youtube/chai-aur-django/tailwind/",
        "https://docs.chaicode.com/youtube/chai-aur-django/welcome/",
        "https://docs.chaicode.com/youtube/chai-aur-git/behind-the-scenes/",
        "https://docs.chaicode.com/youtube/chai-aur-git/branches/",
        "https://docs.chaicode.com/youtube/chai-aur-git/diff-stash-tags/",
        "https://docs.chaicode.com/youtube/chai-aur-git/github/",
        "https://docs.chaicode.com/youtube/chai-aur-git/introduction/",
        "https://docs.chaicode.com/youtube/chai-aur-git/managing-history/",
        "https://docs.chaicode.com/youtube/chai-aur-git/terminology/",
        "https://docs.chaicode.com/youtube/chai-aur-git/welcome/",
        "https://docs.chaicode.com/youtube/chai-aur-html/emmit-crash-course/",
        "https://docs.chaicode.com/youtube/chai-aur-html/html-tags/",
        "https://docs.chaicode.com/youtube/chai-aur-html/introduction/",
        "https://docs.chaicode.com/youtube/chai-aur-html/welcome/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/database-design-exercise/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/introduction/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/joins-and-keys/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/joins-exercise/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/normalization/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/postgres/",
        "https://docs.chaicode.com/youtube/chai-aur-sql/welcome/",
        "https://docs.chaicode.com/youtube/getting-started/"
    ]
