CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():

    CURRENT_CHANNEL = ''

    def __init__(self, channels: list):
        self.channels = channels

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, number):
        global CURRENT_CHANNEL
        CURRENT_CHANNEL = self.channels[number - 1]
        return CURRENT_CHANNEL

    def next_channel(self):
        global CURRENT_CHANNEL
        CURRENT_CHANNEL = self.channels[self.channels.index(CURRENT_CHANNEL) + 1]
        return CURRENT_CHANNEL

    def previous_channel(self):
        global CURRENT_CHANNEL
        CURRENT_CHANNEL = self.channels[self.channels.index(CURRENT_CHANNEL) - 1]
        return CURRENT_CHANNEL

    def current_channel(self):
        global CURRENT_CHANNEL
        return CURRENT_CHANNEL

    def is_exist(self, number_or_name):
        search_result = ""
        if type(number_or_name) == int:
            try:
                self.channels[number_or_name-1]
                search_result = "Yes"
            except IndexError:
                search_result = "No"
        elif type(number_or_name) == str:
            try:
                self.channels.index(number_or_name)
                search_result = "Yes"
            except ValueError:
                search_result = "No"
        else:
            search_result = "No"
        return search_result



def task3(channels: list):

    controller = TVController(channels)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(2))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(4))
    print(controller.is_exist("BBC"))
