## Part 1
import re
def secure_container(l_b, u_b):
    password_count = 0
    for i in range(l_b,u_b):
        num_to_lis = [x for x in str(i)]
        if num_to_lis == sorted(num_to_lis):

            ## Part 1
            # result = re.search(r'(\d)\1+', str(i))
            # if result != None:
            #     password_count +=1

            ## Part 2
            resulta = re.findall(r'(\d)\1+',str(i))
            if resulta != None:
                flag = False
                for x in resulta:
                    if num_to_lis.count(x) == 2:
                        flag=True
                if flag:
                    password_count += 1
    print(password_count)



if __name__ == '__main__':
    lower_bound = 130254
    upper_bound = 678275
    secure_container(lower_bound,upper_bound)


