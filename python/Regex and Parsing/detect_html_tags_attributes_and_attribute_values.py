from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
    
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append((tag, attrs))
    
    def handle_endtag(self, tag):
        pass
    
    def print_tags(self):
        for tag, attrs in self.tag_stack:
            print(tag)
            if attrs:
                for attr, value in attrs:
                    print(f'-> {attr} > {value}')

N = int(input().strip())

html_lines = []
for _ in range(N):
    html_lines.append(input().strip())

html_code = '\n'.join(html_lines)

parser = MyHTMLParser()
parser.feed(html_code)
parser.print_tags()
