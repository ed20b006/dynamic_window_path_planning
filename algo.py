from point import Point

class DynamicPathPlanning:
    # Optimize acceleration and angular acceleration of successing points (including current point)
    # Given: initial point's data

    def __init__(self, init_point: 'Point'):
        self.init_point = init_point

    @staticmethod
    def objective(x):
        pass

    @staticmethod
    def constraint(x):
        pass

    def optimize(self):
        # One function to do everyting related to optimization

        # 1. Create dictionary constraints for setting constraints of velocity angular velocity
        # using Point.constraint_velocity and Point.constraint_angular_velocity

        # 2. Get init_val Intial acceleration and angular acceleration

        # 3. Minimize passing --> objective, init_val, contraints

        pass

