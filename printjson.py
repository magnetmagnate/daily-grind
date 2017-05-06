#!/usr/bin/env python3

import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

