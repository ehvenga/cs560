OK_FORMAT = True
test = {   'name': 'q35',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(farmers_markets_locations_by_latitude) == tables.Table\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # HINT: Check the order of your table. \n'
                                               ">>> list(farmers_markets_locations_by_latitude.column('y').take(range(3)))\n"
                                               '[64.862750000000005, 64.8459, 64.844414]',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
