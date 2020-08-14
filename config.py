import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('BOT_TOKEN')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('OWNER_ID'))
w.write('\n')
w.write('    "USE_SERVICE_ACCOUNTS": '+os.getenv('USE_SERVICE_ACCOUNTS'))
w.write('\n')
w.write('}')
