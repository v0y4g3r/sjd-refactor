import hashlib


def encode(str):
    """
        Encode user input password using rules inherit from legacy code
        :arg str input password
        :return encrypted password
    """
    res = hashlib.md5(str.encode()).hexdigest()
    return res[8:24]


if __name__ == '__main__':
    print(encode('123456'))