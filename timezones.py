from datetime import datetime, timedelta

GEO_WEEK_DAYS = {
    "Monday": "ორშაბათი",
    "Tuesday": "სამშაბათი",
    "Wednesday": "ოთხშაბათი",
    "Thursday": "ხუთშაბათი",
    "Friday": "პარასკევი",
    "Saturday": "შაბათი",
    "Sunday" : "კვირა",
}

RU_WEEK_DAYS = {
    "Monday": "понедельник",
    "Tuesday": "вторник",
    "Wednesday": "среда",
    "Thursday": "четверг",
    "Friday": "пятница",
    "Saturday": "суббота",
    "Sunday" : "воскресенье",
}

LANGUAGES = {
    "ქ" : "ქართული",
    "ი": "ინგლისური",
    "რ": "რუსული",
}

def validate_input():

    while True:
        try:
            print("ფორმატი -> 23/11/2012 12:02\n")
            date_time = input("შეიყვანეთ ფორმატის მიხედვით თარიღი/დრო: ")

            if date_time == "":
                print(datetime.today().strftime("%d/%m/%Y %H:%M"))
                return datetime.today()

            input_time = datetime.strptime(f"{date_time}", "%d/%m/%Y %H:%M")
            return input_time
        except:
            print("თქვენს მიერ შეყვანილი ფორმატი არასწორია, სცადეთ თავიდან")
        
def ask_for_language():
    language = input("\nშეიყვანეთ ენა (ქართული/ქ, რუსული/რ, ინგლისური/ი): ")
    if language == "ქ" or language == '' or language == 'ქართული':
        language = "ქ"
        print("თქვენს მიერ არჩეული ენაა - ქართული\n")
        return language
    elif language == "რ" or language == "რუსული":
        language = "რ"
        print("თქვენს მიერ არჩეული ენაა - რუსული\n")
        return language
    elif language == "ი" or language == "ინგლისური":
        language = "ი"
        print("თქვენს მიერ არჩეული ენაა - ინგლისური\n")
        return language
    print("ეს ენა ჩვენს პროგრამაში არ შედის, დაელოდეთ განახლებას...")
    exit()
        
def get_translated_weekday(input_time, language: str):

    weekday = input_time.strftime('%A')
    if language == "ქ":
        return GEO_WEEK_DAYS[weekday]
    elif language == "რ":
        return RU_WEEK_DAYS[weekday]
    else:
        return weekday
        
def ask_for_datetime():
    input_time = validate_input()
    input_language = ask_for_language()

    week_day = get_translated_weekday(input_time, input_language)

    translated_datetime = f"{input_time} {week_day}"
    return input_time, input_language

def prettify_datetimes(cc: list, language: str):
    for c in cc:
        dt = c["datetime"]
        week_day = get_translated_weekday(dt, language)

        try:
            formated_dt = dt.strftime("%d/%m/%Y %H:%M")
            c["datetime"] = f'{formated_dt} {week_day}'
        except Exception as e:
            print(e)
    return cc


def cc_datetimes(input_time):
    new_york = input_time - timedelta(hours = 8)
    london = input_time - timedelta(hours = 3)
    tokyo = input_time + timedelta(hours = 5)
    brasilia = input_time - timedelta(hours = 7)
    beijing = input_time + timedelta(hours = 4)
    canberra = input_time + timedelta(hours = 6)
    antarctica = input_time + timedelta(hours = 8)

    return [
        {"country": "ნიუ-იორკი", "datetime": new_york},
        {"country": "ლონდონი", "datetime": london},
        {"country": "ტოკიო", "datetime": tokyo},
        {"country": "ბრაზილია", "datetime": brasilia},
        {"country": "ბეიჯინგი", "datetime": beijing},
        {"country": "კანბერა", "datetime": canberra},
        {"country": "ანტარქტიდა", "datetime": antarctica},
    ]

def display_datetimes(cc:list):
    for c in cc:
        country = c["country"]
        dt = c["datetime"]
        print(f'{country} -> {dt}')
    
if __name__ == '__main__':
    input_time, input_language = ask_for_datetime()
    cc = cc_datetimes(input_time)
    pretty_cc = prettify_datetimes(cc, input_language)

    display_datetimes(pretty_cc)
