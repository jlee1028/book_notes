import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Convert docx to txt')
parser.add_argument('path', type=str, help='Path to the docx file')
args = parser.parse_args()
path = args.path

print(f"Current directory: {os.getcwd()}")

os.chdir(path)

print(f"Current directory after cd DDIA: {os.getcwd()}")

files = os.listdir()

docx_files = []
for file in files:
    if file.endswith('.docx'):
        docx_files.append(file[:-5])

print(f'docs files: {docx_files}')

for filename in docx_files:
    command = ['pandoc',
    '-t', 'markdown_strict',
    f"--extract-media='media/{filename}'",
    f'{filename}.docx',
    '-o', f'{filename}.md']

    print(f'command: {command}')

    subprocess.run(command, check=True)