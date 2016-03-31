## Helpful links
You **MUST** go through 
https://docs.docker.com/engine/reference/builder/ and https://docs.docker.com/engine/reference/run/ at least twice!  
https://serversforhackers.com/getting-started-with-docker   
http://rominirani.com/2015/07/19/docker-tutorial-series/  


## Terminology

Container  
Like a hardware unit - analogous to your laptop, for e.g.  
A container is a stripped-to-basics version of a Linux operating system. 

Image  
Analogous to the OS that will run on your laptop (on the container)  
An image is software you load into a container.  


## Errors
1.  
    ```shell
    nik kvs$ sudo docker build -t nkini/kvs .
    W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/trusty-updates/main/binary-amd64/Packages  Hash Sum mismatch
    E: Some index files failed to download. They have been ignored, or old ones used instead.
    ```

    Solution:
    Made the error go away by commenting the following line in the Docker file
    RUN         apt-get update && apt-get install -y python3
    However, I did not ever see the error again after that, even with the line above uncommented.

2.  
    ```shell
    Dockerfile:    
    .  
    .  
    CMD ["cd","/root/webapp"]  
    CMD ["python3", "-m", "http.server"]  
    .  
    .  
    ```
    The result of 
    ```shell
    nik kvs$ curl -i localhost:49160
    ```
    shows that httpserver is running at / and NOT at /root/webapp.  

    Solution:
    This just means that I haven't read the docs. https://docs.docker.com/engine/reference/builder/#cmd  
    *"There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect."*  
    Write multiple shell commands as 
    ```shell
    CMD     cd /root/webapp; python3 app.py
    ```
    or better still, put them in a shell script file and run the script.

3. 
    ```shell
    nik kvs$ cat Dockerfile 
    .
    .
    .
    RUN cd /root/webapp; python3 -m http.server;

    nik kvs$ sudo docker build -t nkini/kvs .
    .
    .
    .
    Removing intermediate container e6d7aca4930a
    Step 5 : RUN cd /root/webapp; python3 -m http.server
     ---> Running in 4a1079fd7173
     #JUST HANGS HERE
    ```
    Solution:  
    I can't quite put a finger on exactly why, but you can't have your last command in the Dockerfile be a RUN like the one here. It needs to be a CMD.
    ```shell
    .
    .
    .
    CMD cd /root/webapp; python3 -m http.server;
    ```
    Do read https://docs.docker.com/engine/reference/builder/#run and https://docs.docker.com/engine/reference/builder/#cmd once more.

4. 
    ```shell
    nik kvs$ sudo docker run -d -p 49160:8080 nkini/kvs
    nik kvs$ curl -i localhost:49160
    curl: (56) Recv failure: Connection reset by peer
    ```
    Solution:  
    If your app 127.0.0.1 or 0.0.0.0? Changing the host of the app running in the Docker container to 0.0.0.0 (from what was initially 127.0.0.1) fixed this error for me.
