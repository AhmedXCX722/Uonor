import random
import requests
from colorama import Fore, init, Style
import time

# دالة للتأكد من توفر اليوزرfrom colorama import Fore, Style, init

# Initialize colorama
init()

# Print the text in yellow
print(Fore.YELLOW + """
                      _    _                        
                     | |  | |                       
                     | |  | | ___  _ __   ___  _ __ 
                     | |  | |/ _ \| '_ \ / _ \| '__|
                     | |__| | (_) | | | | (_) | |   
                      \____/ \___/|_| |_|\___/|_|   

""" + Fore.RESET)

line = r""" ============================================================================ """

print(line)

# ANSI escape code for blue
blue = '\033[34m'
reset = '\033[0m'

# Print the text in blue
print(blue + """
[---]               The 3/4 User Scanner (Uonse)             [---]
[---]                Created by: AKA_Sla7er (AKA)               [---]
[---]                      Version: 1.0.0                       [---]
[---]          Homepage: https://github.com/AhmedXCX722/Uonor    [---]
                Welcome to the 3/4 User Scanner Tool (Uonse)
""" + reset)

def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    # إذا كان موجود، غير متاح
    if response.status_code == 200:
        return False
    # إذا كان 404، متاح
    elif response.status_code == 404:
        return True
    else:
        return None

# توليد يوزرات عشوائية
def generate_username(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

# طباعة النتائج بالألوان
def print_result(username, available):
    if available:
        print(Fore.GREEN + f"{username} ✔" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"{username} X" + Style.RESET_ALL)

# الأداة الرئيسية
def run_tool():
    total_usernames = 1000  # عدد اليوزرات المراد توليدها
    username_length_options = [3, 4]  # يمكن اختيار يوزرات من 3 أو 4 أحرف

    for _ in range(total_usernames):
        length = random.choice(username_length_options)
        username = generate_username(length)
        available = check_username_availability(username)
        
        # تجنب الحظر بانتظار وقت بين الطلبات
        time.sleep(1)

        if available is None:
            print(f"⚠ حدث خطأ أثناء محاولة التحقق من {username}!")
        else:
            print_result(username, available)

# تشغيل البرنامج
run_tool()
