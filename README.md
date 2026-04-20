
#  Port Status Monitoring Tool using SDN

##Project Overview

This project implements a **Software Defined Networking (SDN)** solution to monitor switch port status changes.
The controller detects when a port goes **UP or DOWN**, logs the change, and generates an **alert message**.

---

##  Objectives

* Detect port status changes (UP/DOWN)
* Log changes in the controller
* Generate alert messages
* Observe network behavior during failure and recovery

---

##  Tools & Technologies

* **Mininet** – Network simulation
* **POX Controller** – SDN controller
* **OpenFlow Protocol** – Communication between switch and controller
* **Ubuntu (VirtualBox)** – Environment

---

##  Network Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)
* All hosts connected to a single switch

---

##  Setup & Execution

### 1️ Start Controller

```bash
cd ~/pox
./pox.py openflow.of_01 forwarding.l2_learning misc.port_monitor
```

### 2️ Start Mininet

```bash
sudo mn -c
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

---

##  Test Scenarios

###  Test Case 1: Normal Operation

```bash
pingall
```

**Output:** 0% packet loss
✔ All hosts communicate successfully

---

###  Test Case 2: Port Failure

```bash
link s1 h1 down
```

* Packet loss observed
* Communication failure

**Controller Output:**

```
ALERT: Port X MODIFIED (UP/DOWN)
```

---

###  Test Case 3: Recovery

```bash
link s1 h1 up
pingall
```

**Output:** 0% packet loss
✔ Network restored

---

##  Performance Analysis

* Latency measured using:

```bash
h1 ping h2
```

* Observed delay variation before and after failure

---

##  Screenshots

* Controller running
  <img width="812" height="193" alt="Screenshot from 2026-04-18 12-19-47" src="https://github.com/user-attachments/assets/9fc4e478-fa02-4daa-a913-fdbe594f9a52" />

* Topology creation
  <img width="901" height="324" alt="Screenshot from 2026-04-18 12-20-59" src="https://github.com/user-attachments/assets/fc87cb80-bcca-457b-89eb-e0c78de0b6f5" />

* Successful ping (0% loss)
* <img width="377" height="158" alt="Screenshot from 2026-04-18 12-25-37" src="https://github.com/user-attachments/assets/e8da746b-9cf0-4219-81fd-cb66e49706a7" />

* Port down command
* <img width="363" height="26" alt="Screenshot from 2026-04-18 12-22-52" src="https://github.com/user-attachments/assets/a4f48a60-bf80-40d4-82c0-adb75efa9501" />

* Alert message (MOST IMPORTANT)
* <img width="558" height="59" alt="Screenshot from 2026-04-18 12-22-27" src="https://github.com/user-attachments/assets/21147c09-1244-4fa5-9196-49d6121e633c" />

* Packet loss after failure
* <img width="377" height="140" alt="Screenshot from 2026-04-18 12-24-53" src="https://github.com/user-attachments/assets/803dd362-6626-4218-a204-c3c3bf4f89b7" />

* Network recovery
* <img width="377" height="158" alt="Screenshot from 2026-04-18 12-25-37" src="https://github.com/user-attachments/assets/03f09a27-0076-49e3-9a4f-1d168d4a987f" />

* Latency output
<img width="624" height="526" alt="Screenshot from 2026-04-18 12-26-34" src="https://github.com/user-attachments/assets/869bb928-7c64-4af0-87c6-e8be6065c18c" />


* 

---

##  Key Concepts

* **SDN (Software Defined Networking):** Separation of control plane and data plane
* **OpenFlow:** Protocol used between controller and switch
* **PortStatus Event:** Detects changes in port state

---

##  Conclusion

This project successfully demonstrates how an SDN controller can monitor network ports, detect failures, and generate alerts in real-time. It also shows how network behavior changes during failures and recovers after restoration.

---

## 👨‍💻 Author

Amar Nawadagi
