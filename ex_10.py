first_num = input('input first number:')
if first_num.isnumeric():
    length_f_of_num=len(first_num)
    if 1 <= length_f_of_num <= 6:
        first_num=int(first_num)
        temp_num=first_num
        #
        second_num= input('input second number: ')
        if second_num.isnumeric():
            length_s_of_num=len(second_num)
            if 1 <= second_num <= 6:
                second_num=int(second_num)
                #
                for s_num in range(1, length_s_of_num+1):
                    remainder_of_2_div=second_num%10
                    div_zero_2=second_num//10
                    second_num=div_zero_2
                    for f_num in range(1, length_f_of_num+1):
                        remainder_of_1_div=first_num%10
                        div_zero_1=first_num//10
                        first_num=div_zero_1
                        if remainder_of_2_div == remainder_of_1_div:
                         print(f'Number {remainder_of_1_div} located of {f_num} position')
                        elif  div_zero_1 == 0:
                            first_num=temp_num
            else:
                print('You can input digital from 1 to 999 999')
        else:
            print('Second field accept only digital')
    else:
        print('You can input digital from 1 to 999 999')
else:
    print('First field accept only digital')