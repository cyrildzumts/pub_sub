import pub_sub


def test_pub_sub():
    dispatcher = pub_sub.Dispatcher()
    publisher_1 = pub_sub.Publisher()
    publisher_2 = pub_sub.Publisher()
    subcriber_1 = pub_sub.Subscriber()
    subcriber_2 = pub_sub.Subscriber()
    subcriber_3 = pub_sub.Subscriber()

    publisher_1.register(dispatcher)
    publisher_2.register(dispatcher)

    subcriber_1.register(dispatcher)
    subcriber_2.register(dispatcher)
    subcriber_3.register(dispatcher)

    data1 = pub_sub.Data()
    data2 = pub_sub.Data()
    data2.topic = 3
    data1.topic = 1
    publisher_1.set_topic(1)
    publisher_2.set_topic(3)

    subcriber_1.register_to_topic(1)
    subcriber_2.register_to_topic(1)
    subcriber_2.register_to_topic(3)
    subcriber_3.register_to_topic(3)

    publisher_1.notify(data1)
    publisher_2.notify(data2)

