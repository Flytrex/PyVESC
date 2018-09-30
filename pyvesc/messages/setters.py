from pyvesc.messages.base import VESCMessage


class JumpToBootLoader(metaclass=VESCMessage):
    """ COMM_JUMP_TO_BOOTLOADER
    
    """
    id = 1
    fields = [
    ]

class TerminalCommand(metaclass=VESCMessage):
    """ 
    :ivar command: Terminal command to send
    """
    id = 20

    fields = [
        ('command', 's')
    ]

class PrintedMessage(metaclass=VESCMessage):
    """ 
    """
    id = 21

    fields = [
        ('text', 's')
    ]

    def __str__(self):
            return "message:{}".format(self.text)

class SetDutyCycle(metaclass=VESCMessage):
    """ Set the duty cycle.

    :ivar duty_cycle: Value of duty cycle to be set (range [-1e5, 1e5]).
    """
    id = 5
    fields = [
        ('duty_cycle', 'i', 100000.0)
    ]


class SetRPM(metaclass=VESCMessage):
    """ Set the RPM.

    :ivar rpm: Value to set the RPM to.
    """
    id = 8
    fields = [
        ('rpm', 'i', 1.0)
    ]


class SetCurrent(metaclass=VESCMessage):
    """ Set the current (in amps) to the motor.

    :ivar current: Value to set the current to (in amps).
    """
    id = 6
    fields = [
        ('current', 'i', 1000.0)
    ]


class SetCurrentBrake(metaclass=VESCMessage):
    """ Set the current brake (in amps).

    :ivar current_brake: Value to set the current brake to (in amps).
    """
    id = 7
    fields = [
        ('current_brake', 'i', 1000.0)
    ]

class SetPosition(metaclass=VESCMessage):
    """Set the rotor angle based off of an encoder or sensor
    
    :ivar pos: Value to set the current position or angle to.
    """
    id = 9
    fields = [
        ('pos', 'i', 1000000)
    ]

class SetRotorPositionMode(metaclass=VESCMessage):
    """Sets the rotor position feedback mode.
        
    It is reccomended to use the defined modes as below:
        * DISP_POS_OFF
        * DISP_POS_MODE_ENCODER
        * DISP_POS_MODE_PID_POS
        * DISP_POS_MODE_PID_POS_ERROR
    
    :ivar pos_mode: Value of the mode
    """

    DISP_POS_OFF = 0
    DISP_POS_MODE_ENCODER = 3
    DISP_POS_MODE_PID_POS = 4
    DISP_POS_MODE_PID_POS_ERROR = 5

    id = 10
    fields = [
        ('pos_mode', 'b')
    ]


class SetCurrentLimit(metaclass=VESCMessage):
    """ Set the current (in amps) to the motor.

    :ivar current: Value to set the current limit to (in amps).
    """
    id = 38
    fields = [
        ('current_limit', 'i', 1000.0)
    ]
