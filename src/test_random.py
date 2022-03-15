#!/usr/bin/env python3
import sys
from environment import ArmToolsToysEnvironment
import numpy as np
import time
from pymap_elites.map_elites import cvt as cvt_map_elites
from pymap_elites.map_elites import common as cm



gui = False # Plot environment animation ?
n = 20000 # Number of iterations

env = ArmToolsToysEnvironment()

t = time.time()

stick1_moved = 0
stick2_moved = 0
obj1_moved = 0
obj2_moved = 0


# storage directory for results
log_dir = sys.argv[1]
# num evals
n_evals = int(sys.argv[2])
# batch size
b_size = int(sys.argv[3])
# dump period
dump_period = int(sys.argv[4])
# selector to use [ "uniform", "curiosity", "curiosity-child" ]
selector = sys.argv[5]
# mutation operator to use [ "iso_dd", "polynomial", "sbx" ]
mutation = sys.argv[6]
# additional mutations
variant = "" 
if len(sys.argv) > 7:
    variant = sys.argv[7:]


px = \
    {
        "log_outputs": ['centroid'],
        # more of this -> higher-quality CVT
        "cvt_samples": 25000,
        # we evaluate in batches to parallelize
        "batch_size": b_size,
        # proportion of niches to be filled before starting
        "random_init": 0.003,
        # batch for random initialization
        "random_init_batch": 100,
        # when to write results (one generation = one batch)
        "dump_period": dump_period,
        # do we use several cores?
        "parallel": True,
        # do we cache the result of CVT and reuse?
        "cvt_use_cache": False,
        # min/max of parameters
        "min": 0,
        "max": 1,
        # probability of mutating each number in the genotype
        "mutation_prob": 0.3,
        # selector ["uniform", "curiosity", "random_search"]
        "selector" : selector,
        # mutation operator ["iso_dd", "polynomial", "sbx", "gaussian"]
        "mutation" : mutation,
        "variant" : variant, 
        "eta_m" : 5.0,
        "iso_sigma": 0.01,
        "line_sigma": 0.2,
        "std_dev" : 0.02
        }


'''for i in range(n):
    n_dims = 4
    n_basis = 5

    # m is an array of motor commands, bounded to [-1, 1]
    m = np.random.random(n_dims * n_basis) * 2. - 1.

    # s is the sensory feedback from the simulation
    # s is a list of 5 lists. each list at a timestep in the environment,
    # each sublist of size 31 where each value is the x or y position of a 
    # certain element in the environment
    ''' '''
    -31    hand_pos.x, 0
    -30    hand_pos.y,1
    -29    gripper,2
    -28    3stick1_end_pos.x,
    -27    4stick1_end_pos.y,
    -26    5stick2_end_pos.x,
    -25    6stick2_end_pos.y,
    -24    7magnet1_pos.x,
    -23    8magnet1_pos.y,
    -22    9magnet2_pos.x,
    -21    10magnet2_pos.y,
    -20    11magnet3_pos.x,
    -19    12magnet3_pos.y,
    -18    13scratch1_pos.x,
    -17    14scratch1_pos.y,
    -16    15scratch2_pos.x,
    -15    16scratch2_pos.y,
    -14    17scratch3_pos.x,
    -13    18scratch3_pos.y,
    -12    19cat_pos.x,
    -11    20cat_pos.y,
    -10    21dog_pos.x,
    -9    22dog_pos.y,
    -8    23static_objects_rest_state[0].x,
    -7    24static_objects_rest_state[0].y,
    -6    25static_objects_rest_state[1].x,
    -5  26static_objects_rest_state[1].y,
    -4  27static_objects_rest_state[2].x,
    -3  28static_objects_rest_state[2].y,
    -2    29static_objects_rest_state[3].x,
    -1    30static_objects_rest_state[3].y
    ''''''
    print("geno: ", m)
    s = env.update(m, gui=gui)

    for i in range(len(s)):
        if (s[i] > 2):
            s[i] = 2
        elif (s[i] < -2):
            s[i] = -2
    s = np.array(s)
    s = s/2

    print(s)
    print("Max: ", max(s))
    print("Min: ", min(s))
    print("End Update")
    stick1_moved += env.stick1_held
    stick2_moved += env.stick2_held
    obj1_moved += env.magnet1_move
    obj2_moved += env.scratch1_move
'''

