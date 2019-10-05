# Page Summarizer API
A minimalist Flask Api that takes in a Page summarizer model and renders the output of the Model to the user.
A Sample POST request is described in the request.py file.

# Testing

1. Clone this repo

2. Install requirements

    ```pip install -r requirements.txt```

3. Add a pickle model file to the root of this project and name it modelfile.pkl

4. Run the app

    ```python app.py```

5. To get information on how the app works, make a GET request to ```http://127.0.0.1:5000```.

    Here is a sample response
    ```
        {
            "data": "Welcome to the Page Summarizer API. To summarize pls make a POST request to the /api/summarize endpoint using the format {"article": "some article content that needs summarizing"
        }
    ```

6. To summarize articles, make a POST request to ```http://127.0.0.1:5000```.
    Here is a sample body
    ```
        {
            "article": "some article content that needs summarizing"
        }
    ```

    Here is a sample response
    ```
        {
            "summary": "summary of some article content"
        }
    ```
