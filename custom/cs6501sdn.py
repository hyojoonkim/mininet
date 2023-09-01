"""Custom topology example
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, RemoteController, OVSSwitch, Ryu
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI

class SdnTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        s1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( h1, s1)
        self.addLink( h2, s1)
        self.addLink( h3, s1)
        self.addLink( h4, s1)
        self.addLink( h5, s1)
        self.addLink( h6, s1)
    

def a1():
    topo=SdnTopo()
    net = Mininet(topo=topo,switch=OVSSwitch,
                  controller=RemoteController('c0',ip='127.0.0.1'),
                  autoSetMacs=True, autoStaticArp=True,
                  link=TCLink)

    for h in net.hosts:
        h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    for sw in net.switches:
        sw.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    net.start()
    CLI(net)
    net.stop


if __name__ == '__main__':
    setLogLevel('info')
    a1()


#topos = { 'sdntopo': ( lambda: SdnTopo() ) }
