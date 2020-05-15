import requests


def get_page(token, code):
    r = requests.get('https://api.classtime.com/students-api/v2/sessions/'+code,
                     headers={'Authorization': token})
    return r.json()


def main():
    code = input('Код задания: ')
    token = input('JWT Токен: ')
    page = get_page(token, code)
    que = page['questions']
    for quen in range(len(que)):
        print(f'----------{str(quen+1)}----------')
        if que[quen]['categories'] == []:
            for answer in que[quen]['choices']:
                if answer['isCorrect'] is True:
                    answer = answer['content']['blocks'][0]['text']
                    print(que[quen]['title'])
                    print(answer)
        else:
            for item in que[quen]['items']:
                text = item['content']['blocks'][0]['text']
                categorie_id = item['categories'][0]
                for categorie in que[quen]['categories']:
                    if categorie['id'] == categorie_id:
                        print('['+text+']'+': '+categorie['content']
                              ['blocks'][0]['text'])


main()
