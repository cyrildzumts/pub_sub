

class Dispatcher:
    
    """

    """

    def __init__(self):
        #self.queued_data = []
        self.publishers = set()
        self.subscribers = set()
        self.topics = set()

    def add_publisher(self, publisher):
        self.publishers.add(publisher)
    
    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def update(self, data):
        if data:
            for subscriber in self.subscribers:
                if data.topic in subscriber.get_topics():
                    subscriber.update(data)


    def get_topics(self):
        return self.topics
    

    def contains(self, topic):
        found = False
        if isinstance(topic, int):
            found = topic in self.topics
        return found

    
    def remove_topic(self, topic):
        if isinstance(topic, int):
            try:
                self.topics.remove(topic)
                print("topic  {} was successfuly removed".format(topic))
            except KeyError as e:
                print("No topic found for {}".format(topic))
                print(e)

    def add_topic(self, topic):
        if isinstance(topic, int):
            self.topics.add(topic)




class Publisher:
    num_publishers = 0

    def __init__(self):
        Publisher.num_publishers += 1
        self.num = Publisher.num_publishers
        self.topic = -1
        self.dispatchers = set()
    
    def set_topic(self, topic):
        if isinstance(topic, int):
            self.topic = topic
    

    def get_topic(self):
        return self.topic
    

    def register(self, dispatcher):
        self.dispatchers.add(dispatcher)
        dispatcher.add_publisher(self)
        print("Dispatcher registered on Publisher {}".format(self.num))

    def deregister(self, dispatcher):
        self.dispatchers.discard(dispatcher)

    def notify(self, data):
        print("Publisher {}  published data".format(self.num))
        if data:

            data.topic = self.topic
            for d in self.dispatchers:
                d.update(data)
    



class Subscriber :
    num_subscribers = 0

    def __init__(self):
        self.dispatchers = set()
        self.topics = set()
        Subscriber.num_subscribers += 1
        self.num = Subscriber.num_subscribers
    

    def get_topics(self):
        return self.topics
    

    def register(self, dispatcher):
        self.dispatchers.add(dispatcher)
        dispatcher.add_subscriber(self)
        print("Dispatcher registered on Subscriber {}".format(self.num))
    
    def register_to_topic(self, topic):
        self.topics.add(topic)
    
    def deregister_from_topic(self, topic):
        self.topics.discard(topic)
    
    def remove_dispatcher(self, dispatcher):
        self.dispatchers.discard(dispatcher)
    
    def update(self, data=None):
        print("Subscriber {} get new published data for topic {}".format(self.num, data.topic))

    

class Data:
    
    def __init__(self):
        self.data = "new data"