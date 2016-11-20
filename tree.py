from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
from mininet.topo import Topo
import logging
import os


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        core = self.addSwitch('c1')
        aggregation = []
        edge = []
        host = []

        for i in xrange(1, fanout+1):
            agg = self.addSwitch('a'+str(i))
            self.addLink(
                core, agg, bw=linkopts1[0], delay=str(linkopts1[1])+'ms')
            aggregation.append(agg)

            for k in xrange(1, fanout+1):
                edge_no = k+(i-1)*fanout
                e_sw = self.addSwitch('e'+str(edge_no))
                self.addLink(
                    agg, e_sw, bw=linkopts2[0], delay=str(linkopts2[1])+'ms')
                edge.append(e_sw)

                for j in xrange(1, fanout+1):
                    host_no = (edge_no-1)*fanout+j
                    h = self.addHost('h'+str(host_no))
                    self.addLink(e_sw, h, bw=linkopts3[0], delay=str(linkopts3[1])+'ms')
                    host.append(h)

topos = {'custom': (lambda: CustomTopo())}


def createTopo():
    logging.debug("Create Topo")
    topo = CustomTopo(
        linkopts1=(10, 50), linkopts2=(5, 100),
        linkopts3=(1, 150), fanout=3)

    logging.debug("Start Mininet")
    CONTROLLER_IP = "127.0.0.1"
    CONTROLLER_PORT = 6633
    net = Mininet(topo=topo, link=TCLink, controller=None)
    net.addController(
        'controller', controller=RemoteController,
        ip=CONTROLLER_IP, port=CONTROLLER_PORT)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    if os.getuid() != 0:
        logger.debug("You are NOT root")
    elif os.getuid() == 0:
        createTopo()
