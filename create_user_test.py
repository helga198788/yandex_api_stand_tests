import sender_stand_request
import data
def newuser():
        user_body = data.user_body.copy()
        response = sender_stand_request.post_new_user(user_body)
        return response

#token = newuser().json()["authToken"]
#print(token)

def newkit(kit_body):
        #kit_body = data.kit_body.copy()
        response = sender_stand_request.post_new_kit(kit_body)
        return response

kit1 = newkit({"name":"a"})
print(kit1.status_code,"<--- kit1")
assert kit1.status_code == 201

kit2= newkit({"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})
print(kit2.status_code,"<--- kit2")
assert kit2.status_code == 201

kit10 = newkit({})
print(kit10.status_code,"<--- kit10")
assert kit10.status_code == 400
