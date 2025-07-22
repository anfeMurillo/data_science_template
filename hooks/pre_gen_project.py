import sys

ERROR_COLOR = "\033[31m"
MESSAGE_COLOR = "\033[34m"
RESET_ALL = "\033[0m"

project_slug = "{{cookiecutter.project_slug}}"

if project_slug.startswith('_') or project_slug.startswith('-'):
    print(f"{ERROR_COLOR}Name started with '_' or '-' isn't allow{RESET_ALL}")
    sys.exit(1)
    
print(f"{MESSAGE_COLOR}Let's build it!{RESET_ALL}")