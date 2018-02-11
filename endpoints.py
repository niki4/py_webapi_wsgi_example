import server_v3

application = server_v3.App()


@application.register_handler('^/cart/$', methods=['GET', 'POST'])
def cart_url_handler(environ, url_params):
    return 'Cart page', 200, {}


@application.register_handler('^/$')
def index_url_handler(environ, url_params):
    return 'Index page', 200, {}


@application.register_handler('^/products/$')
def info_url_handler(environ, url_params):
    data = [
        {'title': 'Iphone X', 'price': '50000'},
        {'title': 'Iphone X+', 'price': '60000'},
    ]
    return data, 201, {'X-test-header': '123'}


@application.register_handler('^/products/(?P<product_id>\d+)/$')
def product_info_url_handler(environ, url_params):
    data = {'title': 'Iphone X', 'price': '50000', 'id': url_params['product_id']}
    return data, 200, {}
