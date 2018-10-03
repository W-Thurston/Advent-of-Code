from hashlib import md5

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

secret_key = "yzbqklnj"
key_num = 1

full_key = secret_key + str(key_num)

answer = make_md5(full_key)

while answer[:5] != '00000':
    key_num += 1
    
    full_key = secret_key + str(key_num)

    answer = make_md5(full_key)
    
    if answer[:5] == '00000':
        print(key_num)
        print(answer)
        
        
while answer[:6] != '000000':
    key_num += 1
    
    full_key = secret_key + str(key_num)

    answer = make_md5(full_key)
    
    if answer[:6] == '000000':
        print(key_num)
        print(answer)