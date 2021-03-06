For the 3rd and final assignment, you will implement a fault-tolerant distributed key value store, in a CAP trade-off design space. We will inject faults in the system by crashing nodes, increase the system load to capacity, introduce network delays etc., and test for consistency and availability in spite of such faults, or in the presence of such loads.

### Due Date:  
Soft deadline: June 5th, 2016. 11:59pm.  
Hard deadline: June 10th, 2016. 11:59pm.  
No penalties for submitting after the soft deadline but before the hard deadline. Submissions after the hard deadline will not be graded.  

### Design space:
Implement a C+P or an A+P KVS. Sure, if you feel particularly bold and rebellious, attempt C+A+P. Note that the P (partition tolerance) is mandatory. Introduce fault tolerance through a replication scheme. You can choose any scheme discussed in class, or even one of your own. The scheme of grading will differ depending on your design choice.

Please submit a design document as part of your submission explaining your design, the reasons for your choices, and how you would expect your system to perform under different scenarios - network partition, node failure, heavy load etc.

### Instructions
We will keep updating the spec to add more information, but at the moment, we are giving you the bare minimum that you need to get started, because we do want you to get started.

Once again, you will use a docker container to submit the assignment. What is different this time is that to test a single submission, we will spin up multiple instances of your container. That is, the distributed nodes are the multiple instances of your docker container. You may choose any replication scheme that best fits your trade-off decisions. In this first iteration of the spec, we show what interfaces in Docker are available to make node discovery possible in the network of distributed Docker containers.

We will set the following ENV variables when running your docker instances:  
IP -- the externally-visible ip to which your instance should bind  
PORT -- the port to which your instance should bind  
MEMBERS -- a comma-separated list of IP:PORT pairs representing the other nodes in the system  

More information about environment variables can be found here: 
https://docs.docker.com/engine/reference/run/#env-environment-variables

We will spin up exactly 5 instances of your docker container. The ENV variables for the first instance will look exactly like this:  
IP=10.0.0.20  
PORT=12345  
MEMBERS=10.0.0.20:12345,10.0.0.21:12346,10.0.0.22:12347,10.0.0.23:12348,10.0.0.24:12349  

Also, in this example, you would bind to the IP 10.0.0.20 and PORT 12345, and not localhost and 8080.

To summarize, your 5 nodes will have IP address assignment from 10.0.0.20 to 10.0.0.24, and each node will have its IP address in the IP environment variable. Each of these 5 nodes will have port assignments from 12345 to 12349, and each node will have its port assignment in the PORT environment variable. The MEMBERS environment variable has the same value for all 5 nodes and will look exactly as above.

Here's a list of functionalities expected from your system:   
1. In the case of no faults, all functional guarantees from HW1 and HW2 should hold.  
2. In the case of no faults, every node should be able to receive a R/W request and provide a valid response.    
3. Assuming no failures 1, 2 hold regardless of your design choice. The system must also be robust to the failure of any node. When failure occurs, your choice of C/A/P will dictate the appropriate behavior.  
4. Specific requirements for resistance to failure will be added to this spec. But here are some to begin with:
  * The system must return valid results in the presence high concurrency, with reads and writes issued to multiple nodes
  * The system should be robust to faults such as node crashes, and network delays/partitioning.
  * For example, in the event of a severe network delays
    * An A+P system must continue operating, even if this means returning stale data. 
    * A C+P system must return consistent answers, even if this means blocking for the duration of the delay.  
  * Availability will receive bonus points on a CP system. Consistency will receive bonus points on an AP system.  
5. AP systems are expected to be Eventually Consistent.
6. A CP system that stops responding in the face of node failure is still CP. However, CP systems are expected to implement some sophisticated scheme to allow for responses in spite of node failure.

Notes about how we run the system:  
1. We will spawn exactly 5 docker containers. The environment variables will contain information about all of them when each node comes up.  
2. Nodes will crash, but crashed nodes will not be restarted.  
3. Reads and writes can be issued to any node using HTTP, in the same way as assignment 2, and the same responses are expected.
