from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# Handle port status events
def _handle_PortStatus(event):
    port_no = event.ofp.desc.port_no
    reason = event.ofp.reason

    if reason == 0:
        log.info("Port %s ADDED", port_no)

    elif reason == 1:
        log.info("Port %s DELETED", port_no)

    elif reason == 2:
        log.warning("ALERT: Port %s MODIFIED (UP/DOWN)", port_no)


def launch():
    log.info("Port Monitoring Tool Started")

    # Listen for port status changes
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
