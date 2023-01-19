import subprocess

def networks():
    data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
    profiles = [i.split(':')[1].strip() for i in data if "All User Profile" in i]
    print(f'Profiles: {profiles}\n{"-"*60}\n')
    
    for profile in profiles:
        
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('cp866').split('\n')
        
        try:
            passwords = [i.split(':')[1].strip() for i in profile_info if "Key Content" in i][0]
        except IndexError:
            passwords = None
        except:
            passwords = None
            
        print(f'Profile: {profile}\nPassword: {passwords}\n{"-"*60}')
        
networks()
