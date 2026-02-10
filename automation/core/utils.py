
import asyncio
from playwright.async_api import async_playwright

async def click_all_elements(page):
    buttons = await page.query_selector_all("button")
    for btn in buttons:
        text = await btn.evaluate("el => el.innerText") or ""
        try:
            await btn.click()
            await page.wait_for_load_state("networkidle")
        except Exception as e:
            raise AssertionError(f"Button not clickable: '{text}', reason: {e}")

    links = await page.query_selector_all("a")
    for link in links:
        text = await link.evaluate("el => el.innerText") or ""
        href = await link.evaluate("el => el.href") or ""
        try:
            response = await page.request.get(href)
            if response.status != 200:
                raise AssertionError(f"Broken link: '{text}' -> {href}, status {response.status}")
        except Exception as e:
            raise AssertionError(f"Link check failed: '{text}' -> {href}, reason: {e}")
        
async def go_to_page(page, url, wait_until="networkidle"):
    response = await page.goto(url)
    await page.wait_for_load_state(wait_until)
    return response

