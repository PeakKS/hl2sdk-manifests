import os
import json

outfile = 'manifests/meson.build'
global_config = {}

if os.path.isfile(outfile):
    os.remove(outfile)

for file in os.listdir('manifests'):
  manifest = os.path.join('manifests', file)
  with open(manifest, 'rt') as fp:
    config = json.load(fp)
    name = config.pop('name', None)
    global_config[name] = config

global_config_string = json.dumps(global_config, indent = 2)
manifests_string = global_config_string.replace('"', '\'')

with open(outfile, 'w') as out:
    print('manifests = ', end = '', file = out)
    print(manifests_string, end = '', file = out)
