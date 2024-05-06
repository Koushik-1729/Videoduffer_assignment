import requests
from bs4 import BeautifulSoup
def scrape_all_product_names(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")
        product_names = [li.find(class_="ai_link new_tab").text.strip() for li in soup.find_all("li", class_="li m")]
        return product_names
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return []

def save_file(product_names, filename):
    with open(filename, "w") as file:
        for name in product_names:
            file.write(name + "\n")

if __name__ == "__main__":
    url = "https://theresanaiforthat.com/"
    product_names = scrape_all_product_names(url)
    if product_names:
        for name in product_names:
            print(name)
        save_file(product_names, "product_names.txt")
        # print("Product names saved to product_names.txt")
    else:
        print("No product names extracted.")
