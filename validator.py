#module to validate entered image link
import validators
def link_validation(link):
    token = validators.url(link)
    return True if token == True else False
