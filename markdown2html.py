#!/usr/bin/python3
'''Script to convert Markdown file to HTML file.
'''

import sys
import os
import markdown


def convert_markdown_to_html(markdown_file, output_file):
    '''
    Converts the content of a Markdown file to HTML and
    writes the result to an output file.

    Parameters:
    - markdown_file (str): The path to the Markdown input file.
    - output_file (str): The path to the HTML output file.

    Returns:
    - int: Exit code, where 0 indicates success and 1 indicates an error.
    '''
    try:
        if not os.path.isfile(markdown_file):
            raise FileNotFoundError(f'Missing {markdown_file}')

        # Read the content from the Markdown file
        with open(markdown_file, encoding='utf-8') as file:
            md_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Write the HTML content to the output file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        return 0

    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 1
    except Exception as e:
        print(f'An error occurred: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_markdown_file> \
               <output_html_file>", file=sys.stderr)
        sys.exit(1)

    input_markdown_file = sys.argv[1]
    output_html_file = sys.argv[2]

    exit_code = convert_markdown_to_html(input_markdown_file, output_html_file)

    sys.exit(exit_code)
