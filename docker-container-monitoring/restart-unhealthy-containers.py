import docker
import logging
import time

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
client = docker.from_env()
timerRestarted = 60
timerOK = 30

while True:
    restartStatus = False
    list = client.containers.list()
    for container in list:
        if container.attrs['State']['Health']['Status'] == 'unhealthy' or container.attrs['State']['Health']['Status'] == 'exited':
            logging.error("Found container in unhealthy state! Container: %s has status: %s", container.name, container.attrs['State']['Health']['Status'])
            try:
                container.restart()
                logging.info("Restarted container: %s",container.name)
                restartStatus = True
            except:
                logging.fatal("Container restart command failed!")
        logging.debug('%s - %s', container.name, container.attrs['State']['Health']['Status'])
    if restartStatus == True:
        time.sleep(timerRestarted)
    elif restartStatus == False:
        logging.info("All containers are in healthy state!")
        time.sleep(timerOK)
