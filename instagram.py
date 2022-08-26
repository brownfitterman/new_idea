from instagrapi import Client
import json



def write_file(data, filename):
    fh = open(filename, "w")
    print("oppen file")
    try:
        fh.write(json.dumps(data))
    finally:
        fh.close()
        

def read_file(filename):
    fh= open(filename, "r")
    return json.load(fh)



ACCOUNT_USERNAME = 'dlovej009'
ACCOUNT_PASSWORD = '12345678999'

IG_CREDENTIAL = ACCOUNT_USERNAME
# # IG_CREDENTIAL = random.choice(ACCOUNT_USERNAMES)
print(IG_CREDENTIAL)
cl = None

try:
    cl = Client(read_file(IG_CREDENTIAL))
    print("valid credentials.json")

except:
    print("invalid credentials.json")

    cl = Client()
    print('done')
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    print(cl)
    


