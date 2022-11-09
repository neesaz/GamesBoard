'''
    File: battleship.py
    Author: Nees Abusaada
    Purpose: This program is about battleship game. It will ask
    the user for the style board. The user should type x y numbers to
    sart playing. Also, it will print out the players name and result each time
    the player add new location.
'''


class Board:
    '''
    The Board class represents the battle ship board and update the board
        based on the changes of movements. it includes private attribute,
        which is representing by adding(._).

    The constructor contain the board's size, which is an integer.

    The class defines several helpful methods and fields:
        def get_taken_spaces(self) - getter for the taken points on the board.
        def add_ship(self, ship, location) -  It adds the ship on the board
                                              based on the location as (x,y).
        def print(self) - It prints the board game style.
        def get_ships(self) - getter for ship information.
        def has_been_used(self, position) - It checks if the points has been
                                            used in the board based on the
                                            location as (x,y).
        def attempt_move(self, position) - Changes the point state to
                                           available to hit or miss or sunk,
                                           which is completely destroyed.
        def update_board(self, hit_position) - It updates the board if the
                                               player make any changes
                                               on the game.
    '''

    def __init__(self, size):
        '''
        parameters:
            self: A self pointer.
            size: An integer.
        This method define size, creates empty points based on the
        size. It creates empty array for the all the ships, It has an array
        for that contain the strings that marked the points as used on the
        board, and empty array for the taken points.
        '''
        assert size > 0
        self._size = size
        self._board = [['.'] * size for x in range(size)]
        self._ships = []
        self.used_values = ['*', 'o', 'X']
        self._taken_spaces = []

    def get_taken_spaces(self):
        '''
        parameter:
            self: A self pointer.
        return:
            return self._taken_spaces
        This method returns the used points array.
        '''
        return self._taken_spaces

    def add_ship(self, ship, location):
        '''
        parameter:
            self: A self pointer.
            ship: An array of multiple points
            location: Tuple of integers as (x,y)
        This method has an empty array for storing the positions.
        Using for loop to iterate over the position and append
        with creating new points that adds the x value of the location
        points with x value of the position, and add y value  of the location
        points with y value  of the position. Using for loop to iterate
        over the position on ship class. nested loop for iterating over
        rows an columns. Using if statement to check if pos[1] == row
        and pos[0] == col. Then using the position to put the first
        letter of the name player. then append the (x,y) location to
        the taken spaces array.
        '''
        temp_positions = []
        for pos in ship.get_positions():
            assert 0 <= pos[0] + location[0] <= self._size
            assert 0 <= pos[1] + location[1] <= self._size
            temp_positions.append((pos[0] + location[0], pos[1] + location[1]))
        ship.set_positions(temp_positions)
        # assert location[1] > self._size

        for pos in ship.get_positions():
            for row in range(self._size):
                for col in range(self._size):
                    if pos[1] == row and pos[0] == col:
                        assert self._board[row][col] == '.'
                        self._board[row][col] = ship.get_name()[0]
                        self._taken_spaces.append((location[0], location[1]))
                        self._ships.append(ship)
    def print(self):
        '''
        parameter:
            self: A self pointer.
        This method prints out the game board.
        Using for loop to iterate with range of the size.
        Using if statement for excepting if the size id greater
        than one. Also using another for loop to iterate over the
        board grid and print out the array with using end ="" to
        have it on the same line.
        '''
        calculated_num = self._size // 10
        size_board = self._size - 1
        length_spaces = (self._size * 2) + 1
        print((" " * 2), end="")
        print("+" + "-" * length_spaces + '+')
        for i in range(size_board, -1, -1):
            print(' ' * - (len(str(i)) + 1) + str(i) + ' | ', end='')
            for j in self._board[i]:
                print(j, end=' ')
            print('|')
        print((" " * 2), end="")
        print( '+' + '-' * length_spaces + '+')
        if calculated_num > 1 :
            print((' ' * (int(calculated_num) + 2 )),end=" ")
            first_number_line = " "
            second_numbers_line = "     "
        else:
            first_number_line = "   "
            second_numbers_line = "    "
        for k in range(1, self._size + 1):
            num = str(k - 1)
            if len(num) > 1:
                first_number_line += num[0] + " "
                second_numbers_line += num[1] + " "
            else:
                first_number_line += ("  ")
                second_numbers_line += (num + " ")
        if len(first_number_line.strip()) == 0:
            print(second_numbers_line)
        else:
            print(first_number_line)
            print(second_numbers_line)

    def get_ships(self):
        '''
        parameter:
            self: A self pointer.
        return:
            return self._ships
        This method returns ships array.
        '''
        return self._ships

    def has_been_used(self, position):
        '''
        parameter:
            self: A self pointer.
            position: Tuple of integers as (x,y)
            return self._board[position[1]][position[0]] in self.used_values
        This method returns from self._board position if it is in
        used_values array.
        '''
        assert 0 <= position[0] < self._size
        assert 0 <= position[1] < self._size
        return self._board[position[1]][position[0]] in self.used_values

    def attempt_move(self, position):
        '''
        parameter:
           self: A self pointer.
           position: Tuple of integers as x and y
        This m2ethod changes the movements of the players in the board.
        If the player choose points that has ship on it which is
        any letter, it counts as hit. if it not , which is . it change it
        to miss which is o. Using for loop to iterate over the ships
        and call the hit function with position as parameter. Using
        if statement to check if did_hit_ship True then we change it to
        hit (*). Otherwise, it will be miss(o). Also if the ship is None
        that means the ship has been hit and it returns sunk with the player
        name.
        '''
        assert not self.has_been_used(position)
        did_hit_ship = False
        for s in self._ships:
            if s.is_hit(position):
                did_hit_ship = True
        if did_hit_ship:
            self._board[position[1]][position[0]] = '*'
        if self._board[position[1]][position[0]] == '.':
            self._board[position[1]][position[0]] = 'o'
        ship = self.update_board(position)
        if ship is None:
            if did_hit_ship:
                return "Hit"
            else:
                return "Miss"
        else:
            return "Sunk(" + ship.get_name() + ")"

    def update_board(self, hit_position):
        '''
        parameter:
            self: A self pointer.
            hit_position: Tuple of integers as (x,y)
        return:
            ship_match -  the sunk ship
        This method updates the the new changes to the board
        which is sunk. Using for loop to iterate over the the
        ships and using if statement to chek if the method is_sunk
        return True then will change all of the poisions that been hit
        to X .
        '''
        ship_match = None
        for s in self._ships:
            if s.is_sunk():
                for pos in s.get_positions():
                    self._board[pos[1]][pos[0]] = 'X'
                    if pos[0] == hit_position[0] and pos[1] == hit_position[1]:
                        ship_match = s
        return ship_match


