import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.connect('ssid', 'key')
wlan.isconnected()
wlan.ifconfig()
