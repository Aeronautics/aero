#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nickl-'

import sys
from .runner import run

if __name__ == '__main__':
    exit = run()
    if exit:
        sys.exit(exit)
