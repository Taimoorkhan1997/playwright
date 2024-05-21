from playwright.sync_api import sync_playwright


email = "test.company1@yopmail.com"
password = "Test#123"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://uat.healthcaretalentlink.com/login')
    # page.w('#__next > div > div > main > div > div > div > form > span.w-100.h-16.flex.flex-col.items-center.relative.mb-1 > div > input"]')
    page.fill('//*[@id="__next"]/div/div/main/div/div/div/form/span[1]/div/input', email)
    page.fill('//*[@id="__next"]/div/div/main/div/div/divgit commit -m "first commit"/form/span[2]/div/input', password)


    page.click('input[type="submit"]')

