"""Suvarnabhumi Airport"""
def main(timezone_1, timezone_2, mytime):
    """Main PrePro"""
    meridiem = mytime[-2:]
    hour = int(mytime[0:2])
    minute = int(mytime[3:5])
    # ปรับ เวลาให้เป็น 24 and 12 ==> 0
    hour = hour + ((meridiem == "PM")*12) - (hour == 12)*12
    # เวลาการเดินทาง และ การเปลี่ยนแปลงGMT
    if timezone_2[-4:-1] == "SYD":
        hour += 9+3
    elif timezone_2[-4:-1] == "SGN":
        hour += 1
        minute += 50
    elif timezone_2[-4:-1] == "ATL":
        hour += 20-11
        minute += 55
    elif timezone_2[-4:-1] == "YVR":
        hour += 16-14
        minute += 20
    elif timezone_2[-4:-1] == "KTM":
        hour += 13-2
        minute = minute + 45

    # time จัดรูป
    if minute >= 60:
        hour += 1
        minute = minute%60
    if hour%24 < 12:
        meridiem = "AM"
        hour = hour%12
    else:
        meridiem = "PM"
        hour = hour%12
    if hour == 0:
        hour += 12

    print("%s - %s" %(timezone_1[-4:-1], timezone_2[-4:-1]))
    print("%02i:%02i %s" %(abs(hour), abs(minute), meridiem))
main(input(), input(), input())
