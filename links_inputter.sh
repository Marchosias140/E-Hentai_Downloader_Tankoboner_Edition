#!/bin/bash

sed -i 's/.*/"&"/' links.txt && \
sed -i '$!s/$/,/' links.txt && \
sed -i '31 r links.txt' multiple_print_all_links.py