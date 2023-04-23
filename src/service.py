import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading
# connect by firebase admin
cred = credentials.Certificate('smartgreenhouse-a7809-firebase-adminsdk-ltfsz-6e6855dac0.json')
# Initialize the app with a service account, granting admin privileges
threading.Thread(target=firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartgreenhouse-a7809-default-rtdb.firebaseio.com/'
})).start()
def get_ref(key):
    return db.reference(key)
def get_temp():
    return get_ref('/Temperature').get()
def get_hum():
    return get_ref('/Humidity').get()
def get_soil():
    return get_ref('/Soil humidity').get()
def set_fb(part, bool):
    threading.Thread(target=get_ref('/').update({part: bool})).start()
# main buttons command
array =['None']
plants = get_ref('/Plants')
# Set default
# get_ref('/').set({
#'Humidity' : 0,
#'Soil humidity' : 0,
    #'Temperature' : 0,
#   'Plants': 'None',
#  'Heating': False,
# 'Cooling': False,
# 'Water': False,
# 'Ozon': False
# })

def button(function):
    if get_ref('/').get()[function]:
        threading.Thread(target=set_fb(function, False)).start()
    else:
        threading.Thread(target=set_fb(function, True)).start()



def add_array():
    for i in plants.get():
        threading.Thread(target=array.append(i)).start()


def auto_set(new_scaling):
    threading.Thread(target=set_fb("Heating",plants.child(new_scaling).get()["Temperature"] > db.reference('/Temperature').get())).start()
    threading.Thread(target=set_fb("Cooling", plants.child(new_scaling).get()["Temperature"] > db.reference('/Temperature').get())).start()
    threading.Thread(target=set_fb("Ozon", plants.child(new_scaling).get()["Humidity"] > db.reference('/Humidity').get())).start()
    threading.Thread(target=set_fb("Water",plants.child(new_scaling).get()["Soil humidity"] > db.reference('/Soil humidity').get())).start()


def set_default():
    threading.Thread(target=set_fb('Heating',False)).start()
    threading.Thread(target=set_fb('Cooling', False)).start()
    threading.Thread(target=set_fb('Water', False)).start()
    threading.Thread(target=set_fb('Ozon', False)).start()





