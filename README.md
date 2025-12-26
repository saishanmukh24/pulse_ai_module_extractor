### Pulse – Module Extraction AI Agent

## Overview
This is an AI tool that digs through help and documentation sites, picks out modules and submodules, and builds a structured map of how everything fits together. It doesnott guess everything comes straight from the actual website content.

The agent crawls documentation, figures out the site’s organization, filters out clutter, merges duplicate info and spits out a clean JSON file showing all the product’s modules and what they do.

Problem Statement:-
Modern SaaS products have huge and messy documentation sites. Trying to map out all the different modules and how they are connected by hand is slow and easy to mess up.

This repository solves by automatically reading documentation sites to:
- Find key modules
- Group related submodules together
- Write out clear descriptions using only what’s there—no outside info, no hallucinations

## Solution Summary
This works in a pipeline:-
1. You give it documentation URLs
2. It crawls every internal page it finds
3. Cleans up and normalizes the HTML
4. Follows the heading structure to spot modules and submodules
5. Deduplicates repeated modules
6. Outputs a tidy JSON file

No magic, No hallucinated content, Just what’s on the page.

## Features
- Works with one or many documentation URLs
- Recursively crawls all internal pages
- Strips headers, footers, nav bars, scripts—keeps only the good stuff
- Preserves heading structure to keep things organized
- Automatically finds modules and submodules
- Merges duplicates
- Filters out steps, error codes, and other non-structural sections
- Outputs structured JSON
- Runs from the command line

## Project Structure

pulse_ai_module_extractor/
|
|-- core/
|   |-- url_validator.py
|   |-- site_crawler.py
|   |-- html_cleaner.py
|   |-- module_builder.py
|
|-- main_runner.py
|-- requirements.txt
|-- outputs/
|   |-- extracted_modules.json
|-- README.md

## Tech Stack
- Python 3.14
- requests
- beautifulsoup4
- validators
- lxml

## Setup Instructions

1. pip install -r requirements.txt
2. Activate your virtual environment:
   venv\Scripts\activate
   (You’ll know you’re in the right place when you see (venv) in your terminal.)
3. Run:
   python main_runner.py --urls <source-URL>
4. Check your results in outputs/extracted_modules.json

## System Design

                User Input (URLs)
                      |
                URL Validation
                      |
                Recursive Crawling
                      |
                HTML Sanitization
                      |
                Semantic Section Extraction
                      |
                Module/Submodule Identification
                      |
                Deduplication Logic
                      |
                JSON Serialization

## Design Decisions

Heading-Based Inference:-
Page headings (h1, h2, h3) as the road signs for modules and submodules. This way, you always know exactly where the info came from.

Rule-Based Extraction:-
No guessing. Just a set of clear, predictable rules, so you can always audit what the agent found and why.

Deduplication Strategy:-
If a module pops up in different places, the system gathers all its unique submodules and combines them under one roof.

## Assumptions

- Headings in the docs actually represent the product’s structure
- Internal links always point to the same product context
- The docs themselves are the single source of truth
- Only HTML docs are supported for now

## Case Handling

| Scenario                   | Handling Strategy             |
| ---------------------------| ------------------------------|
| Broken links               | Skipped                       |
| Redirects                  | Followed automatically        |
| Duplicate pages            | Ignored (using a visited set) |
| Repeated modules           | Merged                        |
| Step-by-step headings      | Excluded                      |
| Error-code sections        | Excluded                      |
| Empty sections             | Ignored                       |

## Known Limitations

- Doesnot work with JavaScript rendered docs
- If modules are deeply nested, it may flatten them a bit
- Instruction heavy sections can lead to long descriptions
- No confidence scoring yet

## Validation & Testing
The tool has gone through its paces on several real-world documentation sites:
1. https://support.neo.space/hc/en-us
2. https://wordpress.org/documentation/
3. https://help.zluri.com/
4. https://www.chargebee.com/docs/2.0/



## Demo:-  https://drive.google.com/file/d/1gBtNonvQWE8-UEKPdCBuVffNMlXSjI5C/view?usp=sharing

Check out a quick video—just five minutes tops. Here’s what you’ll see:

- How everything fits together
- Running the program from the command line
- How the crawler works
- What the output looks like

## Environment Notes

This repository was built and tested with Python 3.14.
If you have multiple Python versions, make sure you install dependencies for the same version you run the program with.

## Conclusion

This project turns sprawling documentation sites into clean, structured knowledge fast. The modular setup means you can easily plug it into other tools, build a UI, or use it for analytics.

## Author

Vechalapu S Kanaka Santoshi Sai Shanmukh
