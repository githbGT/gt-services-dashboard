"""
Refresh the dashboard: catalog Excel -> data/public_catalog.csv -> docs/index.html

    python update.py                      # uses CATALOG_PATH from config.py
    python update.py "<path to catalog>"  # any other location
"""
import sys

from src import build, extract

if __name__ == "__main__":
    extract.main(sys.argv[1] if len(sys.argv) > 1 else None)
    build.main()
    print("\nסיום. לבדוק את docs/index.html בדפדפן, ואז commit + push.")
