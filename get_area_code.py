import requests

city = input("Enter Location: ")

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://de.ra.co',
    'priority': 'u=1, i',
    'ra-content-language': 'de',
    'referer': f'https://de.ra.co/events/de/{city}',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Brave";v="129.0.0.0", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

data = f'{{"operationName":"GET_AREA_WITH_GUIDEIMAGEURL_QUERY","variables":{{"areaUrlName":"{city}","countryUrlCode":"de"}},"query":"query GET_AREA_WITH_GUIDEIMAGEURL_QUERY($id: ID, $areaUrlName: String, $countryUrlCode: String) {{\\n area(id: $id, areaUrlName: $areaUrlName, countryUrlCode: $countryUrlCode) {{\\n ...areaFields\\n guideImageUrl\\n __typename\\n }}\\n}}\\n\\nfragment areaFields on Area {{\\n id\\n name\\n urlName\\n ianaTimeZone\\n blurb\\n country {{\\n id\\n name\\n urlCode\\n requiresCookieConsent\\n currency {{\\n id\\n code\\n exponent\\n symbol\\n __typename\\n }}\\n __typename\\n }}\\n __typename\\n}}\\n"}}'

response = requests.post('https://de.ra.co/graphql', headers=headers, data=data).json()

print(response["data"]["area"]["id"])