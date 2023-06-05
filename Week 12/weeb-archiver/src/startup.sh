#!/usr/bin/env sh
start_services() {
    redis-server --daemonize yes
    DBCON=$(timeout 3 curl -v telnet://localhost:6379 2>&1 | grep "Connected to")
    while [ "${DBCON}" = "" ]
    do
        echo $DBCON
        echo "[-] Failed to connect database"
        echo "[*] Retrying in 5 seconds\n"
        sleep 5
        
        DBCON=$(timeout 3 curl -v telnet://localhost:6379 2>&1 | grep "Connected to")
    done
    echo "[+] Connected to the database"

    /usr/local/tomcat/bin/catalina.sh run
}

stop_services() {
    /usr/local/tomcat/bin/shutdown.sh
    redis-cli shutdown
}

start_services
