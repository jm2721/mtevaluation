#!/bin/sh

./evaluate -s 1 > output
./compare-with-human-evaluation < output
