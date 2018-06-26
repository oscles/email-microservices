from django.core.mail import EmailMessage

from django.conf import settings

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_HOST_USER='your email',
    EMAIL_HOST_PASSWORD='your password',
    EMAIL_PORT=587,
    EMAIL_USE_TLS=True,
)


class EmailSender:
    email = EmailMessage()

    def __init__(self, subject, to_address, body, from_email=None):
        self.email.subject = subject
        self.email.from_email = from_email or 'osnaiderluis94@mail.com'
        self.email.to = [to_address]
        self.email.body = body

    def send(self):
        try:
            self.email.send(fail_silently=True)
            print('Mensaje enviado satisfactoriamente...')
        except:
            print('Estamos procesando su mensaje...')
