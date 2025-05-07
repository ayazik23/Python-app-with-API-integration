# BBC News Headlines Viewer

This is a simple Python Flask web application that fetches top headlines from **BBC News** using the [NewsAPI](https://newsapi.org), saves the data as a JSON file (`output.json`), and displays the news in a clean, responsive web interface.

---

## Features

- Fetches live top headlines from **BBC News**.
- Saves the fetched data into `output.json`.
- Displays the news with title, description, image, and link.
- Clean, user-friendly, and responsive design using HTML/CSS.
- Built with **Flask** and **NewsAPI**.

---

## Requirements

- Python 3.7+
- pip

Install dependencies:

```bash
pip install flask requests
```
---

## Structure

bbc-news-app/
- ├── app.py                 # Main Flask app
- ├── output.json            # Saved API response
- ├── templates/
- │         └── index.html         # HTML template for displaying news
- └── README.md              # This documentation

---
## API Change 

- Visit https://newsapi.org/sources to find the list of available news sources.
- Update this line in app.py:
    ```bash
    BBC_NEWS_URL = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}'
    ```
- Example of CNN:
    ```bash
    CNN_NEWS_URL = f'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey={API_KEY}'
    ```
---

## License

MIT License. Feel free to modify and reuse for personal or academic projects.

---

## Author

ayazik23