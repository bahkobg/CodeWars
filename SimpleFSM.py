class Automaton(object):

    def __init__(self):
        self.state = 'CLOSED'
        self.transitions = [{'state': 'CLOSED', 'value': 'APP_PASSIVE_OPEN', 'target': 'LISTEN'},
                            {'state': 'CLOSED', 'value': 'APP_ACTIVE_OPEN', 'target': 'SYN_SENT'},
                            {'state': 'LISTEN', 'value': 'RCV_SYN', 'target': 'SYN_RCVD'},
                            {'state': 'LISTEN', 'value': 'APP_SEND', 'target': 'SYN_SENT'},
                            {'state': 'LISTEN', 'value': 'APP_CLOSE', 'target': 'CLOSED'},
                            {'state': 'SYN_RCVD', 'value': 'APP_CLOSE', 'target': 'FIN_WAIT_1'},
                            {'state': 'SYN_RCVD', 'value': 'RCV_ACK', 'target': 'ESTABLISHED'},
                            {'state': 'SYN_SENT', 'value': 'RCV_SYN', 'target': 'SYN_RCVD'},
                            {'state': 'SYN_SENT', 'value': 'RCV_SYN_ACK', 'target': 'ESTABLISHED'},
                            {'state': 'SYN_SENT', 'value': 'APP_CLOSE', 'target': 'CLOSED'},
                            {'state': 'ESTABLISHED', 'value': 'APP_CLOSE', 'target': 'FIN_WAIT_1'},
                            {'state': 'ESTABLISHED', 'value': 'RCV_FIN', 'target': 'CLOSE_WAIT'},
                            {'state': 'FIN_WAIT_1', 'value': 'RCV_FIN', 'target': 'CLOSING'},
                            {'state': 'FIN_WAIT_1', 'value': 'RCV_FIN_ACK', 'target': 'TIME_WAIT'},
                            {'state': 'FIN_WAIT_1', 'value': 'RCV_ACK', 'target': 'FIN_WAIT_2'},
                            {'state': 'CLOSING', 'value': 'RCV_ACK', 'target': 'TIME_WAIT'},
                            {'state': 'FIN_WAIT_2', 'value': 'RCV_FIN', 'target': 'TIME_WAIT'},
                            {'state': 'TIME_WAIT', 'value': 'APP_TIMEOUT', 'target': 'CLOSED'},
                            {'state': 'CLOSE_WAIT', 'value': 'APP_CLOSE', 'target': 'LAST_ACK'},
                            {'state': 'LAST_ACK', 'value': 'RCV_ACK', 'target': 'CLOSED'}
                            ]

    def read_commands(self, commands):
        for c in commands:
            for t in self.transitions:
                if t['state'] == self.state and t['value'] == c:
                    self.state = t['target']
                    break
            else:
                return 'ERROR'
        return self.state


my_automaton = Automaton()
print(my_automaton.read_commands(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]))
# Do anything necessary to set up your automaton's states, q1, q2, and q3.
