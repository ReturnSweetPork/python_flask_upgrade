from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker



app = Flask(__name__)


@app.route('/lotto')
def lotto():
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    print(lotto_dict["drwNoDate"])
    week_num = []
    week_format_num = []
    bonus = lotto_dict["bnusNo"]
    drwtNo = ["drwtNo1", "drwtNo2", "drwtNo3", "drwtNo4", "drwtNo5", "drwtNo6"]

    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number)
        print(week_num)
        
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        
            
        
#num1 = lotto_dict["drwtNo1"]
#num2 = lotto_dict["drwtNo2"]
#num3 = lotto_dict["drwtNo3"]
#num4 = lotto_dict["drwtNo4"]
#num5 = lotto_dict["drwtNo5"]
#num6 = lotto_dict["drwtNo6"]
#bonum = lotto_dict["bnusNo"]
    
    
#print(lotto_dict["drwNoDate"])
#print(num1)
#print(num2)
#print(num3)
#print(num4)
#print(num5)
#print(num6)
#print(bonum)

    #pick = 우리가 생성한 번호
    #week_num = 이번주 당첨번호
    ##### 위의 두 값을 비교해서 로또 당첨 등수 출력!!!!!
    
    
    
    #print(type(res))
    #print(type(json.loads(res)))

    


    num_list = range(1,46)
    pick = random.sample(num_list, 6)
    pick.sort()
    
    
    lucky = 0
    for i in pick:
        if i in week_num:  
            lucky=lucky+1
            
            
    if lucky == 6:
        luck = "1등 입니다"
        
    elif lucky == 5:
        if bonus in pick:
            luck = "2등 입니다."
        else:
            luck = "3등 입니다."

    elif lucky == 4:
        luck = "4등 입니다."
        
    elif lucky == 3:
        luck = "5등 입니다."
    
    else:
        luck = "꽝입니다"
        
        
        
            
    
    #return  render_template("lotto.html", lotto=pick, num1=num1, num2=num2,  num3=num3,  num4=num4,  num5=num5, num6=num6,  bonum=bonum)
    return render_template("lotto.html",lotto=pick, week_num=week_num, week_format_num=week_format_num, luck=luck)
    
    
@app.route('/lottery')
def lottery():
    # 로또 정보를 가져온다
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    # 1등 당첨 번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
    
    # 보너스 번호를 bonus 변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    # 임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    pick = [2, 25, 28, 30, 33, 6]
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    else:
        text = "꽝"
    
    # 사용자에게 데이터를 넘겨준다.
    
    return render_template("lottery.html",pick=pick, week=week,text=text)
    
    
    
    


@app.route('/ping')
def ping():
    return render_template("ping.html")
    
    
    
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()
    #request 임. requests와 차이 기억!!!
    
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)
    
    
    
@app.route('/input')
def input():
    return render_template("input.html")
    
    
    
    
@app.route('/output')
def output():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_profile = fake.profile()
    #request 임. requests와 차이 기억!!!
    
    return render_template("output.html", html_name=input_name, fake_profile=fake_profile)



    

          
    
  