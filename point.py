
class Point:
    # Group data regarding a particular point

    def __init__(self, x=0, y=0, v=0, w=0, dv=0, dw=0, prev_point: 'Point' = None):
        # Initilaze position, scalar velocity, scalar angular velocity,
        # scalar acceleration and scalar angular acceleration
        self.x = x
        self.v = v
        self.w = w
        self.dv = dv
        self.dw = dw

        # Initialize previous points information
        self.prev_point = prev_point

    def set_velocity(self, dt):
        # Set velocity using prev_point velocity, acceleration and given time interval
        pass

    def set_angular_velocity(self, dt):
        # Set angular velocity using prev_point angular velocity, angular acceleration and given time interval
        pass

    def set_positon(self, dt):
        # Set position using velocity, angular velocity, theta and given time interval
        pass

    def constraint_velocity(self):
        # returns contraint in-equality equation contraining velocity
        pass

    def constraint_angular_velocity(self):
        # returns contraint in-equality equation contraining angulare velocity
        pass
