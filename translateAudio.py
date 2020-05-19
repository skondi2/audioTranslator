import requests
import json
import xmltodict


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def upload_file(filename, token):

    headers = {'authorization': "%s" % token}

    response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(filename))

    return get_url(response.json())


def submit_request(url, token):
    endpoint = "https://api.assemblyai.com/v2/transcript"

    json = {
        "audio_url": "%s" % url
    }

    headers = {
        "authorization": "%s" % token,
        "content-type": "application/json"
    }

    response = requests.post(endpoint, json=json, headers=headers)

    return get_id(response.json())


def check_status(id_p, token):
    endpoint = "https://api.assemblyai.com/v2/transcript/%s" % id_p

    headers = {
        "authorization": "%s" % token,
    }

    response = requests.get(endpoint, headers=headers)
    json_parsed = json.loads(json.dumps(response.json()))

    return json_parsed['status'], json_parsed['text']


def get_url(json_dict):
    json_parsed = json.loads(json.dumps(json_dict))
    return json_parsed['upload_url']


def get_id(json_dict):
    json_parsed = json.loads(json.dumps(json_dict))
    return json_parsed['id']


def translate():
    my_token = "02bad35b48984fbbb8d41e9c7c316c58"
    url = ""

    audio_option = input("Audio URL or Local file path? Enter 1 or 2. ")

    if str(audio_option) == "1":
        filepath = input("Enter local file path: ")
        url = upload_file(filepath, my_token)

    if str(audio_option) == "2":
        url = raw_input("Enter audio URL: ")
        url = str(url)

    lang = raw_input("Enter desired language code. Enter 'options' for possible langauge codes: ")

    if str(lang) == "options":
        lang = raw_input("Options: \nBasque: 'eu' \nWelsh: 'cy' \nDutch: 'nl' \nItalian: 'it'\nSpanish: 'es'\nGerman: 'de'\nFrench: 'fr'\n")

    # url = upload_file(filepath, my_token)
    # url = "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"

    submit_id = submit_request(url, my_token)

    status, text = check_status(submit_id, my_token)
    while status != "completed" and (status != "error"):
        status, text = check_status(submit_id, my_token)

    if status == "error":
        print("Error in transcribing")
        exit(1)

    # print(status)
    print("Original Text: " + text)

    endpoint_1 = "https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20200519T200302Z.d34cc59f3f11cfaf.f" \
                 "3ab7d2fe09da37afa4dc92ea3c42c3551a5a244&text={0}&lang=en-{1}&format=plain&options=1"\
                    .format(text, str(lang))

    response_1 = requests.get(endpoint_1)
    #print(response_1.text)

    xml_text = response_1.text
    if str(xml_text).find("Error code"):
        print("Error in translating")
        exit(1)

    my_dict = xmltodict.parse(xml_text)
    print(my_dict["Translation"]["text"])
    translated = "Translation: {0}".format(str(my_dict["Translation"]["text"]))
    print(translated)
    print("Powered by Yandex.Translate")


# main call:
translate()


