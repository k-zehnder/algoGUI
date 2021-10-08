# NOTE: https://stackoverflow.com/questions/57273945/imports-break-vscode-testing-with-pytest

import os
import sys

if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(ROOT_DIR, "scripts"))
