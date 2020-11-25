is_magician = False
is_expert = True

# check if magician AND expert: 'You are a master magician'

if is_expert and is_magician:
    print('You are a master magician')

# check if magician but not expert: 'at least you're getting there'

elif is_magician and not is_expert:
    print('at least you are getting there')

# if you're not magigician: 'you need magic powers'

elif not is_magician:
    print('you need magic powers')
