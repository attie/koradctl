from time import sleep

class TestSuite:
    # connect a 2.5 Ohm load to the output
    TEST_LOAD = 2.5

    # use 3.3v for testing
    TEST_VOLTAGE = 3.3

    # the test's ideal current (i.e: no current limit / protection)
    TEST_CURRENT_IDEAL = TEST_VOLTAGE / TEST_LOAD

    # the low test current (i.e: current limit / protection should operate)
    TEST_CURRENT_LO = TEST_CURRENT_IDEAL * 0.9
    TEST_CURRENT_LO_VOLTAGE = TEST_CURRENT_LO * TEST_LOAD

    # the high test current (i.e: current limit / protection should not operate)
    TEST_CURRENT_HI = TEST_CURRENT_IDEAL * 1.1
    TEST_CURRENT_HI_VOLTAGE = TEST_VOLTAGE

    # the expected voltage tolerance
    TEST_VOLTAGE_TOLERANCE = 0.05 # +/- 5%
    TEST_VOLTAGE_TOLERANCE_DN = 1 - TEST_VOLTAGE_TOLERANCE
    TEST_VOLTAGE_TOLERANCE_UP = 1 + TEST_VOLTAGE_TOLERANCE

    # the expected current tolerance
    TEST_CURRENT_TOLERANCE = 0.05 # +/- 5%
    TEST_CURRENT_TOLERANCE_DN = 1 - TEST_CURRENT_TOLERANCE
    TEST_CURRENT_TOLERANCE_UP = 1 + TEST_CURRENT_TOLERANCE

    def __init__(self, psu):
        self.psu = psu

    def check_vi_in_range(self, v, i):
        v_live = self.psu.get_output_voltage()
        assert(v_live.value > (v * self.TEST_VOLTAGE_TOLERANCE_DN))
        assert(v_live.value < (v * self.TEST_VOLTAGE_TOLERANCE_UP))

        i_live = self.psu.get_output_current()
        assert(i_live.value > (i * self.TEST_CURRENT_TOLERANCE_DN))
        assert(i_live.value < (i * self.TEST_CURRENT_TOLERANCE_UP))
    
    def run(self, allow_untested: bool = False):
        try:
            self._run(allow_untested)
        except:
            self.psu.set_output_state(False)
            raise

    def _run(self, allow_untested: bool = False):
        print("--- get the supply's identity")
        print(self.psu.get_identity())
        if not allow_untested:
            assert(self.psu.is_tested())

        print('--- disable output')
        self.psu.set_output_state(False)
        assert(self.psu.get_output_state() == False)

        print('--- setup output voltage = %2.2f V' % ( self.TEST_VOLTAGE ))
        self.psu.set_voltage_setpoint(self.TEST_VOLTAGE)
        assert(self.psu.get_voltage_setpoint().value == self.TEST_VOLTAGE)

        print('--- setup output current (high) = %1.3f A' % ( self.TEST_CURRENT_HI ))
        self.psu.set_current_setpoint(self.TEST_CURRENT_HI)
        assert(self.psu.get_current_setpoint().value == self.TEST_CURRENT_HI)

        print('--- enable neither OVP or OCP')
        self.psu.set_ovp_state(False)
        self.psu.set_ocp_state(False)
        assert(self.psu.get_status().ovp_ocp_enabled == False)
        self.psu.set_output_state(True)
        sleep(1)
        assert(self.psu.get_output_state() == True)
        self.check_vi_in_range(self.TEST_CURRENT_HI_VOLTAGE, self.TEST_CURRENT_IDEAL)
        self.psu.set_output_state(False)

        print('--- setup output current (low) = %1.3f A' % ( self.TEST_CURRENT_LO ))
        self.psu.set_current_setpoint(self.TEST_CURRENT_LO)
        assert(self.psu.get_current_setpoint().value == self.TEST_CURRENT_LO)

        print('--- enable neither OVP or OCP')
        self.psu.set_ovp_state(False)
        self.psu.set_ocp_state(False)
        assert(self.psu.get_status().ovp_ocp_enabled == False)
        self.psu.set_output_state(True)
        sleep(1)
        assert(self.psu.get_output_state() == True)
        self.check_vi_in_range(self.TEST_CURRENT_LO_VOLTAGE, self.TEST_CURRENT_LO)
        self.psu.set_output_state(False)

        print('--- enable OVP')
        self.psu.set_ovp_state(True)
        self.psu.set_ocp_state(False)
        assert(self.psu.get_status().ovp_ocp_enabled == True)
        self.psu.set_output_state(True)
        sleep(1)
        assert(self.psu.get_output_state() == True)
        self.check_vi_in_range(self.TEST_CURRENT_LO_VOLTAGE, self.TEST_CURRENT_LO)
        self.psu.set_output_state(False)

        print('--- enable OCP')
        self.psu.set_ovp_state(False)
        self.psu.set_ocp_state(True)
        assert(self.psu.get_status().ovp_ocp_enabled == True)
        self.psu.set_output_state(True)
        sleep(1)
        assert(self.psu.get_output_state() == False)
        assert(self.psu.get_output_voltage().value == 0)
        assert(self.psu.get_output_current().value == 0)

        print('--- enable both')
        self.psu.set_ovp_state(True)
        self.psu.set_ocp_state(True)
        assert(self.psu.get_status().ovp_ocp_enabled == True)
        self.psu.set_output_state(True)
        sleep(1)
        assert(self.psu.get_output_state() == False)
        assert(self.psu.get_output_voltage().value == 0)
        assert(self.psu.get_output_current().value == 0)
