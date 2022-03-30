from apscheduler.schedulers.background import BackgroundScheduler
import random
from firebase_admin import messaging

from .models import Citation 
from .serializers import CitationSerializer 


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(sendNofifyCitation, 'interval', seconds=5, id='sendNotifyCitation', replace_existing=True)
    scheduler.start()

def sendNofifyCitation():
    topic = 'citai'

    citations = list(Citation.objects.all())

    random_citation = random.choice(citations) 

    serializer = CitationSerializer(
        instance=random_citation,
        many=False,
    )

    message = messaging.Message(
        notification={
            'title': serializer.data['category']['name'],
            'body': serializer.data['text'],
        },
        topic=topic,
    )
    
    messaging.send(message)

