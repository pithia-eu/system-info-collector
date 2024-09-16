import argparse


def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test',
                        action='store_true',
                        help='Enable test mode')
    args = parser.parse_args()
    return args
