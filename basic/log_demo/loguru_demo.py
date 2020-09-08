"""
https://github.com/Delgan/loguru
pip3 install loguru
"""
import sys

from loguru import logger

logger.add(sink="file_1.log",
           level="INFO",
           rotation="500 MB",
           compression="zip",
           retention="100 days",
           # backtrace=False
           )


@logger.catch
def my_function(x, y, z):
    # An error? It's catched anyway!
    return 1 / (x + y + z)


config = {
    "handlers":[
        {"sink":sys.stdout, "format":"{time} - {message}"},
        {"sink": "file_2.log", "serialize": True}
    ]
}
logger.configure(**config)

if __name__ == "__main__":
    # logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

    logger.debug("That's it, beautiful and simple logging!")
    logger.info("info")
    print(my_function(0, 0, 0))

    new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

    logger.log("SNAKY", "Here we go!")

    logger.info("=---",{"1":1})

    # import notifiers

    # params = {
    #     "username": "you@gmail.com",
    #     "password": "abc123",
    #     "to": "dest@gmail.com"
    # }


    # # Send a single notification
    # notifier = notifiers.get_notifier("email")
    # notifier.notify(message="The application is running!", **params)
    #
    # # Be alerted on each error message
    # from notifiers.logging import NotificationHandler
    #
    # handler = NotificationHandler("email", defaults=params)
    # logger.add(handler, level="ERROR")
    # print(my_function(0, 0, 0))


