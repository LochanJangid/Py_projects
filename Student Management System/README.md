# SMS — School Management System

CLI-based school management system using Python + SQLite.

## Structure
```
school_sms/
├── app.py                # Entry point
├── database/
│   ├── create_tables.py  # Schema definition
│   └── database.py       # All DB queries
├── models/
│   └── person.py         # Student & Teacher models
├── ui/
│   ├── student_ui.py
│   ├── teacher_ui.py
│   ├── finance_ui.py
│   └── utils_ui.py
├── README.md
└── requirements.txt

```

## Setup
```bash
python -m venv env
source env/bin/activate      # Windows: env\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Commands
| Key | Action |
|-----|--------|
| `1` | Add student |
| `2` | Add teacher |
| `3` | Deposit fee |
| `4` | Pay salary |
| `5` | List payments |
| `6` | Update student |
| `7` | Update teacher |
| `8` | List students |
| `9` | List teachers |
| `11` | Show commands |
| `0` | Exit |

## Notes
- `SchoolData.db` is auto-created on first run

*By Lochan Jangid*