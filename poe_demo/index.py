import logging
import sys


def main():
    print('prints')
    logging.basicConfig(
        format="%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
        level="INFO",
        stream=sys.stdout
    )
    logging.getLogger().info('it works')
