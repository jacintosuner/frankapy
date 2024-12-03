import argparse
from frankapy import FrankaArm
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_pose', '-u', action='store_true')
    parser.add_argument('--move_away_z', '-z', type=float, default=0.05, help='Distance in meters to move up in z-direction')
    parser.add_argument('--close_grippers', '-c', action='store_true')
    args = parser.parse_args()

    print('Starting robot')
    fa = FrankaArm()

    if args.move_away_z:
        current_pose = fa.get_pose()
        transformation_matrix = np.array(fa._state_client._get_current_robot_state().robot_state.O_T_EE).reshape(4, 4).transpose()
        z_axis = transformation_matrix[:3, 2]
        current_pose.translation -= z_axis * args.move_away_z
        fa.goto_pose(current_pose)

    if args.use_pose:
        print('Reset with pose')
        fa.reset_pose()
    else:
        print('Reset with joints')
        fa.reset_joints()
    
    if args.close_grippers:
        print('Closing Grippers')
        fa.close_gripper()
    else:
        print('Opening Grippers')
        fa.open_gripper()