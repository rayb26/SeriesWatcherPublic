from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



def send_confirmation_email(email, title):
    message = Mail(from_email='from email address', to_emails=email,
                   subject="Your now in the loop for " + title,
                   plain_text_content="Hello!\nYou'll now be one of the first people to know when " + title + " releases more "
                                                                                                              "episodes"
                                                                                                              "\nBest,\n"
                                                                                                              "the "
                                                                                                              "SeriesWatcher "
                                                                                                              "team ")

    try:
        sg = SendGridAPIClient('#add your api key here')
        sg.send(message)
    except Exception as e:
        return "error"
