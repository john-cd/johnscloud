#!/usr/bin/env python

import yaml
import json
import click
import sys

@click.command()
@click.argument('json_fp', type=click.File('r'))
@click.argument('yaml_fp', type=click.File('w'))
def main(json_fp, yaml_fp):
        json_data = json.load(json_fp)
        yaml.safe_dump(json_data, yaml_fp, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
    main()