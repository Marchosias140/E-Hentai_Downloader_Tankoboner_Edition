import subprocess

# Run input_the_links.py
subprocess.run(['python3', 'input_the_links.py'])

# Run links_inputter.sh
subprocess.run(['./links_inputter.sh'])

# Run multiple_print_all_links.py, pipe output to grep, and write to list.txt
output = subprocess.Popen(['python3', 'multiple_print_all_links.py'], stdout=subprocess.PIPE)
grep_output = subprocess.check_output(['grep', '-i', '/s/'], stdin=output.stdout)
with open('list.txt', 'wb') as f:
    f.write(grep_output)

# Run processing
subprocess.run(['./processing.sh'])

# Run soup.py
subprocess.run(['python3', 'soup.py'])

# Regenerate multi and soup

subprocess.run(['./regenerator.sh'])

# Delete .txt files

subprocess.run(['./clean.sh'])



