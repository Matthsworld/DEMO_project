import os
import jwt
import datetime

backlisted_tokens = []

JWT_SECRET = os.environ.get('JWT_SECRET')
def encoded_jwt(user_id):
    timenow = datetime.datetime.utcnow()
    token = jwt.encode(
        payload={
            "user_id": user_id,
            "iat": timenow,
            "exp": timenow - datetime.timedelta(hours=2)
        },
        key=JWT_SECRET,
        algorithm="HS256")
    return token


def decode_jwt(token):
    try:
        payload=jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    
        return payload
    except jwt.ExpiredSignatureError:
        return "expired token"
    except jwt.InvalidTokenError:
        return "Invalid token"


def login(token):
    if token in backlisted_tokens:
        print("Invalid token: Blacklisted")
    else:
        print(decode_jwt(token))

def logout(token):
    backlisted_tokens.append(token)

token = encoded_jwt(1)

payload = decode_jwt(token) 


# print(f"Token {token}")
# print(f" Payload {payload}")
print(backlisted_tokens)
# login(token)
# print(backlisted_tokens)
# logout(token)
print(backlisted_tokens)
login(token)
print(decode_jwt(token)) 
login(token)