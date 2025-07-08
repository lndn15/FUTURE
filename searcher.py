import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

class SearchAnswer:
    @classmethod
    def run(cls):
        while True:
            print("(SearchAnswerFile)")
            print("\nДоступные команды: search, exit, help")
            command = input(">>> ").strip().lower()
            
            if command == "search":
                results = cls.mainwork()
                for item in results:
                    print(f"\n{item['title']}\n{item['url']}")
            elif command in ("exit", "quit"):
                break
            elif command == "help":
                print("Доступные команды: search - выполнить поиск, exit - выход")
            else:
                print("Неизвестная команда")

    @staticmethod
    def mainwork():
        max_results = 10
        secret_protocol = bool
        with sync_playwright() as p:    
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()
            query = str(input("Ваш запрос: "))

            page.goto("https://duckduckgo.com/", timeout=15000)

            page.wait_for_selector("input[name=q]", state="visible")
            page.fill("input[name=q]", query)
            page.press("input[name=q]", "Enter")

            page.wait_for_selector("[data-testid=result-title-a]", timeout=15000)
                
            results = []
            for result in page.locator("[data-testid=result]").all()[:max_results]:
                try:
                    title = result.locator("[data-testid=result-title-a]").first.text_content()
                    url = result.locator("a[data-testid=result-title-a]").first.get_attribute("href")
                    if title and url:
                        results.append({
                            "title": title.strip(),
                            "url": url
                        })
                    secret_protocol = True
                except Exception as e:
                    print(f"Ошибка обработки элемента: {e}")
                    secret_protocol = False

            
            browser.close()
            return results
