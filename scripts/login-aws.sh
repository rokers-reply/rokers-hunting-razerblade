#!/bin/bash

KEYFILE="$HOME/Downloads/rokers-reply.pem"

chmod 400 "$KEYFILE"
ssh -i "$KEYFILE" ubuntu@ec2-34-245-235-123.eu-west-1.compute.amazonaws.com
