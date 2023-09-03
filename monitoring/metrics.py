from prometheus_client import start_http_server, Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request():
    # Simulated ML processing or scoring function
    pass

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request()
