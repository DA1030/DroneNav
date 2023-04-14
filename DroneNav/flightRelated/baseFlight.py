from typing import Tuple
from cameraRelated.baseCamera import BaseCamera
from dronekit import Vehicle

class BaseFlight:

    vehicle: Vehicle = None
    cameraRelated: BaseCamera = None

    _targetPosition = (0.0, 0.0)
    _targetYaw      = 0.0

    def __init__(self, vehicle: Vehicle, camera: BaseCamera):
        self.vehicle = vehicle
        self.cameraRelated = camera

    def isActive(self) -> bool:
        return False

    def update(self) -> None:
        self._targetPosition = (0.0, 0.0)
        self._targetYaw = 0.0

    def reset(self) -> None:
        self._targetPosition = (0.0, 0.0)
        self._targetYaw = 0.0

    def getState(self) -> Tuple[Tuple[float, float], float]:
        return (self._targetPosition, self._targetYaw)

    def name(self) -> str:
        return 'base'