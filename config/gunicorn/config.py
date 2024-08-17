from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

workers = 2
reload = True
errorlog = str(BASE_DIR / 'logs/error.log')
access_log = str(BASE_DIR / 'logs/access.log')

bind = "0.0.0.0:8000"

daemon = True