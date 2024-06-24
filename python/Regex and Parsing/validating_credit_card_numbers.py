import re

N = int(input().strip())
pattern = r'^([456]\d{3})(-?\d{4}){3}$'

for _ in range(N):
    cc_number = input().strip()
    if re.match(pattern, cc_number):
        cc_number = cc_number.replace('-', '')
        is_valid = True
        for i in range(len(cc_number) - 3):
            if cc_number[i] == cc_number[i+1] == cc_number[i+2] == cc_number[i+3]:
                is_valid = False
                break
        
        if is_valid:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
