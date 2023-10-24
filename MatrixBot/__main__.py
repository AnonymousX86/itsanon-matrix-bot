# -*- coding: utf-8 -*-
from nio.events.room_events import RoomMessageText
from nio.rooms import MatrixRoom
from simplematrixbotlib import (
    Bot,
    Config,
    Creds,
    MessageMatch
)

from MatrixBot.config import HOMESERVER_URL, BOT_LOGIN, BOT_PASSWORD, PREFIX


def main() -> None:
    config = Config()
    config.load_toml('config.toml')
    creds = Creds(
        HOMESERVER_URL,
        BOT_LOGIN,
        BOT_PASSWORD
    )
    bot = Bot(creds, config)

    @bot.listener.on_message_event
    async def echo(room: MatrixRoom, message: RoomMessageText):
        if not (match := MessageMatch(room, message, bot, PREFIX)).is_not_from_this_bot():
            return
        elif not match.prefix():
            return
        elif match.command('echo'):
            await bot.api.send_text_message(
                room.room_id, ' '.join(arg for arg in match.args())
            )

    bot.run()


if __name__ == '__main__':
    main()
