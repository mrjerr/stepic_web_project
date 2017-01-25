# import pprint
def app(environ, start_response):
    data = b'\n'.join([i.encode('utf8') for i in environ.get('QUERY_STRING').split('&')])
    # pprint.pprint(environ)
    start_response("200 OK", [
         ("Content-Type", "text/plain"),
         ("Content-Length", str(len(data)))
    ])
    return iter([data])
