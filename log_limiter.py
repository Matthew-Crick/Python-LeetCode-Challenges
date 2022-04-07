import unittest


class Logger:
    """ Logger class """

    def __init__(self) -> None:
        """ initialise the instance variables """
        self.map = {}
        self.time = []
        self.msg = []
        self.output = []

    def assess_message(self, lst: list) -> list:
        """ Main caller partitions list for aux method; utilises aux method to solve.
        :input: timestamp: lst: original input list containing lists of both message and time elements
        :return: list of booleans
        :pre-condition: 0 <= timestamp <= 109.  timestamp passed in chronological order.
        1 <= message.length <= 30.  At most 104 calls; no null-like elements.
        :post-condition: true, false elements, length equal to num of input messages.
        :time-complexity: O(1)
        :aux-space-complexity: O(1)
        """
        for e in lst:
            self.time.append(e[0])
            self.msg.append(e[1])

        for i in range(len(self.msg)):
            self.output.append(self.assess_message_aux(self.time[i], self.msg[i]))

        return self.output

    def assess_message_aux(self, timestamp: int, message: str) -> bool:
        """ Assesses if a message input is allowed to be received
        against the criteria of its uniqueness and timestamp.
        :input: timestamp: time received as int. message: input str
        :return: bool showing message acceptance against criteria
        :pre-condition: 0 <= timestamp <= 109.  timestamp passed in chronological order.  
        1 <= message.length <= 30.  At most 104 calls; no null-like elements.
        :post-condition: true, false elements, length equal to num of input messages.
        :time-complexity: O(1)
        :aux-space-complexity: O(1) 
        """
        #  if unique, approve input
        if message not in self.map:

            #  count as seen, map message to time
            self.map[message] = timestamp
            return True

        #  if not unique
        else:

            #  if current message time less than prev + 10
            if self.map[message] + 10 <= timestamp:

                #  approve input, update map message to time
                self.map[message] = timestamp
                return True

            #  if current message time > previously seen time + 10
            else:

                #  disapprove input; unique message every 10
                return False


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            Logger().assess_message(([[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]])),
            [True, True, False, False, False, True])


if __name__ == '__main__':
    unittest.main()
