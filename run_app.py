from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-332206272599-331125880628-333503980579-09eb901792d7a8577148524360396e19', #app verification token
							'xoxb-334436638134-5cpe4KPNVIMqOxqvvrFPoUO7', # bot verification token
							'5U6QRP2YZZS9igSvVauRQl33', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))