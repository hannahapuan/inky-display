#!/bin/bash

# Processor Throttling - only use if you've got performance headroom!
#echo "arm_freq_min=250" >> /boot/config.txt
#echo "core_freq_min=100" >> /boot/config.txt
#echo "sdram_freq_min=150" >> /boot/config.txt
#echo "over_voltage_min=0" >> /boot/config.txt

# Disable boot splash screen
echo "disable_splash=1" >> /boot/config.txt

# Disable bluetooth
echo "dtoverlay=pi3-disable-bt" >> /boot/config.txt

# Disable on board LEDs
echo "dtparam=act_led_trigger=none" >> /boot/config.txt
echo "dtparam=act_led_activelow=on" >> /boot/config.txt

# Reduce pre-built boot delay
echo "boot_delay=0" >> /boot/config.txt

# Improve SD Card life
sudo bash -c 'echo $(cat /boot/cmdline.txt) "fastboot noswap ro" > /boot/cmdline.txt'

# Disable unused system services
sudo systemctl disable dphys-swapfile.service
sudo systemctl disable keyboard-setup.service
sudo systemctl disable apt-daily.service
sudo systemctl disable raspi-config.service
sudo systemctl disable triggerhappy.service
sudo systemctl disable avahi-daemon.service

# sudo apt-get remove --purge wolfram-engine triggerhappy anacron logrotate dphys-swapfile -y

# Disable Logging Services
sudo systemctl disable bootlogs
sudo systemctl disable console-setup

# Replace Logs with Busybox in memory logger
sudo apt-get install busybox-syslogd -y
sudo dpkg --purge rsyslog
sudo apt autoremove -y

# Disable USB ports
echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind &

# Turn off HDMI
sudo /opt/vc/bin/tvservice -o

