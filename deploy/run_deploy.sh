#!/bin/bash -

cmd='ansible-playbook -i ansible_hosts deploy.yml'
echo 'Running command: '
echo "$cmd"
$cmd
