import sys
import argparse
from pyChatGPT import ChatGPT

class ChatBot:
    def __init__(self, conversation_id='', verbose=True, chrome_args=[],unknown=[]):
        self.session_token = ''
        self.conversation_id = conversation_id
        self.verbose = verbose
        self.chrome_args = chrome_args
        self.api = ChatGPT(session_token=self.session_token, conversation_id=self.conversation_id, verbose=self.verbose, chrome_args=self.chrome_args)

    def start(self):
        if self.conversation_id:
            self.interactive_mode()
        else:
            self.one_time_mode(unknown)

    def interactive_mode(self):
        while True:
            user_input = input("請輸入詢問的問題：")
            resp = self.api.send_message(user_input)
            print(resp['message'])

    def one_time_mode(self,user_input):
        resp = self.api.send_message(user_input)
        print(resp['message'])
        if args.delete:
            self.api.clear_conversations()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A chatbot based on OpenAI\'s GPT')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-c", "--conversation_id", required=False, help="conversation ID")
    group.add_argument("-d", "--delete", required=False, help="clear conversation history", action='store_true')
    args, unknown = parser.parse_known_args()
    bot = ChatBot(conversation_id=args.conversation_id, verbose=True, chrome_args=['--headless'],unknown=unknown)
    bot.start()