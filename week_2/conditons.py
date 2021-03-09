# x = 10
# if x > 0:
#     print(f'{x} is postive')
# elif x == 0:
#     print(f'{x} is zero')
# else:
#     print(f'{x} is negative')

weather = input('Enter the weather: ').lower()
if weather == 'rainy':
    print('Please take unumbrella')
elif weather =='sunny':
    print('Go out freely, it just a shiny day')
elif weather == 'cloudy':
    print('No one knows about todays\' weather is just cloudy and gloomy')
elif weather =='snowy':
    print('Wear properly, you might found frozen.')
else:
    print('No one knows the weather')
