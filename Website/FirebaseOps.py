# Code Created by Rayhan Biju 2021 #
from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate('Website/event-fusion-bf6b1-firebase-adminsdk-xznez-482251e739.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://event-fusion-bf6b1.firebaseio.com'
})


def check_existing_email(email):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://fir-project-65f8b.firebaseio.com/", None)
    result = firebase.get('/fir-project-65f8b/Alerts', '')

    return email in str(result)

    # return str(result).count(email) < 2



def coming_soon_as_list():
    from firebase import firebase
    from firebase_admin import db

    coming_soon_list = []
    firebase = firebase.FirebaseApplication("https://event-fusion-bf6b1.firebaseio.com/", None)
    coming_soon_titles = db.reference('event-fusion-bf6b1').child('Coming-Soon').get()

    for title in coming_soon_titles:
        result = firebase.get('/event-fusion-bf6b1/Coming-Soon', title)
        coming_soon_list.append(result.get('title'))
    return coming_soon_list
