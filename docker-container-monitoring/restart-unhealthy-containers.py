import docker
import logging
import time

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
client = docker.from_env()
timerRestarted = 300
timerOK = 30
restartedContainers = []

while True:
    restartStatus = False
    list = client.containers.list()
# Loop trough the list of containers
    for container in list:
# Check if the container was restarted previously and is now healthy, log if recovered
        if container.short_id in restartedContainers and container.attrs['State']['Health']['Status'] == 'healthy':
            logging.info("Container %s has recovered and is now healthy!", container.name)
            restartedContainers.remove(container.short_id)
# Check weather the container is in unhealthy status
        elif container.attrs['State']['Health']['Status'] == 'unhealthy' or container.attrs['State']['Health']['Status'] == 'exited':
            logging.error("Found container in unhealthy state! Container: %s has status: %s", container.name, container.attrs['State']['Health']['Status'])
            try:
                container.restart()
                logging.info("Restarted container: %s",container.name)
                restartStatus = True
                if container.short_id not in restartedContainers:
                    restartedContainers.append(container.short_id)
            except:
                logging.fatal("Container restart command failed!")
        logging.debug('%s - %s', container.name, container.attrs['State']['Health']['Status'])

    if restartStatus == True:
        time.sleep(timerRestarted)
    elif restartStatus == False:
        logging.info("All containers are in healthy state!")
        time.sleep(timerOK)
