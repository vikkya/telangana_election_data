import requests

def get_pdf(**params):
    partNumber = params["partNumber"]
    districtName = params["districtName"]
    acname = params["acname"]
    acnameeng = params["acnameeng"]
    acnameurdu = params["acnameurdu"]
    acno = params["acno"]
    districtText = params["districtText"]
    cname = params["cname"]
    cookies = {
        'ASP.NET_SessionId': "lpmtbvoyyveaqa2somb5we2k",
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'ASP.NET_SessionId=fvbtkoqojwrkh10kce43qvlo',
        'Origin': 'https://ceotserms2.telangana.gov.in',
        'Referer': f'https://ceotserms2.telangana.gov.in/ts_erolls/Popuppage.aspx?partNumber={partNumber}&roll=EnglishMotherRoll&districtName={districtName}&acname={acname}&acnameeng={acnameeng}&acno={acno}&acnameurdu={acnameurdu}',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'partNumber': partNumber,
        'roll': 'EnglishMotherRoll',
        'districtName': districtName,
        'acname': acname,
        'acnameeng': acnameeng,
        'acno': acno,
        'acnameurdu': acnameurdu,
    }

    data = {
        '__VIEWSTATE': 'XbfK9ioSFynqZsFYjF5jM07EIzq294PsQBdjSIABvEBdHCD4Yttk31AHgxGOudYtxZuyep0nKjKnIJkDgjnZ/qmu5lmTj8S1AZ7tsfyDT4PyBXUAUbhdHUgRfOO2tHfZFVLaiA==',
        '__VIEWSTATEGENERATOR': '4016BEDE',
        '__EVENTVALIDATION': 'r30xkWTXopJVI8WTUVDdipOzd8E8ws5OZ3S8FEt8VDP7I2RktiXfV/HEG7KeibZtBRJkd0+yvVrnNF+lNHwqvFnhcj0rbWPy9aVdJNcHQ5VfA6avMijspQjTUEBEuAAgIdN+cbat0o4ATyynDkCBkbc9tYQwFEz3YmDRzUQF0g4o19j0',
        'txtVerificationCode': '7941',
        'btnSubmit': 'Submit',
    }
    response = requests.post('https://ceotserms2.telangana.gov.in/ts_erolls/Popuppage.aspx', params=params, cookies=cookies, headers=headers, data=data)

    with open(f"pdfs/{districtText}_{cname}_{partNumber}.pdf", "wb") as out:
        out.write(response.content)