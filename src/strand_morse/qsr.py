import sys
import math

NUMBER_OF_PARTITIONS = 8
PARTITION_SIZE = (2.0 * math.pi) / NUMBER_OF_PARTITIONS  

def relative_radius(a, b, c):
    # compute relative radius r (close/distant)
    return math.sqrt( math.pow(c[0] - b[0],2.0) +  math.pow(c[1] - b[1],2.0) +  math.pow(c[2] - b[2],2.0))/ math.sqrt( math.pow(b[0] - a[0],2.0) +  math.pow(b[1] - a[1],2.0) +  math.pow(b[2] - a[2],2.0))
  

def relative_angle(a, b, c):

    # compute relative angle (left/right/straight, front/back/straight)
    angle_BA = math.atan2((b[1] - a[1]),(b[0] - a[0]))

    if angle_BA < 0:
      angle_BA += 2 * math.pi

    angle_CB = math.atan2((c[1] - b[1]),(c[0] - b[0]))
    if angle_CB < 0:
       angle_CB += 2 * math.pi
    
    ## std::cout << "BA: " << angle_BA << std::endl;
    ## std::cout << "CB: " << angle_CB << std::endl;    
    ## std::cout << "CB - BA: " << angle_CB - angle_BA << std::endl;

    angle_rel = angle_CB - angle_BA
    if angle_rel < 0:
        angle_rel += 2 * math.pi

    return angle_rel

def normal_dist(x, mean, var):
    return (1.0 / math.sqrt( var * 2.0* math.pi)) * math.exp(-0.5 *(math.pow(x - mean,2)/var));
  
def mean(partition):
    return partition * PARTITION_SIZE
  
def var(partition):
    return PARTITION_SIZE / 2
  
def partition_value(p, angle):
    
    val = sys.float_info.min
    val_cycle = sys.float_info.min
    
    val = normal_dist(angle, mean(p), var(p))
    
    # NOTE: handling cycle [0,2*M_PI] 
    if (p == 0): # first partition
        
        val_cycle = normal_dist(angle, mean(NUMBER_OF_PARTITIONS), var(NUMBER_OF_PARTITIONS))
   
    elif (p == (NUMBER_OF_PARTITIONS - 1)): # last partition
        val_cycle = normal_dist(angle, mean(-1), var(-1));
      

    if (val_cycle > val):
        return val_cycle
    return val

def argmax_partition(angle):
    
    argmax = -1
    max_val = sys.float_info.min
    
    for i in range(0,NUMBER_OF_PARTITIONS):
        val = partition_value(i, angle)
        if val > max_val:
            max_val = val;
            argmax = i;
    return argmax;

def partition_name(p):
    if p == 0:
        return ['behind']
    elif p == 1:
        return ['behind','left']
    elif p == 2:
        return ['left']
    elif p == 3:
        return ['front','left']
    elif p == 4:
        return ['front']
    elif p == 5:
        return ['front','right']
    elif p == 6:
        return ['right']
    else: # p ==7
        return ['behind','right']

def distance(dist):
    if 0.0 <= dist and dist < 0.3:
        return 'close'
    return 'distant'
  

def calc_QSR(camera, landmark, obj):

    reld = relative_radius(camera,landmark,obj)
    rela = relative_angle(camera,landmark,obj)

    #print(reld,rela)

    part = argmax_partition(rela)
    part_qsr = partition_name(part)

    dist_qsr = distance(reld)

    part_qsr.append(dist_qsr)

    qsr_lst = part_qsr
    #print(qsr_lst)
    
    return qsr_lst

