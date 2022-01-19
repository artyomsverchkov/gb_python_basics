# HW_Lesson8_Task2

# ip_reg = r'((?:[0-9]{1,3}[.]){3}[0-9]{1,3}) - - '
# datetime_reg = r'.([0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}). .'
# rest_request_reg = r'([A-Z]{3,7}) '
# link_reg = r'([/\w+]{0,}) '
# protocol_version_reg = r'([A-Z]{4}/\d+.\d+\") ' - not used in output
# code_1 = r'([0-9]+) '
# code_2 = r'([0-9]+)'

import re
import requests

log_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
text_log = requests.get(log_url).text

regex = re.compile(r'((?:[0-9]{1,3}[.]){3}[0-9]{1,3}) - - '
                   r'.([0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}). .'
                   r'([A-Z]{3,7}) '
                   r'([/\w+]{0,}) '
                   r'([A-Z]{4}/\d+.\d+\") ' # group5 like: "HTTP/1.1 " as protocol_version_reg - not used in output
                   r'([0-9]+) '
                   r'([0-9]+)')

for ip_reg, datetime_reg, rest_request_reg, link_reg, protocol_version_reg, code_1, code_2 in regex.findall(text_log):
    tuple_line = (ip_reg, datetime_reg, rest_request_reg, link_reg, code_1, code_2)
    print(tuple_line)