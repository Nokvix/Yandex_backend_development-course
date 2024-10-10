def obfuscator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        name = result['name']
        password = result['password']
        
        result = {
            'name': name[0] + len(name[1:-1]) * '*' + name[-1],
            'password': len(password) * '*'
        }

        return result

    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
