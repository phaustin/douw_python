# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Import modules and pick a nice plotting style

# %%
from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')

# %% [markdown]
# # Create the series
#
# Note that python counts from 0 by default, so if we create a 40 item list starting
# from zero, we need to add 1 to each term. Alternatively, we could say:
#
# ```python
# term_counter = np.arange(1,41)
# ```

# %%
numterms=40
term_counter = np.arange(0,numterms)
term_counter = term_counter + 1
output_list = []
for n in term_counter:
    this_term = (1 + (1/n))**n
    output_list.append(this_term)

# %% [markdown]
# # Make the plot
#
# I'm using the more sophisticate python plotting style (object oriented)
# because it makes it easier to keep track of what attributes go onto
# which graph.  Overkill in this case, but important if you have multi-axes
# plots.  (This is called "handle graphics" in matlab).

# %%
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.plot(term_counter,output_list,'b-')
ax.set_title("exponential series")
ax.set_xlabel("term number")
ax.set_ylabel("term value");