def eval( geno ):
    initial_pos = np.array([0.5             ,    0.75            ,    0.75            \
    , 0.22411165235168157 ,0.6508883476483185  ,0.7758883476483185 \
    , 0.6508883476483185  ,0.425               ,0.775              \
    , 0.375               ,0.875               ,0.425              \
    , 0.875               ,0.575               ,0.775              \
    , 0.575               ,0.875               ,0.625              \
    , 0.875               ,0.43331536249035657 ,0.778985905004028  \
    , 0.5571903985815629  ,0.7807324831910138  ,0.325              \
    , 0.775               ,0.375               ,0.775              \
    , 0.625               ,0.775               ,0.675              \
    , 0.775               ,0.5                 ,0.75               \
    , 0.75                ,0.22411165235168157 ,0.6508883476483185 \
    , 0.7758883476483185  ,0.6508883476483185  ,0.425              \
    , 0.775               ,0.375               ,0.875              \
    , 0.425               ,0.875               ,0.575              \
    , 0.775               ,0.575               ,0.875              \
    , 0.625               ,0.875               ,0.5049572254938071 \
    , 0.7319699055573236  ,0.3959161556121309  ,0.7346464941440664 \
    , 0.325               ,0.775               ,0.375              \
    , 0.775               ,0.625               ,0.775              \
    , 0.675               ,0.775               ,0.5                \
    , 0.75                ,0.75                ,0.22411165235168157\
    , 0.6508883476483185  ,0.7758883476483185  ,0.6508883476483185 \
    , 0.425               ,0.775               ,0.375              \
    , 0.875               ,0.425               ,0.875              \
    , 0.575               ,0.775               ,0.575              \
    , 0.875               ,0.625               ,0.875              \
    , 0.4532407081540726  ,0.7852251650729435  ,0.39003445320895463\
    , 0.6155682929063008  ,0.325               ,0.775              \
    , 0.375               ,0.775               ,0.625              \
    , 0.775               ,0.675               ,0.775              \
    , 0.5                 ,0.75                ,0.75               \
    , 0.22411165235168157 ,0.6508883476483185  ,0.7758883476483185 \
    , 0.6508883476483185  ,0.425               ,0.775              \
    , 0.375               ,0.875               ,0.425              \
    , 0.875               ,0.575               ,0.775              \
    , 0.575               ,0.875               ,0.625              \
    , 0.875               ,0.48939678266887393 ,0.8728450206539082 \
    , 0.328103199468302   ,0.5683846055734257  ,0.325              \
    , 0.775               ,0.375               ,0.775              \
    , 0.625               ,0.775               ,0.675              \
    , 0.775               ,0.5                 ,0.75               \
    , 0.75                ,0.22411165235168157 ,0.6508883476483185 \
    , 0.7758883476483185  ,0.6508883476483185  ,0.425              \
    , 0.775               ,0.375               ,0.875              \
    , 0.425               ,0.875               ,0.575              \
    , 0.775               ,0.575               ,0.875              \
    , 0.625               ,0.875               ,0.45714588760021946\
    , 0.9183917781807354  ,0.24647613557307435 ,0.6664626197232839 \
    , 0.325               ,0.775               ,0.375              \
    , 0.775               ,0.625               ,0.775              \
    , 0.675               ,0.775              ])

    genotype = geno
    genotype = genotype * 2
    genotype = genotype - 1
    
    # get BD

    s = env.update(genotype, gui=gui)
    # dound BD to [0, 1]
    '''for i in range(len(s)):
       if (s[i] > 2):
           s[i] = 2
       elif (s[i] < -2):
           s[i] = -2
   ''' 
    s = np.array(s)
    s = s/4
    s = s+0.5
    '''
    Start positions:
    stick_1:        -0.75, 0.25
    stick_2:        0.75, 0.25
    magnet_1:       -0.3, 1.1
    magnet_2:       -0.5, 1.5
    magnet_3:       -0.3, 1.5
    scratch_1:      0.3, 1.1
    scratch_2:      0.3, 1.5
    scratch_3:      0.5, 1.5
    cat:            -0.1, 1.1
    dog:            0.1, 1.1
    static_1:       -0.7, 1.1
    static_2:       -0.5, 1.1
    static_3:       0.5, 1.1
    static_4:       0.7, 1.1
    '''

    BD = [np.array([0.03333333,s[-31],  s[-30]])] # hand coordinate
    indexes = [\
            (-28, -27, 0.1       ),\
            (-26, -25, 0.16666667),\
            (-24, -23, 0.23333333),\
            (-22, -21, 0.3       ),\
            (-20, -19, 0.36666667),\
            (-18, -17, 0.43333333),\
            (-16, -15, 0.5       ),\
            (-14, -13, 0.56666667),\
            (-8,  -7,  0.76666667),\
            (-6,  -5,  0.83333333),\
            (-4,  -3,  0.9       ),\
            (-2,  -1,  0.96666667)\
            ]
    '''
    -31    hand_pos.x, 0
    -30    hand_pos.y,1
    -29    gripper,2
    -28    3stick1_end_pos.x,
    -27    4stick1_end_pos.y,
    -26    5stick2_end_pos.x,
    -25    6stick2_end_pos.y,
    -24    7magnet1_pos.x,
    -23    8magnet1_pos.y,
    -22    9magnet2_pos.x,
    -21    10magnet2_pos.y,
    -20    11magnet3_pos.x,
    -19    12magnet3_pos.y,
    -18    13scratch1_pos.x,
    -17    14scratch1_pos.y,
    -16    15scratch2_pos.x,
    -15    16scratch2_pos.y,
    -14    17scratch3_pos.x,
    -13    18scratch3_pos.y,
    -12    19cat_pos.x,
    -11    20cat_pos.y,
    -10    21dog_pos.x,
    -9    22dog_pos.y,
    -8    23static_objects_rest_state[0].x,
    -7    24static_objects_rest_state[0].y,
    -6    25static_objects_rest_state[1].x,
    -5  26static_objects_rest_state[1].y,
    -4  27static_objects_rest_state[2].x,
    -3  28static_objects_rest_state[2].y,
    -2    29static_objects_rest_state[3].x,
    -1    30static_objects_rest_state[3].y
    '''
    for x, y, lvl in indexes:
        if (s[ x ] != initial_pos[ x ] and s[ y ] != initial_pos[ y ]):
            BD.append(np.array([lvl , s[ x ],  s[ y ]])) 
                #get_index( x ,  y , initial_pos, s))) # stick_1 end position

    return 0, BD

   


np.set_printoptions(precision=20)

functions = []
if 'curiosity_func' in px['mutation']:
    functions = [ cm.iso_dd, cm.sbx, cm.polynomial_mutation ]
else:
    if 'iso_dd' in px['mutation']:
        functions.append( cm.iso_dd )
    if 'sbx' in px['mutation']:
        functions.append( cm.sbx )
    if 'polynomial' in px['mutation']:
        functions.append( cm.polynomial_mutation )

archive = cvt_map_elites.MapElites(3, 20, eval, n_niches=15*100*100, max_evals=n_evals, log_file=None, mutation_func=functions, params=px, bins=[15, 100, 100], log_dir=log_dir)
    

