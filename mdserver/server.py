import logging
from argparse import ArgumentParser

USERDATA_TEMPLATE = """\
#cloud-config
hostname: {{hostname}}
local-hostname: {{hostname}}
fqdn: {{hostname}}.localdomain
manage_etc_hosts: true
ssh_authorized_keys:
    - {{public_key_default}}
"""

logger = logging.getLogger("mdserver")

def early_logging():
    """Set up an early logging mechanism."""
    early_logger = logging.getLogger("early_logger")
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stdout_log = logging.StreamHandler()
    stdout_log.setLevel(logging.DEBUG)
    stdout_log.setFormatter(formatter)
    early_logger.setLevel(logging.DEBUG)
    early_logger.addHandler(stdout_log)

def main():
    early_logging()

if __name__ == "__main__":
    main()