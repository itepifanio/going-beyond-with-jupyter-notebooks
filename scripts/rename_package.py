import re
import os
import sys
from nbdev.config import add_init, get_config
from nbdev.doclinks import _build_modidx, nbglob, nb_export

# Renames python library

def _is_snake_case_without_symbols(s):
    pattern = r'^[a-z]+(?:_[a-z]+)*$'
    return bool(re.match(pattern, s))

def extract_legacy_package_name() -> str:
    pattern = r'lib_name\s*=\s*(\w+)'

    with open(f'settings.ini', 'r') as f:
        settings = f.read()

    return re.search(pattern, settings).group(1)

def rename_settings_ini(legacy_name: str, new_name: str):
    with open(f'settings.ini', 'r') as f:
        settings = f.read()

    settings = re.sub(legacy_name, new_name, settings)

    with open(f'settings.ini', 'w') as f:
        f.write(settings)

def rename_lib_folder(legacy_name: str, new_name: str):
    os.rename(legacy_name, new_name)

def _change_imports(file: str, legacy_name: str, new_name: str):
    with open(file, 'r') as f:
        code = f.read()
        code = re.sub(r'(?<!\.)\b'+legacy_name+r'\b', new_name, code)

    with open(file, 'w') as f:
        f.write(code)  

def _export(legacy_name, new_name: str):
    files = nbglob(path='nbs', as_path=True).sorted('name')

    for file in files:
        _change_imports(file, legacy_name, new_name)

    for f in files: nb_export(f, procs=None)
    add_init(get_config().lib_path)
    _build_modidx()

if __name__ == "__main__":
    assert len(sys.argv) == 2, "missing package name"

    invalid_package_name = (
        "Invalid package name " 
        "try a singleword or snake_case"
    )
    new_package_name = sys.argv[1]

    assert _is_snake_case_without_symbols(new_package_name), invalid_package_name

    legacy_package_name = extract_legacy_package_name()
    rename_settings_ini(legacy_package_name, new_package_name)
    rename_lib_folder(legacy_package_name, new_package_name)
    _export(legacy_package_name, new_package_name)
