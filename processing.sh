#!/bin/bash

python3 multiple_print_all_links.py | grep -i /s/ > list.txt && \
sed -i 's/.*/"&"/' list.txt && \
sed -i '$!s/$/,/' list.txt && \
sed -i '14 r list.txt' soup.py

