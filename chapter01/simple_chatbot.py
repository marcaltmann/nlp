greetings = 'Hi Hello Greetings'.split()

while True:
    user_statement = input('Input: ')
    user_token_sequence = user_statement.split()

    if user_token_sequence[0] in greetings:
        bot_reply = 'Thermonuclear war is a strange game. '
        bot_reply += 'The only winning move is not to play.'
    else:
        bot_reply = 'Would you like to play a nice game of chess?'

    print(bot_reply)
