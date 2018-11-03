import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Settings for Plotting
plt.style.use('seaborn-white')
plt.rcParams['font.size'] 		= 30
plt.rcParams['axes.labelsize'] 	= 30
plt.rcParams['axes.titlesize'] 	= 30
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 30
plt.rcParams['figure.titlesize']= 30
# plt.rcParams['text.usetex'] 	= True


#Constants for Model
params = {}
params['c_op'] 	=  .1
params['delta_same'] =  .3
params['support_v'] = (0,1)
params['degradation_multiplier'] = 2
params['EEPP_coeff'] = 1
params['p_s_1_per_mile'] = 0.15
params['k_bar'] = 1
params['scenario'] = 'sdsd' #'ssssd' #'sssd' # 'ssd' #'sdsd' means two different destinations, 'ssd' means a common one, two customers

#Constants for Optimization
params['solver_type'] = 'closed_form' #  'gridsearch' #
params['gridsearch_num'] = 21
params['p_x_max_per_mile'] = params['support_v'][1]

#Location grid
if params['scenario'] == 'sdsd':
	params['x_min'] = -1
	params['x_max'] = 3
	params['y_min'] = -2
	params['y_max'] = 2
	params['EEPP_coeff_array'] = [1,50]#[1,10,50] #[10000,100000]#[50,1000]#
else:
	params['x_min'] = -3
	params['x_max'] = 3
	params['y_min'] = -3
	params['y_max'] = 3
	params['EEPP_coeff_array'] = [1,10]

params['xy_grid_resolution_num'] = 20 #100
params['xvals'] = np.array(list(range(params['x_min']*params['xy_grid_resolution_num'],params['x_max']*params['xy_grid_resolution_num'],1)))/params['xy_grid_resolution_num']
params['yvals'] = np.array(list(range(params['y_min']*params['xy_grid_resolution_num'],params['y_max']*params['xy_grid_resolution_num'],1)))/params['xy_grid_resolution_num']



#Profit vs EEPP_coeff
params['multiprocessing'] = False
params['nprocesses'] = 8
params['all_data_keys'] = [
	'profitval',
	'expost_penalty',
	'ps',
	'px',
	'prob_pool',
	'prob_exclusive',
	'prob_nothing',
	't_j',
	'circle_s1d',
	'profitval_and_prob_pool',
	'circle_delta_1_bar',
	'circle_delta_2_bar',
	'circle_delta_3_bar',
	'profitval_and_prob_pool_and_deltabars',
	'circle_delta_1_bar_region',
	'circle_delta_2_bar_region',
	'circle_delta_3_bar_region',
	'foc_condition',
	'foc_condition_boundary',
	'foc_condition_boundary_overlay_prob_pool',
	'delta1bars_intersection']

params['plot_keys'] = [
	# 'profitval',
	# 'expost_penalty',
	# 'ps',
	# 'px',
	'prob_pool',
	# 'prob_exclusive',
	# 'prob_nothing',
	# 't_j',
	# 'circle_s1d',
	# 'profitval_and_prob_pool',
	# 'circle_delta_1_bar',
	# 'circle_delta_2_bar',
	# 'circle_delta_3_bar',
	'profitval_and_prob_pool_and_deltabars',
	'circle_delta_1_bar_region',
	'circle_delta_2_bar_region',
	'circle_delta_3_bar_region',
	# 'foc_condition',
	# 'foc_condition_boundary',
	'foc_condition_boundary_overlay_prob_pool',
	'delta1bars_intersection']
params['plot_probabilities'] = [
	'prob_pool',
	'prob_exclusive',
	'prob_nothing']