#!/usr/bin/env python3

import os
from slack import RTMClient
from slack.errors import SlackApiError

@RTMClient.run_on(event='hello')
def hi(**payload):
    try:
        data = payload['data']
        web_client = payload['web_client']
        response = web_client.chat_postMessage(
            channel="#brokebotmountain",
            text="Hi"
        )
    except SlackApiError as e:
        print(f"Got an error: {e.response['error']}")
    except Exception as e:
        print(f"{e}")

@RTMClient.run_on(event='message')
def say_hello(**payload):
    try:
        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
        if 'text' in data and 'Hello' in data.get('text', []):
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

                response = web_client.chat_postMessage(
                    channel=channel_id,
                    text=f"Hi <@{user}>!",
                    thread_ts=thread_ts
                )
    except SlackApiError as e:
        print(f"Got an error: {e.response['error']}")
    except Exception as e:
        print(f"{e}")

rtm_client = RTMClient(token=os.environ["SLACK_API_TOKEN"])
rtm_client.start()
