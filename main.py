from datetime import datetime
from dotenv import load_dotenv

from source.log.logger import logger
from source.utils.arguments import process_args
from source.collect.collect import collect_info
from source.collect.csv import create_csv_report


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
    create_csv_report(timestamp,
                      collected_info,
                      test)
    if args.test:
        logger.warning("Test run completed. No info created")
    else:
        logger.info('System info process completed successfully')


if __name__ == '__main__':
    main()
