import os
import pandas

from source.utils.environment import get_env_variable
from source.utils.directory import create_local_directory
from source.utils.permissions import change_local_directory_permission
from source.log.logger import logger


def create_csv_report(timestamp,
                      collected_info,
                      test):
    collected = []
    errors = []
    for system, results in collected_info.items():
        system_results = {"system": system}
        for result_key, results_value in results.items():
            system_results[result_key] = results_value
        if "error" in results.keys():
            errors.append(system_results)
        else:
            collected.append(system_results)
    collected_df = pandas.DataFrame(collected)
    errors_df = pandas.DataFrame(errors)
    reports_csv_path = get_env_variable("REPORT_PATH")
    create_local_directory(reports_csv_path)
    change_local_directory_permission(reports_csv_path)
    if test:
        collected_csv_path = os.path.join(reports_csv_path,
                                          f"system-info-collector-{timestamp}_collected_test.csv")
        errors_csv_path = os.path.join(reports_csv_path,
                                       f"system-info-collector-{timestamp}_errors_test.csv")
    else:
        collected_csv_path = os.path.join(reports_csv_path,
                                          f"system-info-collector-{timestamp}_collected.csv")
        errors_csv_path = os.path.join(reports_csv_path,
                                       f"system-info-collector-{timestamp}_errors.csv")
    collected_df.to_csv(collected_csv_path, index=False)
    errors_df.to_csv(errors_csv_path, index=False)
    logger.info(f"CSV reports created, path: {reports_csv_path}")
