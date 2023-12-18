This application comprises an Android client-server system. The Android app collects user-entered data, which is then sent via a POST request to a specified server address. The server, written in Python, utilizes a K-Nearest Neighbors (KNN) machine learning model trained on the Iris dataset.

Here's a breakdown:

### Android Application (Client)
- **Functionality**: The app captures user input data through an interface.
- **Operation**: When the user clicks the "Send" button, the entered data is formatted, converted into JSON, and sent as a POST request to a predetermined server URL (`http://192.168.1.36:8080/` in this case).
- **Feedback**: Upon receiving a response from the server, the app displays a toast message showing either the successful result or a failure message.

### Python Server
- **HTTP Server**: Utilizes Python's `http.server` to handle incoming POST requests.
- **Prediction Handling**: A `PredictionHandler` class processes incoming POST data, extracts the 'data' field from the JSON payload, and uses a pre-trained KNN model to predict the type of Iris flower based on this data.
- **Response**: The server responds with a JSON payload containing the predicted result ('Iris setosa', 'Iris versicolor', or 'Iris virginica').

The KNN model used by the server is trained on the Iris dataset to classify iris flowers into different species based on their features.

