# NSO Loopback Service

Example Cisco NSO 6.4.x service package created using ncs-make-package.

ncs-make-package loopback-service \
    --service-skeleton python-and-template \
    --dest packages

## Features

- Custom YANG model
- Python service implementation
- Unit testing (pytest)
- Robot Framework integration test
- CI ready

## Use Case

Demonstrates service lifecycle development workflow:

Model → Service Logic → Test → Deploy
