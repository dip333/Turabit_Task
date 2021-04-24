import json, requests

def ocr_space_file(filename, overlay=True, api_key='5b1e8fc03088957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )

    # result = json.loads(r.content.decode())
    # parsedResults = result.get("ParsedResults")[0].get("TextOverlay")
    # print(parsedResults)

    result = json.loads(r.content.decode())
    parsedResults = result.get("ParsedResults")[0].get("TextOverlay").get("Lines")
    l = len([i for i in parsedResults if i['LineText']])
    print(l)

    for i in range(0,l):
        parsedResults = result.get("ParsedResults")[0]
        textDetected = parsedResults.get("TextOverlay").get("Lines")

    for i in textDetected:
        print(i)
        print()

    result = json.loads(r.content.decode())
    parsedResults = result.get("ParsedResults")[0]
    textDetected = parsedResults.get("ParsedText")
    print(textDetected)

def ocr_space_url(url, overlay=True, api_key='5b1e8fc03088957', language='eng'):

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    # result = json.loads(r.content.decode())
    # parsedResults = result.get("ParsedResults")[0].get("TextOverlay").get("Lines")
    # l = len([i for i in parsedResults if i['LineText']])
    # # print(l)
    #
    # for i in range(0, l):
    #     parsedResults = result.get("ParsedResults")[0]
    #     textDetected = parsedResults.get("TextOverlay").get("Lines")
    #
    # for i in textDetected:
    #     print(i)
    #     print()

    result = json.loads(r.content.decode())
    parsedResults = result.get("ParsedResults")[0]
    textDetected = parsedResults.get("ParsedText")
    print(textDetected)

test_file = ocr_space_file(filename='2-min.png', language='eng')

# test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')

# Arabic=ara
# Bulgarian=bul
# Chinese(Simplified)=chs
# Chinese(Traditional)=cht
# Croatian = hrv
# Czech = cze
# Danish = dan
# Dutch = dut
# English = eng
# Finnish = fin
# French = fre
# German = ger
# Greek = gre
# Hungarian = hun
# Korean = kor
# Italian = ita
# Japanese = jpn
# Polish = pol
# Portuguese = por
# Russian = rus
# Slovenian = slv
# Spanish = spa
# Swedish = swe
# Turkish = tur