sample_dict = {'value1': '12', 'value2': '37', 'value3': '1', 'value4': '83', 'value5': '17',
               'value6': '56', 'value7': '91', 'value8': '48', 'value9': '66', 'value10': '73'}

sample_dict['value2'] = '26'
sample_dict['value7'] = '2'

sample_dict.pop('value3')
sample_dict['value'] = None
print(sample_dict)

