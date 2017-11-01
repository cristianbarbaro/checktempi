### CheckTemPi

#### Check CPU temperature and execute a command.

* Clone this project in cron.d folder as root user:
	* git clone https://github.com/cristianbarbaro/checktempi.git /etc/cron.d/checktempi/

* Move config-example to config and edit your variables.
	* `cd /etc/cron.d/checktempi/`
	* `mv config-example.py config.py`

* Open crontab as root user:
	* `crontab -e`

* Add next line:
	* `*/5 * * * * python3 /etc/cron.d/checktempi/checktempi.py`
	
