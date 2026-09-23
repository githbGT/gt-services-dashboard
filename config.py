"""
All settings in one place. Edit this file, not the scripts.
"""
from pathlib import Path

ROOT = Path(__file__).parent

# ------------------------------------------------------------------ paths
# The source catalog stays in SharePoint and is NOT committed (see .gitignore).
# Either copy it to the repo root under this name, point this to the synced
# OneDrive/SharePoint path on your computer, or pass a path on the command line:
#   python update.py "C:\Users\...\קטלוג שירותים גני תקווה לתושבים.xlsx"
CATALOG_PATH = ROOT / "קטלוג_שירותים_גני_תקווה_לתושבים.xlsx"
CATALOG_SHEET = "קטלוג שרותים"

PUBLIC_CSV = ROOT / "data" / "public_catalog.csv"
TEMPLATE = ROOT / "templates" / "dashboard.html"
OUTPUT_HTML = ROOT / "docs" / "index.html"
ASSETS = ROOT / "assets"

# ------------------------------------------------------------------ texts
TITLE = "קטלוג השירותים העירוני"
SUBTITLE = ("סקירה ציבורית של השירותים שעיריית גני תקווה מעניקה לתושבים: "
            "למי הם מיועדים, באילו שירותים משתמשים הכי הרבה, וכמה מהם אפשר לבצע מהבית.")
# None = the month the dashboard is built (e.g. "ספטמבר 2026").
# Set a fixed string to override, e.g. UPDATE_DATE = "אוגוסט 2026"
UPDATE_DATE = None
FOOTER = ("הנתונים עודכנו לאחרונה ב{date}. "
          "מקור: קטלוג השירותים העירוני של עיריית גני תקווה. "
          "היקף השימוש מתייחס לשנה החולפת.")

# ------------------------------------------------------------------ columns
# Output CSV column -> header text in the catalog (row 2).
# Matching ignores '*', line breaks and extra spaces, so small header edits are fine.
# A header matches if it equals the text or starts with it.
COLUMNS = {
    "name": "שם השרות",
    "url": "קישור לדף השירות",
    "unit": "שם היחידה מספקת השרות",
    "description": "תאור ופירוט השרות",
    "type": "סוג השרות",
    "audience": "קהל יעד",
    "online": "מקוון",
    # ways to receive the service (כן/לא)
    "ch_branch": "סניפים",
    "ch_phone": "טלפון",
    "ch_email": "דואר אלקטרוני",
    "ch_mail": "דואר",
    "ch_kiosk": "עמדות שירות",
    "level": "רמת דיגיטליות של השירות",
    "usage_total": 'סה"כ היקף שימוש בשנה החולפת',
    "usage_digital": "היקף שימוש דיגיטלי",
    "usage_frontal": "היקף שימוש פרונטלי",
    "usage_phone": "היקף שימוש טלפוני",
}

# ------------------------------------------------------------------ values
# Catalog value -> short display label. Values not listed are kept as they are
# (and reported as new values, so you can decide whether to add a mapping).
AUDIENCE_MAP = {
    "כלל האוכלוסייה": "כלל האוכלוסייה",
    "אוכלוסיה כללית": "כלל האוכלוסייה",
    "הורים": "הורים",
    "בעלי עסקים / עוסקים מורשים / עוסקים פטורים": "בעלי עסקים",
    "ילדים וצעירים (כולל תלמידים וסטודנטים)": "ילדים וצעירים",
}

# Level is taken from the leading digit ("4- טופס דיגיטלי מאחורי הזדהות" -> 4)
LEVEL_NAMES = {
    1: "הגעה פיזית",
    2: "טופס להורדה",
    3: "טופס דיגיטלי",
    4: "דיגיטלי עם הזדהות",
    5: "תהליך אוטומטי",
}

# How each channel is shown in the service list, in display order
CHANNEL_LABELS = {
    "online": "מקוון",
    "ch_phone": "טלפון",
    "ch_email": "דואר אלקטרוני",
    "ch_branch": "פרונטלי",
    "ch_mail": "דואר",
    "ch_kiosk": "עמדת שירות",
}

KNOWN_TYPES = {"אחר", "רישוי, רישום ותעודות", "תשלומים", "בקשת מידע",
               "דיווח מידע", "סיוע כלכלי וקצבאות"}
