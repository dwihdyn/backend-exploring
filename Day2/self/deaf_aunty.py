init_auntie = ''
end_auntie = str('bYe')

# while True:
#     init_auntie = input('say something to auntie : ')
#     if init_auntie == init_auntie.upper():
#         print('WHY YOU SCREAMING')
#     elif init_auntie == init_auntie.lower():
#         print('speak up or square up')
#     elif init_auntie == init_auntie.title():
#         print('cant hear u, anyway, when u getting married ?')
#     elif init_auntie == end_auntie:
#         print('k bye')
#         print('u there ?')
#         first_ignore = input('say something to auntie : ')
#         if first_ignore == '':
#             second_ignore = input('pls say something : ')
#             if second_ignore == '':
#                 print('bitch left me hanging')
#                 break


def leaving():
    ign = 0


while True:
    init_auntie = input('say something to auntie : ')
    if init_auntie == init_auntie.upper():
        print('WHY YOU SCREAMING')
    elif init_auntie == init_auntie.lower():
        print('speak up or square up')
    elif init_auntie == init_auntie.title():
        print('keke')
    elif init_auntie == end_auntie:
        print('k bye')
        print('u there ?')

        # ign = 0
        # while ign < 2:
        #     init_auntie = input('say something to auntie : ')
        #     if init_auntie == '':
        #         ign = ign + 1
        # print('left me hanging')
        # break

        first_ignore = input('say something to auntie : ')
        if first_ignore == '':
            second_ignore = input('pls say something : ')
            if second_ignore == '':
                print('bitch left me hanging')
                break
