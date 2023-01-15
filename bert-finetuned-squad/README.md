---
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: test-bert-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-bert-finetuned-squad

This model was trained from scratch on the squad dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.11.0.dev0
- Pytorch 1.8.1+cu111
- Datasets 1.12.2.dev0
- Tokenizers 0.10.3
