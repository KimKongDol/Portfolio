from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
import random
from nltk.corpus import words #영어단어가 맞는지 확인하는 모듈
from nltk.tokenize import word_tokenize #문장을 토큰으로 쪼개기 위한 모듈
from nltk.stem import WordNetLemmatizer #복수명사를 단수로 바꿔주기 위한 모듈

#########################################
def gallery_index(request):
    return render(request, 'gallery.html')

def christmas(request):
    return render(request, 'christmas.html')

def caesar(request):
    return render(request, 'caesar.html')
#######################################

#ascii로 바꿈
ascii_sentence=[]
#카이사르 암호를 쓴 문장의 아스키
cearsar_ascii =[]
#카이사르 암호문
cearsar_sentence=""

# final_sentence = ""

def test(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('title'))
    return JsonResponse(jsonObject)


def input_string(request):
    jsonObject = json.loads(request.body)
    sentence = jsonObject.get('ajax_string_input')
    cearsar_sentence = caesar_encryp(sentence)

     #몇번 쉬프트했는지 모르는 상황에서 시프트 횟수 찾기
    shift_num = AA()

    jsonObject['cearsar_sentence']= cearsar_sentence
    jsonObject['shift_num']= shift_num
    return JsonResponse(jsonObject)

def random_string(request):
    rand = random.randint(7,10)
    sentence = " ".join(random.sample(words.words(),rand))
    cearsar_sentence = caesar_encryp(sentence)
    print("뽑은 수",rand,"원문:",sentence)

    #몇번 쉬프트했는지 모르는 상황에서 시프트 횟수 찾기
    shift_num = AA()

    jsonObject = {
        'rand_string':sentence, 
        'cearsar_sentence':cearsar_sentence, 
        'shift_num':shift_num,
        }
    return JsonResponse(jsonObject)
    

def AA():
    decryp_sentence_token =[]
    shift_num=4
    for shift in range (1,27):
        cnt = 0
        print("shiftttt::::::::::",caesar_decryp(shift))
        decryp_sentence_token = word_tokenize(caesar_decryp(shift))
        for token in decryp_sentence_token:
            #동사를 동사원형으로
            token = WordNetLemmatizer().lemmatize(token.lower(),pos='v')
            #동사를 단수형
            token = WordNetLemmatizer().lemmatize(token, pos='n')
            #토큰이 알파벳이면서 사전에 있는 영어가 맞을 때
            if(token.isalpha() and token in words.words()):
                cnt+=1
            #토큰이 그 외 문자일 땐 패스
            elif(not token.isalpha()):
                cnt+=1
            #토큰이 알파벳이면서 사전에 없으면 break
            else:
                break;
        
        if (cnt == len(decryp_sentence_token)):
            print(f"{shift}번 시프트했네요.")
            shift_num = shift
            break
    return shift_num



def caesar_encryp(sentence):
    global cearsar_ascii 

    #카이사르 쉬프트 횟수
    caesar_shift = random.randint(1,26)   
    #카이사르 암호문
    cearsar_sentence=""
    #임의문장char로 쪼갬
    sentence_char_list = list(sentence)
    for j in sentence_char_list:
        ascii_cha = ord(j) #char로 쪼갠 원문을 아스키로 변환
        #대문자일때, 소문자일때, 그 외 특수문자일때로 나눔
        if(ascii_cha>64 and ascii_cha<91):
            # print(chr(ascii_cha),"는 대문자")
            ascii_cha = ascii_cha+caesar_shift #카이사르 쉬프트만큼 돌림
            if(ascii_cha>90):
                ascii_cha = ascii_cha-26
        if(ascii_cha>96 and ascii_cha<123):
            # print(chr(ascii_cha),"는 소문자")
            ascii_cha = ascii_cha+caesar_shift #카이사르 쉬프트만큼 돌림
            if(ascii_cha>122):
                ascii_cha = ascii_cha-26
        cearsar_ascii.append(ascii_cha)
        cearsar_sentence += chr(ascii_cha)

        print("암호문: ", cearsar_sentence)
    return cearsar_sentence


#shift수를 넣으면 해독문을 뱉어줌
def caesar_decryp(shift):
    #해독한 문장
    decryp_sentence=""
    for ascii_cha in cearsar_ascii:
        #대문자일때, 소문자일때, 그 외 특수문자일때로 나눔
        if(ascii_cha>64 and ascii_cha<91):
            # print(chr(ascii_cha),"는 대문자")
            ascii_cha = ascii_cha-shift #카이사르 쉬프트만큼 돌림
            if(ascii_cha<65): ascii_cha = ascii_cha+26
        if(ascii_cha>96 and ascii_cha<123):
            # print(chr(ascii_cha),"는 소문자")
            ascii_cha = ascii_cha-shift #카이사르 쉬프트만큼 돌림
            if(ascii_cha<97):ascii_cha = ascii_cha+26
        decryp_sentence += chr(ascii_cha)
    return decryp_sentence