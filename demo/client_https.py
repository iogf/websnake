"""
Overview
========

Retrieve user data from github.

"""

from websnake import Get, ResponseHandle, core, die

def on_response(request, response):
    print('Headers:', response.headers)
    print('Code:', response.code)
    print('Version:', response.version)
    print('Reason:', response.reason) 
    print('Data:', response.fd.read())
    die('Request done.')

if __name__ == '__main__':
    request = Get('https://www.google.com.br/')
    
    request.add_map(ResponseHandle.RESPONSE, on_response)
    core.gear.mainloop()






