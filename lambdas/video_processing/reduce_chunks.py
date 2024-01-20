import logging
from typing import Dict, Any
import os

JOB_TABLE_NAME = os.environ["JOB_TABLE_NAME"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
  """
  Reduces all processed chunks to a single video.
  """
  
  logger.info(f"Invoked with event: {event}")

  # TODO: implement job

  logger.info(f"Success")

  return {}
