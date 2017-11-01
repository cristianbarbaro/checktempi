from gpiozero import CPUTemperature
import config
import subprocess
import logging


def get_gpu_temp():
    """Return GPU temperature"""
    command = "/opt/vc/bin/vcgencmd measure_temp"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output.decode(encoding='UTF-8').replace("temp=", "").replace("\n","")


fmt = "%(asctime)s: %(levelname)s: %(message)s"
logging.basicConfig(format=fmt, datefmt='%Y/%m/%d %H:%M:%S', filename=config.log_file, level=logging.INFO)

# Show CPU temperature: 
cpu = CPUTemperature()
cpu_temp = cpu.temperature

# Show GPU temperature:
gpu_temp = get_gpu_temp()

if cpu_temp >= config.max_temp:
    # Logging warning and executing command
    logging.warning("CPUTemp=%s'C", str(cpu_temp))
    logging.warning("GPUTemp=%s", gpu_temp)
    process = subprocess.Popen(config.command.split(), stdout=subprocess.PIPE)
    #output = process.communicate()[0]
    #print(output)
else:
    # Logging info
    logging.info("CPUTemp:=%s'C", str(cpu_temp))
    logging.info("GPUTemp:=%s", gpu_temp)
    
exit(0)