class Ship:
    '''
    The Ship class represents the ship information that should appear
        on the game board, which is the player's name and locations.
        it includes private attribute, which is representing by adding(._).

    The constructor contain the ship name and an array contains the
        position of the ship.

    The class defines several helpful methods and fields:
        def set_name(self, name) - Setter for the name
        def get_name(self) - Getter for the name
        def set_positions(self, positions) - Setter for the positions
        def is_hit(self, position) - Returns False if the location is not hit
                                     yet.
        def get_positions(self) -  Getter for the array positions
        def rotate(self, rot) - Change the position by coordinates
        def is_sunk(self) -  Return True if it is sunk .
        def print(self):- It prints the ship
    '''

    def __init__(self, name, positions):
        '''
        parameter:
            self: A self pointer.
            name : A string
            positions: An array
        This method defines th name and positions. Also
        it takes a place of the name to add it on the board
        multiplied by the length of the array that contain all
        the positions of the ship.
        '''
        assert len(name) > 0
        self._name = name
        self._positions = positions
        # at index zero to get the first letter of the name.
        self._ship_info = [name[0]] * len(self._positions)

    def set_name(self, name):
        '''
        parameter:
            self: A self pointer.
            name: A string
        This method set the name.
        '''
        self._name = name

    def get_name(self):
        '''
        parameter:
            self: A self pointer.
        return:
            return self._ships
        This method gets the name
        '''
        return self._name

    def set_positions(self, positions):
        '''
        parameter:
            self: A self pointer.
            positions: An array
        This method set the positions.
        '''
        self._positions = positions

    def is_hit(self, position):
        '''
        parameter:
            self: A self pointer.
            position: Tuple of integers as (x,y)
        return:
            missile_hit - False
        This method set missile_hit to False. Using for loop
        to iterate over the length of the array that contain the
        ship positions. Using if statement to chek if x value in the
        positions array equals x value in the position and the y in the
        positions array equals y value in the position, then change
        missile_hit to True. Aslo hit the player name at that position.
        '''

        missile_hit = False
        for i in range(len(self._positions)):
            if self._positions[i][0] == position[0] \
                    and self._positions[i][1] == position[1]:
                missile_hit = True
                self._ship_info[i] = "*"
        return missile_hit

    def get_positions(self):
        '''
        parameter:
            self: A self pointer.
        return:
             self._positions
        This method gets the array that contain the points.
        '''
        return self._positions

    def rotate(self, rot):
        '''
        parameter:
            self: A self pointer.
            rot: an integer.
        This method gets the array that contain the points.
        using assrt function to check the rot is [0,3].
        Uding for loop to iterate over the positions and
        and muniplate it with coordinates.
        '''
        assert 0 <= rot <= 3
        for i in range(rot):
            temp = []
            for s in self._positions:
                if s[1] < 0:
                    temp.append((s[1], s[0]))
                else:
                    temp.append((s[1] * -1, s[0] * -1))
            self._positions = temp


    def is_sunk(self):
        '''
        parameter:
            self: A self pointer.
        return:
            all_parts_destroyed
        This method set the all_parts_destroyed true.
        Using for loop to check if info in ships are
        same as the first letter of player's name
        then it will returns False.
        '''
        all_parts_destroyed = True
        for info in self._ship_info:
            if info == self._name[0]:
                all_parts_destroyed = False
        return all_parts_destroyed

    def print(self):
        '''
        parameter:
            self: A self pointer.
        This method print out the ship info with
        the name. using join function to combine the
        whitespace with the self._ship_info.
        '''
        print("".join(self._ship_info) +\
        " " * (10 - len(self._positions)) + self._name)
SIZE = 10
player_A_board = Board(SIZE)
player_A_board.print()
