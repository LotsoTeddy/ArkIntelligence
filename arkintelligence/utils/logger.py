import sys

from loguru import logger

logger.remove()

logger.level("INFO", color="<fg cyan>")
logger.level("WARNING", color="<fg yellow>")
logger.level("ERROR", color="<fg red>")
logger.level("DEBUG", color="<fg white>")
logger.level("CRITICAL", color="<fg magenta>")

logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <green>{file}</green>:<green>{line}</green> - <level>{message}</level>",
    # level="CRITICAL",
)

# We disable the logger for arkintelligence defaultly
logger.disable("arkintelligence")

__all__ = ["logger"]
