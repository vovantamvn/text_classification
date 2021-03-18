from crawl import crawl_data, format_text, tokenize_string
import pickle
import os

if __name__ == '__main__':
    MODEL_PATH = "/home/tamvv/PycharmProjects/detectText/models"
    model = pickle.load(open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'rb'))

    urls = []
    texts = []

    while True:
        url = input()
        if url == "end":
            break
        if url.startswith("http://") or url.startswith("https://"):
            urls.append(url)

    for url in urls:
        text = crawl_data(url)
        text = format_text(text)
        text = tokenize_string(text)
        texts.append(text)

    labels = model.predict(texts)
    print(labels)
