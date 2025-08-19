def http_error(status):
    #it is similar to switch case in other languages
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # _ is a comodin for else
        case _:
            return "Something's wrong with the internet"