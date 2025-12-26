import validators

def validate_url(url: str) -> bool:
    
    #checks whether a given string is a valid URL or not.
    
    return validators.url(url)
