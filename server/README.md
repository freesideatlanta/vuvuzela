hardware:
- rack server

software:
- linux (ubuntu)
- vuvuzela service

generator script:
- runs as vuvuzela user
- cron runs daily at 1a
- for each node in query(mysql.node)
  - query to produce acl for each relay number
  - generate `/srv/vuvuzela/<hostname>-<relayid>.db` (overwrite)

loggregator script:
- runs as vuvuzela user
- cron runs daily at 6a
- for each `<hostname>-<relayid>.db` in `/var/log/vuvuzela/.`
  - query(sqlite.log) and append rows to mysql.log
