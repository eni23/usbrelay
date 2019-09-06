SERIAL_DEVICE		= /dev/ttyACM*

all:
	platformio -f -c vim run

upload: monitor-close
	platformio -f -c vim run --target upload -v

clean:
	platformio -f -c vim run --target clean

update:
	platformio -f -c vim update

find-serial:
	ls -1 $(SERIAL_DEVICE)
	$(eval USBTTY=$(shell tools/find-serial.py ))

monitor: find-serial
	tools/monitor.sh open $(USBTTY) 0

monitor-close:
	tools/monitor.sh close

monitor-loop: find-monitor-baud find-serial
	-tools/monitor.sh loop $(USBTTY) $(MONITOR_BAUD)

monitor-notify-done:
	tools/monitor.sh notify-done
