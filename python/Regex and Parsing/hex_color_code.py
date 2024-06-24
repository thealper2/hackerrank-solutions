import re

def extract_hex_color_codes(css_text):
    pattern = r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})"
    hex_color_codes = re.findall(pattern, css_text)
    return hex_color_codes

N = int(input().strip()) 
css_text = ''
for _ in range(N):
    css_text += input().strip() + '\n'

hex_color_codes = extract_hex_color_codes(css_text)
for code in hex_color_codes:
    print(code)
