#!/usr/bin/env python3
# -*- coding: utf8 -*-
import yaml
import os

YAML_INPUT = "yml-reader-config.yml"

with open(YAML_INPUT, "r") as f:
    y=yaml.safe_load(f)
    for v in y:
        print("{}:  {}".format(v,y[v]))
        for v2 in y[v]:
            print("{}".format(v2))
            print("-----")
            for v3 in y[v][v2]:
                print("    {}".format(v3))
        print("=====")
