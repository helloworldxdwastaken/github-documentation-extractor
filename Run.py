import subprocess
import os

def clone_repository(repo_url):
    subprocess.run(['git', 'clone', repo_url])

def clean_combined_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = line.strip().replace('#', '').replace('*', '').replace('-', '').replace('>', '').strip()
            if cleaned_line:
                outfile.write(cleaned_line + '\n')

def combine_markdown_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md') or file.endswith('.mdx'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read() + '\n\n')

clone_repository('https://github.com/open-webui/docs.git')
combine_markdown_files('docs/docs', 'combined_docs.txt')
clean_combined_file('combined_docs.txt', 'final_combined_docs.txt')