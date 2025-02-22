import argparse

def parse():
    parser = argparse.ArgumentParser(description='Define hyperparameters.')
    parser.add_argument('--model_name', type=str, choices=['monodepth2', 'planedepth', 'depthhints', 'google_api', 'SQLdepth', 'FlowNetC', 'FlowNet2', 'PWC-Net'], required=True, help='name of the subject model.')
    parser.add_argument('--attack_method', type=str, choices=['ours', 'GA_attack', 'S-RS', 'hardbeat', 'whitebox'], required=True, help='name of the attack method.')
    parser.add_argument('--countermeasure', type=str, choices=['None', 'Blacklight'], required=False, default='None', help='name of the cuntermeasure')
    parser.add_argument('--n_iter', type=int, default=10001, help='maximim iterations to try')
    parser.add_argument('--alpha', type=float, default=0.1,  help='step of each attack')
    parser.add_argument('--targeted_attack', default=False, action='store_true', help="attack one targeted scene")
    parser.add_argument('--patch_ratio', type=float, default=0.02,  help='Proportion of patch area')
    parser.add_argument('--batch_size', type=int, default=5, help='batch size of kitti loader')
    parser.add_argument('--n_batch', type=int, default=1, help='number of batch to evaluate per iteration')
    parser.add_argument('--trail', type=int, default=20, help='number of noise sampled')
    parser.add_argument('--num_pos', type=int, default=1, help='number of different position, if 1 then fixed position')
    parser.add_argument('--topk', type=int, default=1, help='number of top k patch for hardbeat')
    parser.add_argument('--p_init', type=float, default=0.025, help='initial ratio of square patch')
    parser.add_argument('--init_iters', type=int, default=100, help='number of initial iters of the attack')
    parser.add_argument('--square_steps', type=int, default=200, help='number of maximum iters of the attack in a square area')
    parser.add_argument('--p_sche', type=str, default='v6', help='square size changing schdule version')
    parser.add_argument('--log_dir', type=str, help='log dir', required=False)
    parser.add_argument('--test_name', type=str, required=True, help='name for this test')
    parser.add_argument('--seed', type=int, default=1, help='Random Seed')
    parser.add_argument("--patch_only", required=False, default=False, action="store_true", help="only focus on the loss of patch area")
    args = parser.parse_args()
    return args


'''tensorboard --logdir /data4/user/cheng443/MDEBlackBox/logs --samples_per_plugin images=200'''