# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

from app.handlers import langchain_handler

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        chain = langchain_handler.get_qa_chain()
        response = chain(turn_context.activity.text)
        await turn_context.send_activity(response["result"])

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                # if you dont want to create vecotor store everytime then comment this line langchain_handler.create_vector_db()
                await turn_context.send_activity("Hello and welcome!")
                await turn_context.send_activity("Please wait while we create a datastore from sample_faqs")
                langchain_handler.create_vector_db()
                await turn_context.send_activity("datastore has been creates, please ask a question from sample_faqs")
