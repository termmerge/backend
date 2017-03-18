#!/bin/bash

set -e

# Install app dependencies
pip install -r /termmerge/requirements.txt

# Run Flask Server
exec flask run --host=0.0.0.0
