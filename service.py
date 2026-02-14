import ncs
from ncs.application import Service

class LoopbackService(Service):

    @Service.create
    def cb_create(self, tctx, root, service, proplist):

        device = root.devices.device[service.device]
        config = device.config

        intf = config.interface.Loopback.create(service.id)
        intf.ip.address.primary.address = service.ip_address
        intf.ip.address.primary.mask = "255.255.255.255"
