# Week 10 Tutorial – Security Project Progress Journal

## Objective

The objective of this tutorial was to continue progressing the security project by configuring communication between Ubuntu virtual machines, testing network connectivity, establishing client-server communication, configuring an Apache web server, and capturing network traffic using packet analysis tools. The tutorial focused on practical implementation of networking and cybersecurity concepts within Oracle VirtualBox.

---

# 1. Virtual Machine Network Configuration

Two Ubuntu virtual machines were configured in Oracle VirtualBox using a host-only network adapter to allow direct communication between both systems. The `ip addr` command was executed on each virtual machine to verify that both systems had been assigned valid IP addresses within the same subnet.

The following IP addresses were identified during the configuration process:

- Ubuntu VM 1: `192.168.56.103`
- Ubuntu VM 2: `192.168.56.104`

The successful assignment of different IP addresses confirmed that both virtual machines were correctly configured on the same internal network and were ready for communication testing.

## Screenshot
week10/images/Screenshot 2026-05-23 144129.png

---

# 2. Network Connectivity Testing Using Ping

After verifying the IP configuration, connectivity between the two virtual machines was tested using the `ping` command. This was performed to confirm that packets could successfully travel between both systems across the configured network.

The following command was executed from one virtual machine:

```bash
ping 192.168.56.104
```

Successful replies were received from the destination machine, confirming that communication between the two virtual machines was functioning correctly. The output also confirmed that there was no packet loss during transmission.

This test verified that the Oracle VirtualBox networking configuration had been successfully implemented.

## Screenshot
*(Insert Screenshot 1 – Successful ping communication between both virtual machines)*

---

# 3. TCP Communication Testing Using Netcat

Following successful network connectivity testing, Netcat (`nc`) was used to establish a simple TCP communication channel between the two Ubuntu virtual machines. This demonstrated that direct client-server communication could occur successfully across the network.

One virtual machine was configured as a listening server while the second virtual machine connected as a client.

The following commands were used during the test:

### Server Virtual Machine

```bash
nc -l -p 4444
```

### Client Virtual Machine

```bash
nc 192.168.56.104 4444
```

After establishing the connection, a test message was entered on the client virtual machine and was successfully displayed on the server virtual machine. This confirmed that data transfer between the two systems was operating correctly through TCP communication.

The successful Netcat test demonstrated that both systems were capable of exchanging network data reliably.

## Screenshot
*(Insert Screenshot 1 – Successful Netcat communication between both virtual machines)*

---

# 4. Apache Web Server Installation and Remote Access

An Apache2 web server was installed and configured on one of the Ubuntu virtual machines to simulate a basic client-server environment.

The following commands were used to install and start Apache2:

```bash
sudo apt update
sudo apt install apache2 -y
sudo systemctl start apache2
```

After installation, the web server was tested locally using:

```bash
curl localhost
```

Once local functionality was confirmed, the second virtual machine accessed the Apache web server remotely using the server IP address.

The following command was executed on the client virtual machine:

```bash
curl http://192.168.56.104
```

The Apache default webpage HTML source code was successfully returned on the client machine, confirming that the web server was operating correctly and could be accessed remotely across the configured network connection.

This demonstrated successful HTTP communication between the client and server virtual machines.

## Screenshot
*(Insert Screenshot 2 – Successful Apache web server communication between both virtual machines using curl)*

---

# 5. Packet Capture Using tcpdump

After confirming successful HTTP communication, network traffic generated during the web server communication was monitored and captured using `tcpdump`.

The following command was executed on the client virtual machine:

```bash
sudo tcpdump -i enp0s8 port 80 -w capture.pcap
```

This command configured tcpdump to listen for HTTP traffic on port 80 and save captured packets into a packet capture file named `capture.pcap`.

While packet capture was active, the Apache web server was accessed again using:

```bash
curl http://192.168.56.104
```

During execution, tcpdump displayed that it was listening on the specified network interface and monitoring network traffic. After stopping packet capture using `Ctrl + C`, tcpdump displayed packet statistics including packets captured, packets received by filter, and packets dropped by kernel.

This process demonstrated practical packet capture and traffic monitoring techniques commonly used in network security analysis and troubleshooting.

## Screenshot
*(Insert Screenshot 3 – tcpdump listening on interface and monitoring HTTP traffic)*

---

# 6. Verification of Packet Capture File

After packet capture was completed, the generated capture file was verified using the `ls -lh` command.

The following command was executed:

```bash
ls -lh
```

The output confirmed that the `capture.pcap` file had been successfully created and stored within the working directory. The file listing displayed the packet capture file along with file size and permissions.

This confirmed that network traffic had been successfully recorded for later packet analysis using tools such as Wireshark.

## Screenshot
*(Insert Screenshot 4 – Directory listing showing the generated `capture.pcap` file)*

---

# Conclusion

During this tutorial, two Ubuntu virtual machines were successfully configured and connected within Oracle VirtualBox using a host-only network. Network connectivity was verified using the `ping` command, while Netcat was used to establish TCP communication between both systems.

An Apache2 web server was then installed and accessed remotely using HTTP requests between the virtual machines. Finally, tcpdump was used to capture network traffic generated during the communication process, and the resulting packet capture file was successfully stored for future analysis.

Overall, the tutorial provided practical experience with virtual machine networking, client-server communication, web server configuration, and packet capture techniques relevant to cybersecurity and secure network communication.
