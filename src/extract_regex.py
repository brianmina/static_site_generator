import re

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


text_link = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
print(extract_markdown_links(text_link))


text_images = "This is text with an ![image](https://example.com/image.png) and ![another](https://example.com/another.png)"
print(extract_markdown_images(text_images))