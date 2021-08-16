# Code created by Rayhan Biju 2021

from flask import Blueprint, render_template, request, flash, redirect, url_for, session, make_response
import RetrieveInfo
from firebase import firebase
from . import FirebaseOps, Email_Sender

views = Blueprint('views', __name__)

firebase = firebase.FirebaseApplication("#firebase project url", None)


@views.route('/', methods=['GET', 'POST'])
@views.route('/browse', methods=['GET', 'POST'])
def browse():
    data = request.form

    if request.method == 'POST' and len(data.get('tv_series')) == 0:
        flash("Please enter a valid tv series", category='error')

    elif request.method == 'POST' and len(data) > 0:
        tv_series = data.get('tv_series')

        tv_series_info = RetrieveInfo.get_items_as_dict(tv_series)

        if 'Not Found' in str(tv_series_info):
            flash("TV Series Not Found", category='error')

        else:
            return render_template('browse.html', tv_series=tv_series, description=tv_series_info.get('description'),
                                   img_src=tv_series_info.get('image'))
    return render_template('browse.html')


@views.route('/coming-soon/', methods=['GET', 'POST'])
def coming_soon():
    return render_template('coming_soon.html', coming_soon_titles=
    FirebaseOps.coming_soon_as_list())


@views.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    data = request.form
    tv_series = data.get('tv_series')
    if request.method == 'POST' and (len(data.get('email')) == 0 or len(data.get('tv_series')) == 0):
        flash("Please enter all fields", 'error')

    elif request.method == 'POST':

        if FirebaseOps.check_existing_email(data.get('email').lower()) is True:
            flash("You can only get an alert for up to 1 tv show", category='error')
        elif "Not Found" in str(RetrieveInfo.get_items_as_dict(tv_series)):
            flash("Your tv series could not be found", category='error')
        else:
            number_episodes = RetrieveInfo.get_number_of_episodes(tv_series)
            title_id = RetrieveInfo.get_id(tv_series)

            data_to_send = {

                'user_email': data.get('email'),
                'number_of_episodes': number_episodes,
                'title': tv_series,
                'title_id': title_id,

            }

            Email_Sender.send_confirmation_email(data.get('email'), tv_series)

            firebase.post('#table path for firebase', data_to_send)
            flash('Success, you will get an email when your series comes out!', category='success')

            email_cookie = make_response(redirect('/subscribe'))
            email_cookie.set_cookie('email', data.get('email'))
            return email_cookie

    return render_template("subscribe.html", email=request.cookies.get('email'))


@views.route('/subscribe/<tv_series_browse>', methods=['GET', 'POST'])
def subscribe_tv(tv_series_browse):
    data = request.form
    tv_series = data.get('tv_series')

    if request.method == 'POST' and (len(data.get('email')) == 0 or len(data.get('tv_series')) == 0):
        flash("Please enter all fields", 'error')

    elif request.method == 'POST':

        if FirebaseOps.check_existing_email(data.get('email').lower()) is True:
            flash("You can only get an alert for one tv series", category='error')
        elif "Not Found" in str(RetrieveInfo.get_items_as_dict(tv_series)):
            flash("Your tv series could not be found", category='error')
        else:
            number_episodes = RetrieveInfo.get_number_of_episodes(tv_series)
            title_id = RetrieveInfo.get_id(tv_series)

            Email_Sender.send_confirmation_email(data.get('email'), tv_series)

            data_to_send = {

                'user_email': data.get('email'),
                'number_of_episodes': number_episodes,
                'title': tv_series,
                'title_id': title_id,

            }

            firebase.post('#your firebase table', data_to_send)
            flash('Success, you will get an email when your series comes out!', category='success')
    return render_template('subscribe.html', tv_series_browse=tv_series_browse, email=request.cookies.get('email'))
