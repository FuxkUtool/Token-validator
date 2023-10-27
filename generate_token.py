try:
    import datetime, random
    from colorama import Fore, init
    import string
    init(autoreset=True)

    green = Fore.GREEN
    red = Fore.RED
    blue = Fore.BLUE
    yellow = Fore.YELLOW

    print(f'''
        {green}FuxkUTOOLS
                    {red}coded by iampopg & himld
        ''')
# i put the in this format id ,token, date , true
    def generate():
        print(yellow + 'Do you want to generate Token?')
        print("yes/no")
        ans = input(': ')
        if ans.strip().lower() == 'yes':
            id = input("Please Enter the user_id: ")
            alphabet = string.ascii_letters.upper()
            numbers = '0123456789'
            length = 16
            token = ''.join(random.choice(alphabet + numbers) for _ in range(length))
            formatted_token = '-'.join([token[i:i+4] for i in range(0, len(token), 4)])
            print(blue + f'Generated Token: {green}{formatted_token}')
            with open('Create_Token.txt', 'a') as write:
                Full_Token = id + '|' + formatted_token+'|'+str(datetime.date.today())+'|'+ 'True'
                file = write.write(f'{Full_Token}\n')

            with open('Token.txt', 'a') as write:
                Main_Token = formatted_token
                file = write.write(f'{Main_Token}\n')
        else:
            print(blue + 'Thanks for the visit')
            
    generate()
except ModuleNotFoundError:
    import os, time
    print('you dont have colorama, about to install it now')
    time.sleep(1)
    os.system('pip install colorama')
    
except Exception as e:
    print(e)