#!/usr/bin/env python3

import sys

import json
from dagshub import dagshub_logger


def calc_volume(radius: float, height: float) -> float:
    return 3.1415926 * radius * radius * height


input_file, output_file = sys.argv[1:]
with open(input_file) as f:
    param_dict = json.load(f)

volume = calc_volume(param_dict['radius'], param_dict['height'])

with dagshub_logger(metrics_path=output_file, should_log_hparams=False) as logger:
    logger.log_metrics({'volume': int(volume)}, step_num=1)
