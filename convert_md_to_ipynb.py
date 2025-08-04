import os
import nbformat
from nbformat import v4 as nbf

# Directories
tutorial_dir = os.path.join(os.path.dirname(__file__), 'tutorial')
output_dir = os.path.join(os.path.dirname(__file__), 'tutorial_notebooks')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over markdown files in tutorial
for fname in os.listdir(tutorial_dir):
    if not fname.endswith('.md'):
        continue
    input_path = os.path.join(tutorial_dir, fname)
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines()
    cells = []
    in_code = False
    code_lines = []
    md_lines = []

    for line in lines:
        if line.startswith('```'):
            if in_code:
                # Close code block
                cells.append(nbf.new_markdown_cell('\n'.join(md_lines))) if md_lines else None
                md_lines = []
                cells.append(nbf.new_code_cell('\n'.join(code_lines)))
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
        else:
            md_lines.append(line)
    # Add any remaining markdown
    if md_lines:
        cells.append(nbf.new_markdown_cell('\n'.join(md_lines)))
    # Create notebook for tutorial
    nb = nbf.new_notebook(cells=cells)
    output_path = os.path.join(output_dir, fname.replace('.md', '.ipynb'))
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f'Converted {fname} -> {output_path}')

# Process Chinese tutorials in tutorial_zh
zh_tutorial_dir = os.path.join(os.path.dirname(__file__), 'tutorial_zh')
zh_output_dir = os.path.join(os.path.dirname(__file__), 'tutorial_notebooks_zh')
# Ensure output directory exists
os.makedirs(zh_output_dir, exist_ok=True)

for fname in os.listdir(zh_tutorial_dir):
    if not fname.endswith('.md'):
        continue
    input_path = os.path.join(zh_tutorial_dir, fname)
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines()
    cells = []
    in_code = False
    code_lines = []
    md_lines = []

    for line in lines:
        if line.startswith('```'):
            if in_code:
                # Close code block
                cells.append(nbf.new_markdown_cell('\n'.join(md_lines))) if md_lines else None
                md_lines = []
                cells.append(nbf.new_code_cell('\n'.join(code_lines)))
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
        else:
            md_lines.append(line)
    # Add any remaining markdown
    if md_lines:
        cells.append(nbf.new_markdown_cell('\n'.join(md_lines)))
    # Create notebook for Chinese tutorial
    nb = nbf.new_notebook(cells=cells)
    output_path = os.path.join(zh_output_dir, fname.replace('.md', '.ipynb'))
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f'Converted zh {fname} -> {output_path}')
