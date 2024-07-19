import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def fetch_gig_details(gig_url):
    # استبدل هذا التعليق بالكود الفعلي لجلب تفاصيل gig
    title = "عنوان مثال"
    description = "وصف مثال"
    tags = "علامة1, علامة2"
    return title, description, tags

def analyze_content(title, description, tags):
    keywords = []
    
    if "تصميم" in title:
        keywords.append("خدمات تصميم")
    if "SEO" in description:
        keywords.append("تحسين محركات البحث")
    if "إعلانات" in tags:
        keywords.append("إعلانات عبر الإنترنت")
    
    return ', '.join(keywords)

def update_gig_keywords(driver, gig_url, new_keywords):
    driver.get(gig_url)
    
    # تسجيل الدخول
    login(driver)

    # تعديل الكلمات المفتاحية
    tags_input = driver.find_element(By.CSS_SELECTOR, 'input.tags-input')  # استبدل CSS Selector بالعنصر الصحيح
    tags_input.clear()
    tags_input.send_keys(new_keywords)
    tags_input.send_keys(Keys.RETURN)
    
    # حفظ التعديلات
    save_button = driver.find_element(By.CSS_SELECTOR, 'button.save-button')  # استبدل CSS Selector بالعنصر الصحيح
    save_button.click()

def login(driver):
    username = os.getenv("FIVERR_USERNAME")
    password = os.getenv("FIVERR_PASSWORD")
    
    # عنوان URL لصفحة تسجيل الدخول
    login_url = "https://www.fiverr.com/login"
    driver.get(login_url)

    # إدخال بيانات تسجيل الدخول
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)

    # الضغط على زر تسجيل الدخول
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.login-button')
    login_button.click()

    # الانتظار حتى يتم تسجيل الدخول
    time.sleep(5)

def main():
    gig_url = 'https://www.fiverr.com/s/DB5P21X'  # استبدل بعنوان gig الخاص بك
    title, description, tags = fetch_gig_details(gig_url)
    recommendations = analyze_content(title, description, tags)

    print("توصيات تحسين SEO:")
    for rec in recommendations.split(', '):
        print(f"- {rec}")

    # تحديث الكلمات المفتاحية
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # تأكد من إعداد ChromeDriver بشكل صحيح
    update_gig_keywords(driver, gig_url, recommendations)
    driver.quit()

if __name__ == "__main__":
    main()
