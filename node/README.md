hardware:
- raspi
- 4GB SD card
- USB wifi card
- relay (x4) shield
- RFID reader

software:
- linux (debian wheezy)
- vuvuzela service
- access control list (ACL) pull

vuvuzelad service:
- runs as vuvuzela user
- listens for RFID swipe
  - examine Pi4J, way to communicate with serial interface on Raspi: http://pi4j.com/example/serial.html
- on RFID swipe (8-char string), query SQLite access table
- if 'tokenid' exists, then grant relay 'number' in matching row
  - record granted = true in log
- else deny
  - record granted = false in log

aclpull script:
- runs as vuvuzela user
- cron runs daily at 4a
    scp <server>:/srv/<hostname>.db /var/vuvuzela/.
    scp /var/log/vuvuzela/log.db <server>:/var/log/vuvuzela/<hostname>-log.db
