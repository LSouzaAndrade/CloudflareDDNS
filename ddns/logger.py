import logging
import sys


logger = logging.getLogger("ddns")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)  # Apenas terminal
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)