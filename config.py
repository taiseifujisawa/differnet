'''This file configures the training procedure because handling arguments in every single function is so exhaustive for
research purposes. Don't try this code if you are a software engineer.'''

# device settings
device = 'cuda' # or 'cpu'
#device = 'cpu' # or 'cpu'
import torch
torch.cuda.set_device(0)

seed = 1

# data settings
dataset_path = r"C:\Users\nktlab\Desktop\Experiment\fujisawa\dataset_for_differnet\dataset"
class_name = "class"
modelname = "test_result"

img_size = (256,256)
img_dims = [3] + list(img_size)

# transformation settings
transf_rotations = True
transf_brightness = 0.0
transf_contrast = 0.0
transf_saturation = 0.0
norm_mean, norm_std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

# network hyperparameters
n_scales = 3 # number of scales at which features are extracted, img_size is the highest - others are //2, //4,...
clamp_alpha = 3 # see paper equation 2 for explanation
n_coupling_blocks = 8
fc_internal = 2048 # number of neurons in hidden layers of s-t-networks
dropout = 0.0 # dropout in s-t-networks
lr_init = 2e-4
n_feat = 256 * n_scales # do not change except you change the feature extractor

# dataloader parameters
n_transforms = 4 # number of transformations per sample in training
n_transforms_test = 32 # number of transformations per sample in testing
batch_size = 16 # actual batch size is this value multiplied by n_transforms(_test)
batch_size_test = batch_size * n_transforms // n_transforms_test

# total epochs = meta_epochs * sub_epochs
# evaluation after <sub_epochs> epochs
meta_epochs =40
sub_epochs = 20

# output settings
verbose = False
grad_map_viz = False
hide_tqdm_bar = True
save_model = True
