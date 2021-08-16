# Code Created by Rayhan Biju 2021 #
from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate('#your firebase table')

firebase_admin.initialize_app(cred, {
    'databaseURL': '#your database url'
})


def check_existing_email(email):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("#link to firebase table", None)
    result = firebase.get('#path to firebase table', '')

    return email in str(result)


def coming_soon_as_list():
    from firebase import firebase
    from firebase_admin import db

    coming_soon_list = []
    firebase = firebase.FirebaseApplication("#your firebase table", None)
    coming_soon_titles = db.reference('#firebase table name').child('Coming-Soon').get()

    for title in coming_soon_titles:
        result = firebase.get('#path to firebase table', title)
        coming_soon_list.append(result.get('title'))
    return coming_soon_list
