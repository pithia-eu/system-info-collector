from datetime import datetime
from dotenv import load_dotenv

from source.log.logger import logger
from source.utils.arguments import process_args
from source.collect.collect import collect_info


def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    args = process_args()
    test = False
    if args.test:
        test = True
        logger.warning("Test mode enabled. Testing hosts connectivity and program flow - No info will be collected")
    else:
        logger.info('System info process starts')
    load_dotenv()
    collected_info =collect_info(timestamp,
                                 test)
    print(collected_info)
    if args.test:
        logger.warning("Test run completed. No info created")
    else:
        logger.info('System info process completed successfully')


if __name__ == '__main__':
    main()
