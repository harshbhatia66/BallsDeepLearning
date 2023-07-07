import time

out_dir = 'out-charlie_v3'
eval_interval = 10
eval_iters = 40
wandb_log = True # feel free to turn on
wandb_project = 'charlie_v3'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'charlie_v3'
init_from = 'gpt2-large' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 2
gradient_accumulation_steps = 32
max_iters = 20000

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
