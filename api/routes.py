from api.box_api import authentication, finish_authentication

routes = [
    (r'/api/login_test', 'api.login_test.MyHandler'),
    (r'/api/get_box_', 'api.login_test.MyHandler'),
    (r'/api/box/authentication', authentication),
    (r'/api/box/finish_authentication', finish_authentication),
]
