from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# api key = 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

def send_confirmation_email(email, title):
    message = Mail(from_email='serieswatcherteam@gmail.com', to_emails=email,
                   subject="Your now in the loop for " + title,
                   plain_text_content="Hello!\nYou'll now be one of the first people to know when " + title + " releases more "
                                                                                                              "episodes"
                                                                                                              "\nBest,\n"
                                                                                                              "the "
                                                                                                              "SeriesWatcher "
                                                                                                              "team ")

    try:
        sg = SendGridAPIClient('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')
        sg.send(message)
    except Exception as e:
        return "error"
