#-*- coding:utf-8 -*-

import requests, json, logging, sys, uuid
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class TransaltorAPI:
    def __init__(self, endpoint, key, file, lang):
        self.uri = endpoint
        self.key = key
        self.file = file     
        self.lang = lang           
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.key, 
            'Content-Type': 'application/json; charset=UTF-8',
            'X-ClientTraceId': str(uuid.uuid4())
        }
       

    def Run(self):
        infile = open(self.file, 'r', encoding='UTF-8')
        outfile = open('result.tsv', 'w', encoding='UTF-8')

        lines = infile.readlines()
        for line in lines:
            line = line.replace('\n','')
            payload = [{'Text':line}]
            response = requests.post(f'{self.uri}{self.lang}', headers=self.headers, json=payload)
            translationtext = response.json()[0]['translations'][0]['text']
            logging.info(f'{line}, {translationtext}')
            outfile.write(f'{line}, {translationtext}\n')
        
        infile.close()
        outfile.close()
        logging.info('완료')

# 실행방법: 
# 실행 오류시 필요 라이브러리 설치명령> pip install requests, json, logging, sys, uuid
# Python.exe Translator.py "test_ko.txt", "en"
# Python.exe Translator.py "test_en.txt", "ko"
if __name__ == '__main__':
    file = sys.argv[1]
    lang = sys.argv[2]

    #테스트 하려면 아래 주석 해제
    #file = 'test_ko.txt'
    #lang = 'en'
    endpoint = f'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to='
    key = 'translator api key'

    translator = TransaltorAPI(endpoint, key, file, lang)
    translator.Run()

