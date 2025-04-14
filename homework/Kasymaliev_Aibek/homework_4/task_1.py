my_dict = {'tuple': (1, 2, 3, 4, 'ak47', True), 'list': ['good', 'day', True, 77, 99], 'dict': {'num_1': 1, 'num_2': 2,
           'num_3': 3, 'log_sost': False, 'log_sost_1': True}, 'set': {1, 2, 3, 4, 5}}

print(my_dict['tuple'][-1])


my_dict['list'].append(62)

my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'gg'

del my_dict['dict']['num_1']

my_dict['set'].add(22)

my_dict['set'].remove(3)

print(my_dict)
