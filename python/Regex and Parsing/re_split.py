regex_pattern = r"(?<=\d)[.,](?=\d)"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))