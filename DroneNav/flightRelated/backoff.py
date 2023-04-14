from .baseFlight import BaseFlight
from parameters import BACKOFF_DISTANCE, MINIMUM_DISTANCE

class Backoff(BaseFlight):
    '''
    Rule to move back if the detection is too close
    '''

    def isActive(self):
        return self.cameraRelated.closestDetection() != None and \
            self.cameraRelated.closestDetection().z < BACKOFF_DISTANCE

    def update(self):
        detection = self.cameraRelated.closestDetection()
        if detection == None:
            return

        xDistance = detection.x
        zDistance = detection.z

        self._targetPosition = (zDistance - MINIMUM_DISTANCE, xDistance)

    def name(self) -> str:
        return 'backoff'
    