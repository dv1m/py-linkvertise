import random
import base64


def linkvertise(userID, url):
    url_bytes = url.encode('ascii')
    base64_bytes = base64.b64encode(url_bytes)
    base64_message = base64_bytes.decode('ascii')

    return str(f"https://link-to.net/{userID}/{str(random.randint(0, 10000000))}/dynamic?r={base64_message}")


print(linkvertise('111933', 'https://www.google.com'))