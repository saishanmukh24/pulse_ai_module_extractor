import argparse
import json
from core.url_validator import validate_url
from core.site_crawler import crawl_docs
from core.html_cleaner import extract_sections
from core.module_builder import create_modules

def run_extraction(urls):
    global_sections = []

    for url in urls:
        print(f"\nProcessing: {url}")
        pages = crawl_docs(url)

        for soup in pages.values():
            structured = extract_sections(soup)
            if structured:
                global_sections.append(structured)

    #build modules from all pages.
    final_modules = create_modules(global_sections)
    return final_modules


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pulse AI - Module Extraction Agent"
    )
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="One or more documentation URLs"
    )

    args = parser.parse_args()

    valid_urls = [u for u in args.urls if validate_url(u)]

    if not valid_urls:
        print("No valid URLs provided.")
        exit(1)

    output = run_extraction(valid_urls)

    output_file = "outputs/extracted_modules.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n Extraction completed. Output saved to {output_file}")
