import boto3, json
from botocore.exceptions import ClientError
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from models import QuizForm

AWS_REGION = 'us-east-1'
BODY_TEXT = 'Phrases Recieved!'
CHARSET = 'UTF-8'
SENDER = 'Your Name <youremail@gmail.com>' # ENTER YOUR NAME and EMAIL
RECIPIENT = 'youremail@gmail.com'          # ENTER YOUR EMAIL

class Config(object):
  SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

application = Flask(__name__)
application.config.from_object(Config)

Bootstrap(application)

ses_client = boto3.client('ses',region_name=AWS_REGION)

@application.route('/', methods=['GET', 'POST'])
def take_test():
  form = QuizForm(request.form)
  if not form.validate_on_submit():
    return render_template('take_quiz_template.html', form=form)
  if request.method == 'POST':
    user_json = {}
    user_json['customer_email'] = request.form.get('customer_email')
    user_json['qty_beaks'] = request.form.get('qty_beaks')
    user_json['fry_the_beaks'] = request.form.get('fry_the_beaks')
    user_json['comments'] = request.form.get('comments')

    SUBJECT = 'Order for {} beak{}'.format(user_json['qty_beaks'], 's.' if int(user_json['qty_beaks']) > 1 else '.')
    BODY_HTML = render_template( 'pretty_json.html', user_json = user_json )
    try:
      response = ses_client.send_email(
        Destination = { 'ToAddresses': [ RECIPIENT, ], },
        Message={ 'Body': { 'Html': { 'Charset': CHARSET, 'Data': BODY_HTML, },
                            'Text': { 'Charset': CHARSET, 'Data': BODY_TEXT, }, }, 
                  'Subject': { 'Charset': CHARSET, 'Data': SUBJECT, },}, 
        Source=SENDER, )
    except ClientError as e:
        render_msg = 'Email failed with response <b>{}</b>.'.format(e.response['Error']['Message'])
    else:
        render_msg = 'Email sent!  Message ID: <b>{}</b>'.format(response['MessageId'])
    return render_msg

if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True)