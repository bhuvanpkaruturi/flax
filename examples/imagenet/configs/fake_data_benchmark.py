# Copyright 2024 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hyperparameter configuration for Fake data benchmark."""

import jax

from configs import default as default_lib


def get_config():
  """Get the hyperparameter configuration for Fake data benchmark."""
  # Override default configuration to avoid duplication of field definition.
  config = default_lib.get_config()
  # batch size must be divisible by number of devices.
  config.batch_size = 64 * jax.device_count()
  # Using half precision does not work on TPUs
  config.half_precision = False
  config.num_epochs = 5

  # Run for a single step:
  config.num_train_steps = 2000
  config.steps_per_eval = 100

  config.log_every_steps = 100

  return config
