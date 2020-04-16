# Translator Text API v3.0
https://docs.microsoft.com/ko-kr/azure/cognitive-services/translator/reference/v3-0-reference#authentication


python script

실행방법

아래 명령으로 소스코드 로컬로 복제

```
git clone https://github.com/dotnetpower/Translator.git
```

https://portal.azure.com 에서 Translator Cognitive services 생성후 Key 복사하여 Translator.py 의 key 에 붙여넣고

```
cd Translator

pip install  requests, json, logging, sys, uuid

Python.exe Translator.py "test_ko.txt", "en"
```

