"""
This module contains useful functions for running bandits.

You do not need to do anything here; but you're free to read up how things work!
"""
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def softmax(x):
    """
    Compute softmax values for each sets of scores in x.
    The softmax is a way to turn values ("preferences") into a distribution,
    where the highest values have the higher probabilities.
    Reminder: softmax(x)_i = e^x_i / sum(e^x).
    We substract by the max to add numerical stability for huge values.
    It has mathematically no effect on the output.
    Parameters
    ----------
    x: vector
        Vector of which we want to compute the softmax.
    Returns
    -------
    ret : vector
        Vector of probabilities following the numerical preferences from x.
    """
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def my_random_choice(v, p=None):
    """
    Samples a value from a vector v following probabilities p.
    Alternatively, v can be a integer = len(p), and this function returns the
    index that would have been selected from v otherwise.
    In the second case, the function doesn't actually need v, but it is used
    to check if the task is consistent (v=len(p)).
    This is a faster version of the np.random.choice function with probabilities.
    Parameters
    ----------
    v: list, or int
        If v is a list, we sample an element from it following p.
        If v is an int, we return the index that would have been the index
        if v was a list.
    p: vector
        Vector of probabilities we want to sample from,
        i.e. discrete vector with sum(p)=1.
    Returns
    -------
    i or v[i] : int or element from v
        Either the index sampled from 0 to integer v-1, or the element of v
        at said index when v is a list.
    """
    if p is None:
        return v[np.random.randint(len(v))]
    # else (general case)
    assert (abs(sum(p)-1.)<1e-6), "Invalid probability vector p, sum={}".format(sum(p))
    r = np.random.rand()
    i = 0
    s = p[i]
    while s < r:
        i += 1
        s += p[i]

    if type(v) is int:
        assert len(p) == v, "Int doesn't match proba length: {} != {}".format(v, len(p))
        return i
    else:
        assert len(v) == len(p), "Incorrect entry lengths v,p: {} != {}".format(len(v), len(p))
        return v[i]


def save_plot(l, file_name, suptitle, title, xlabel, ylabel,
              labels=None, interval_yaxis=None):
    """ Simply saves a plot with multiple usual arguments."""
    if labels is None:
        plt.plot(l)
    else:
        for perf, label in zip(l, labels):
            plt.plot(perf, label=label)
        plt.legend()

    plt.suptitle(suptitle, fontsize=14, fontweight='bold')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if interval_yaxis is not None:
        new_y1, new_y2 = interval_yaxis
        x1,x2,y1,y2 = plt.axis()
        plt.axis((x1,x2,new_y1,new_y2))

    file_name += '.png'
    plt.savefig(file_name)
    print("Saved figure to", file_name)
    plt.close()

def action_plot(l, file_name, suptitle, title, labels=None):
    """ Specific call of save_plot in the case of action proportions
    in bandit problems. """
    save_plot(l, file_name, suptitle, title, 'Steps', 'Best action proportion', labels, interval_yaxis=[0,1])

def perf_plot(l, file_name, suptitle, title, labels=None):
    """ Specific call of save_plot in the case of average reward over time
    in bandit problems. """
    save_plot(l, file_name, suptitle, title, 'Steps', 'Average Reward', labels, interval_yaxis=None)

def dict_string(d):
    """ Turns a dictionary d to a single readable string (for plot title)"""
    s = ""
    for key, value in d.items():
        s += "{}:{}, ".format(key, value)
    return s[:-2] # erase final comma and space
