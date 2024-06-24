import re

def is_valid_UID(uid):
    if len(uid) != 10:
        return False
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    if len(re.findall(r'\d', uid)) < 3:
        return False
    
    if len(set(uid)) != 10 or not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False
    
    return True

t = int(input().strip())

for _ in range(t):
    uid = input().strip()
    if is_valid_UID(uid):
        print('Valid')
    else:
        print('Invalid')
