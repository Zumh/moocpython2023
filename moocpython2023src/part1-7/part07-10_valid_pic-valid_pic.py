# Write your solution here

from datetime import datetime
def verify_date_format(pic:str, pic_date:str):

    # check if the date format is correct
    pic_date = pic[:len(pic_date)]
    day = int(pic_date[:2])
    month = int(pic_date[2:4])
    year = pic_date[4:] 

    if "+" in pic:
        year = "18" + year
    elif "-" in pic:
        year = "19" + year
    elif "A" in pic:
        year = "20" + year
    else:
        raise ValueError('wrong date format')
    year = int(year)
    
    # trying to convert to date time format
    # if it can't convert then raise and error that try block will catch in the main function or function it was call
    datetime(year,month,day)
def verify_control_char(pic:str):
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digits = int(pic[0:6] + pic[7:10])
    control_indx =  nine_digits % 31 
    last_control_pic_value = pic[-1]
    if control_chars[control_indx] != last_control_pic_value:
        raise ValueError("wrong control char")
def is_it_valid(pic: str)->bool:
    
    # check the date ddmmyy
    pic_date = "ddmmyy"
    control_char = "Xyyyz"
    valid_len = len(pic_date+control_char) 
    is_valid_pic = True 
    # check the length of the pic and it must be 
    if valid_len < len(pic):
        return False
    try:
        verify_date_format(pic, pic_date)
        verify_control_char(pic)

    except ValueError:
        is_valid_pic = False 
    
    return is_valid_pic
    