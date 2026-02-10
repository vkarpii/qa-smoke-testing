from core.utils import click_all_elements
from core.utils import go_to_page

async def test_home_page_console_errors(page, config):
    console_errors = []
    page.on("pageerror", lambda e: console_errors.append(str(e)))
    
    await go_to_page(page, f"{config['base_url']}/")

    if len(console_errors) > 0:
        raise AssertionError(f"JS console errors detected on /: {console_errors}")

async def test_home_page_clicks(page, config):
    await go_to_page(page, f"{config['base_url']}/")
    await click_all_elements(page)
    
async def test_home_page_response(page, config):
    response = await go_to_page(page, f"{config['base_url']}/")
    if response.status != 200: raise AssertionError("/ page did not return 200")
    
async def test_home_page_nav(page, config):
    await go_to_page(page, f"{config['base_url']}/")
    nav = await page.wait_for_selector("nav", timeout = config["timeout"])
    if not await nav.is_visible(): raise AssertionError("Nav not visible on /")

async def test_home_page_interactive(page, config):
    await go_to_page(page, f"{config['base_url']}/")
    interactive = await page.wait_for_selector("button, a", timeout = config["timeout"])
    if not await interactive.is_enabled(): raise AssertionError("Interactive element not clickable on /")
    

