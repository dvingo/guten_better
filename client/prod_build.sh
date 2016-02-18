#!/bin/bash -

cmd='webpack --config webpack.prod.config.js --progress'
echo $cmd
$cmd

hash=$(shasum dist/bundle.js | head -c 10)

cmd="cp dist/bundle.js dist/${hash}_bundle.js"
echo $cmd
$cmd
