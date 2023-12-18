from http.server import BaseHTTPRequestHandler, HTTPServer
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import json
import numpy as np

class PredictionHandler(BaseHTTPRequestHandler):
    knn = None

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        new_data = data['data']
        new_data_np = np.array(new_data).reshape(1, -1)
        prediction = self.knn.predict(new_data_np)

        if prediction[0] == 0:
            result = 'Iris setosa'
        elif prediction[0] == 1:
            result = 'Iris versicolor'
        else:
            result = 'Iris virginica'

        response = {'result': result}
        self._set_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=PredictionHandler, port=8080):
    server_address = ('', port)
    handler_class.knn = KNeighborsClassifier(n_neighbors=3)
    iris = load_iris()
    X = iris.data
    y = iris.target
    handler_class.knn.fit(X, y)

    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
