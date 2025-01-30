import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Convert docx to txt')
parser.add_argument('path', type=str, help='Path to the docx file')
args = parser.parse_args()
path = args.path

os.chdir(path)

files = os.listdir('docx_files')

docx_files = []
for file in files:
    if file.endswith('.docx'):
        docx_files.append(file[:-5])

for file in docx_files:
    command = ['pandoc',
    '-t', 'markdown_strict',
    f"--extract-media=media/{file}",
    f'docx_files/{file}.docx',
    '-o', f'{file}.md']

    subprocess.run(command, check=True)