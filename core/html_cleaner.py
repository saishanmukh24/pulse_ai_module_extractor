import re
from bs4 import BeautifulSoup

def is_valid_module_heading(text: str) -> bool:
    
    #filters all non-semantic headings like steps, errors, etc.

    invalid_patterns = [
        r"^step\s+\d+",
        r"^sla-\d+",
        r"error",
        r"troubleshooting",
    ]

    lowered = text.lower()
    return not any(re.search(p, lowered) for p in invalid_patterns)


def extract_sections(soup: BeautifulSoup):
    for tag in soup(["nav", "footer", "header", "aside", "script", "style"]):
        tag.decompose()

    sections = []
    active_section = None

    for element in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        if element.name in ["h1", "h2", "h3"]:
            title = element.get_text(strip=True)

            if not is_valid_module_heading(title):
                active_section = None
                continue

            active_section = {
                "title": title,
                "content": []
            }
            sections.append(active_section)

        elif active_section:
            text = element.get_text(strip=True)
            if text:
                active_section["content"].append(text)

    return sections
