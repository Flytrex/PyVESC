from pyvesc.messages.base import VESCMessage
# python format codes are documented here: https://docs.python.org/2/library/struct.html
# protocol is doucmented here: http://vedder.se/2015/10/communicating-with-the-vesc-using-uart/

class GetVersions(metaclass=VESCMessage):
    """ Gets version fields
    """
    id = 0

    fields = [
            ('comm_fw_version', 'b'),
            ('fw_version_major', 'b'),
            ('fw_version_minor', 'b')
    ]

    def __str__(self):
            return f"versons:{self.comm_fw_version}.{self.fw_version_major}.{self.fw_version_minor}"


class GetValues(metaclass=VESCMessage):
    """ Gets internal sensor data
    """
    id = 4

    fields = [
                ('temp_fet', 'h', 10),
                ('temp_motor', 'h', 10),
                ('avg_motor_current', 'i', 100),
                ('avg_input_current', 'i', 100),
                ('avg_id', 'i', 100),
                ('avg_iq', 'i', 100),
                ('duty_cycle_now', 'h', 1000),
                ('rpm', 'i', 1),
                ('v_in', 'h', 10),
                ('amp_hours', 'i', 10000),
                ('amp_hours_charged', 'i', 10000),
                ('watt_hours', 'i', 10000),
                ('watt_hours_charged', 'i', 10000),
                ('tachometer', 'i', 1),
                ('tachometer_abs', 'i', 1),
                ('mc_fault_code', 'c'),
                ('pid_pos_now', 'i', 1000000),
                ('app_controller_id', 'c'),
                ('time_ms', 'i', 1),
        ]

    def __str__(self):
            return f"values:  rpm {self.rpm} time {self.time_ms} tacho {self.tachometer}"

class GetTelem(metaclass=VESCMessage):
    """ Gets internal sensor data
    """
    id = 40

    fields = [
                ('time_ms', 'i', 1),
                ('rpm', 'i', 1),
                ('tachometer', 'i', 1),
                ('avg_motor_current', 'i', 100),
                ('current_iterm', 'i', 100),
                ('current_cmd', 'i', 100),
                ('rpm_error', 'i', 1),
                ('mc_fault_code', 'c')
       ]

    def __str__(self):
            return f"values:  rpm {self.rpm} time {self.time_ms} tacho {self.tachometer}"

class GetRotorPosition(metaclass=VESCMessage):
    """ Gets rotor position data
    
    Must be set to DISP_POS_MODE_ENCODER or DISP_POS_MODE_PID_POS (Mode 3 or 
    Mode 4). This is set by SetRotorPositionMode (id=22).
    """
    id = 22

    fields = [
            ('rotor_pos', 'i', 100000)
    ]

    def __str__(self):
            return "rotor_pos:{}".format(self.rotor_pos)
