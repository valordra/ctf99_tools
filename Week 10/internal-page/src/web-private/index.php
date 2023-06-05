<?php
    $FLAG = "CSCE604258{REDACTED}";

    // https://www.php.net/manual/en/ref.network.php#121090
    function ipCIDRCheck ($IP, $CIDRS) {
        foreach ($CIDRS as $CIDR) {
            list ($net, $mask) = explode ('/', $CIDR);
            
            $ip_net = ip2long ($net);
            $ip_mask = ~((1 << (32 - $mask)) - 1);
        
            $ip_ip = ip2long ($IP);
        
            if (($ip_ip & $ip_mask) == ($ip_net & $ip_mask)) return true;
        }
        return false;
    }
    
    function getClientIP() {
        // redacted
        return "255.255.255.255";
    }

    $client_ip = getClientIP();
    $whitelist_range = array('127.0.0.1/32', '192.168.0.0/16', '172.0.0.0/24');
    if (ipCIDRCheck($client_ip, $whitelist_range)) {
        echo $FLAG;
    } else {
        echo "Your IP Address: ".$client_ip;
        echo "<br>Forbidden. The request is not coming from the internal.";
    }
?>