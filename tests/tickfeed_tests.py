import feed.tickfeed as tf


feed = tf.TickFeed("test.csv")
feed.prepare()
while feed.valid():
    print(feed.get())
