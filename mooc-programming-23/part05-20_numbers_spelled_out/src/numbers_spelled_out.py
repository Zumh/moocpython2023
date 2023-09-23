# Write your solution here
def dict_of_numbers()->dict:
    numbers = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    all_dict_numbers = {}
    for key in range(0,100):
        
        if key < 20:
            all_dict_numbers[key] = numbers[key]
        elif key < 100:
            if key%10 == 0:
                all_dict_numbers[key] = numbers[key]
            else:
                all_dict_numbers[key] = numbers[(key//10)*10]+ "-" + numbers[key%10]
    return all_dict_numbers