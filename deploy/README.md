# Deploy Guten Better

## setup

Install Ansible Galaxy.

Install the redis ansible [role](https://github.com/DavidWittman/ansible-redis) from the Galaxy:

```
ansible-galaxy install DavidWittman.redis
```

Deploy uses ansible

ansible-playbook -i ansible_hosts setup.yml
ansible-playbook -i ansible_hosts deploy.yml
