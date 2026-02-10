from core.utils import click_all_elements
from core.utils import go_to_page

async def test_about_page_console_errors(page, config):
    console_errors = []
    page.on("pageerror", lambda e: console_errors.append(str(e)))
    
    await go_to_page(page, f"{config['base_url']}/about")

    if len(console_errors) > 0:
        raise AssertionError(f"JS console errors detected on /about: {console_errors}")
    
async def test_about_page_clicks(page, config):
    await go_to_page(page, f"{config['base_url']}/about")
    await click_all_elements(page)

async def test_about_page_response(page, config):
    response = await go_to_page(page, f"{config['base_url']}/about")
    if response.status != 200: raise AssertionError("/about page did not return 200")
    
async def test_about_page_h1(page, config):
    await go_to_page(page, f"{config['base_url']}/about")
    header = await page.wait_for_selector("header", timeout = config["timeout"])
    if not await header.is_visible(): raise AssertionError("Header not visible on /about")
    
async def test_about_page_nav(page, config):
    await go_to_page(page, f"{config['base_url']}/about")
    nav = await page.wait_for_selector("nav", timeout = config["timeout"])
    if not await nav.is_visible(): raise AssertionError("Nav not visible on /about")
    
async def test_about_page_content(page, config):
    await go_to_page(page, f"{config['base_url']}/about")
    content = await page.wait_for_selector(".content", timeout = config["timeout"])
    if not await content.is_visible(): raise AssertionError("Content not visible on /about")

async def test_about_page_interactive(page, config):
    await go_to_page(page, f"{config['base_url']}/about")
    interactive = await page.wait_for_selector("button, form", timeout = config["timeout"])
    if not await interactive.is_enabled(): raise AssertionError("Interactive element not clickable on /about")
    