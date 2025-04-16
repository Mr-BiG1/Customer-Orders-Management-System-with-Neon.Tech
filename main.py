# Darsan Sabu George 
# 2025-04-16
# PROG2390 
# 8959922

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.gui.layout import get_gui # type: ignore

if __name__ == "__main__":
    get_gui()
