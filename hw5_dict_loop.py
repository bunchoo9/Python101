#โปรแกรมค้นหาคนที่มีรอบเอวเกิน 90 ซม

waist = {'aek':88,'nokia':61,'bunchoo':82,'yam':101,'may':91,'teng':99}

def waistNo(waist):
    for w in waist.items():
        if w[1] > 90:
            print(w[0], w[1])

waistNo(waist)

