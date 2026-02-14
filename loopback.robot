*** Settings ***
Library    Process

*** Test Cases ***
Create Loopback Service
    Run Process    ncs_cli -u admin -C "config"
    Run Process    ncs_cli -u admin -C "set loopback-service loopback test1 device ios1 id 100 ip-address 10.10.10.1"
    Run Process    ncs_cli -u admin -C "commit"
    Run Process    ncs_cli -u admin -C "show configuration devices device ios1 config interface Loopback100"
