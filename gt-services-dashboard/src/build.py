"""
Step 2: build the self-contained dashboard HTML from data/public_catalog.csv.

Output: docs/index.html (one file, no external requests: the logo and the
chart library are embedded, so it works inside an iframe on any site).
"""
import base64
import csv
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config  # noqa: E402

HEB_MONTHS = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי",
              "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]

INT_FIELDS = ("usage_total", "usage_digital", "usage_frontal", "usage_phone")


def load_services(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in INT_FIELDS:
            r[k] = int(r[k] or 0)
        r["level"] = int(r["level"]) if r["level"] else None
        r.pop("level_name", None)
    return rows


def logo_data_uri():
    path = config.ASSETS / "logo.png"
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


def update_date():
    if config.UPDATE_DATE:
        return config.UPDATE_DATE
    t = date.today()
    return f"{HEB_MONTHS[t.month - 1]} {t.year}"


def safe_json(obj):
    # keep '</script>' inside data from closing the script tag
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def main():
    services = load_services(config.PUBLIC_CSV)
    html = config.TEMPLATE.read_text(encoding="utf-8")
    parts = {
        "{{TITLE}}": config.TITLE,
        "{{SUBTITLE}}": config.SUBTITLE,
        "{{FOOTER}}": config.FOOTER.format(date=update_date()),
        "{{LOGO}}": logo_data_uri(),
        "{{CHANNELS_JSON}}": safe_json(config.CHANNEL_LABELS),
        "{{DATA_JSON}}": safe_json(services),
        "{{PLOTLY_JS}}": (config.ASSETS / "plotly-basic.min.js").read_text(encoding="utf-8"),
    }
    for k, v in parts.items():
        html = html.replace(k, v)
    config.OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    config.OUTPUT_HTML.write_text(html, encoding="utf-8")
    kb = config.OUTPUT_HTML.stat().st_size / 1024
    print(f"שלב 2: נבנה {config.OUTPUT_HTML.relative_to(config.ROOT)} "
          f"({len(services)} שירותים, {kb:,.0f} KB)")


if __name__ == "__main__":
    main()
