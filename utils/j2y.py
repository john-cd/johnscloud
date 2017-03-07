#!/usr/bin/env python
import yaml
import json
import click
import os
import glob
import collections

@click.command()
@click.argument('json_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True))
def main(json_dir):
        for json_file in glob.iglob(os.path.join(json_dir, "*.template")):  #[ os.path.join(path, fn) for fn in next(os.walk(path))[2]]:
            yaml_file = os.path.splitext(json_file)[0] + ".cf.yml"
            print("{0} --> {1}".format(json_file, yaml_file))
            with open(json_file, 'r') as json_fp:
                with open(yaml_file, 'w') as yaml_fp:
                    json_data = json.load(json_fp, object_pairs_hook=OrderedDict)
                    yaml.safe_dump(json_data, yaml_fp, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
    main()