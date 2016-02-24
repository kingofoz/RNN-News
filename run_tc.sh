#!/usr/bin/env bash

export PYTHONPATH=$PYTHONPATH:./core/

python services/tweet_collector_service.py
