def create_modules(sectioned_pages):
    module_map = {}

    for page in sectioned_pages:
        if not page:
            continue

        module_title = page[0]["title"].strip()
        module_desc = " ".join(page[0]["content"]).strip()

        if module_title not in module_map:
            module_map[module_title] = {
                "module": module_title,
                "Description": module_desc,
                "Submodules": {}
            }

        for subsection in page[1:]:
            if subsection["content"]:
                sub_title = subsection["title"].strip()
                sub_desc = " ".join(subsection["content"]).strip()

                #avoid overwritting  good content.
                if sub_title not in module_map[module_title]["Submodules"]:
                    module_map[module_title]["Submodules"][sub_title] = sub_desc

    return list(module_map.values())
