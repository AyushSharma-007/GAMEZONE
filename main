pip install pyrebase4
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "assignment-efe1b-default-rtdb.firebaseapp.com",
  "databaseURL": "https://assignment-efe1b-default-rtdb.firebaseio.com/",
  "storageBucket": "assignment-efe1b-default-rtdb.appspot.com"
}
db = firebase.database()
db.child("users").child("Morty")
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
firebase = pyrebase.initialize_app(config)
// used to insert the database in it 
def passwordcheck(password):
    while True:
        specChar = '!@#$%^&*_-+=<>'
        ac = uc = lc = dc = sc = 0
        strength = 0
        if len(password)>=8:
            for char in password:
                if char.isalpha():
                    ac += 1
                    if char.isupper(): uc += 1
                    else             : lc += 1
                elif char.isdigit()  : dc += 1
                elif char in specChar: sc += 1
        
            if ac > 0 and dc > 0     : strength += 1
            else                     : print('Combination of alpha and digit is a must')
            
            if uc > 0 and lc > 0     : strength += 1 
            else                     : print('Combination of alpha and digit is a must')
            
            if sc > 0                : strength += 1
            else                     : print('Special Character is a must')
            
            if strength == 3:
                print('password is strong')
                return password
            else:
                e = 1
        else:
            print('password should be atleast 8 characters')
            e = 1
        
        if e == 1:
                # password = passSuggest()
                # print(f'''Password not strong. Suggested password is {password}
                #     press 0 to Exit
                #     or''')
                password = input('please enter a strong password again:')
                if password == '0': return 0  
