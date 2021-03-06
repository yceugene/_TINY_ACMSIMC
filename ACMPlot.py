# coding:u8
from pylab import plt, mpl, np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# from pprint import pprint
from collections import OrderedDict as O
import pandas as pd
import matplotlib

matplotlib.use("TkAgg")

######################
# Plotting
def get_axis(cNr):
    # fig, axes = plt.subplots(ncols=cNr[0], nrows=cNr[1], dpi=150, sharex=True);
    fig, axes = plt.subplots(
        ncols=cNr[0],
        nrows=cNr[1],
        sharex=True,
        figsize=(16 * 0.8, 9 * 0.8),
        dpi=80,
        facecolor="w",
        edgecolor="k",
    )
    fig.subplots_adjust(right=0.95, bottom=0.1, top=0.95, hspace=0.2, wspace=0.02)
    # fig.subplots_adjust(right=0.85, bottom=0.1, top=0.95, hspace=0.25)
    if sum(cNr) <= 2:
        return axes
    else:
        return axes.ravel()


def plot_key(ax, key, df, time, font):
    ax.plot(time, df[key].values, "-", lw=1)
    ax.set_ylabel(key, fontdict=font)


def plot_it(ax, ylabel, d, time, font):
    count = 0
    for k, v in d.items():
        if count == 0:
            count += 1
            # ax.plot(time, v, '--', lw=2, label=k)
            ax.plot(time, v, "-", lw=1)
        else:
            # ax.plot(time, v, '-', lw=2, label=k)
            ax.plot(time, v, "-", lw=1)

    # ax.legend(loc='lower right', shadow=True)
    # ax.legend(bbox_to_anchor=(1.08,0.5), borderaxespad=0., loc='center', shadow=True)
    ax.set_ylabel(ylabel, fontdict=font)
    # ax.set_xlim(0,35) # shared x
    # ax.set_ylim(0.85,1.45)


def draw_trend():
    # plot style
    style = np.random.choice(plt.style.available)
    print(style)
    plt.style.use(
        "grayscale"
    )  # [u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']
    # plot setting
    mpl.rcParams["mathtext.fontset"] = "stix"
    mpl.rcParams["font.family"] = "STIXGeneral"
    mpl.rcParams["legend.fontsize"] = 11
    # mpl.rcParams['legend.family'] = 'Times New Roman'
    mpl.rcParams["font.family"] = ["Times New Roman"]
    mpl.rcParams["font.size"] = 11.0
    # mpl.style.use('classic')
    font = {
        "family": "Times New Roman",  #'serif',
        "color": "darkblue",
        "weight": "normal",
        "size": 11,
    }
    textfont = {
        "family": "Times New Roman",  #'serif',
        "color": "darkblue",
        "weight": "normal",
        "size": 9,
    }

    df_profiles = pd.read_csv(
        r"./algorithm.dat", na_values=["1.#QNAN", "-1#INF00", "-1#IND00"]
    )
    df_info = pd.read_csv(r"./info.dat", na_values=["1.#QNAN", "-1#INF00", "-1#IND00"])

    # df_profiles["rpm_cmd"]=df_profiles["ACM.rpm_cmd"]
    # df_profiles["rpm_mes"]=df_profiles["ACM.rpm_cmd"]-df_profiles["e_omega"]
    # print(df_profiles.keys())

    no_samples = df_profiles.shape[0]
    no_traces = df_profiles.shape[1]
    print(
        df_info,
        "Simulated time: %g s."
        % (no_samples * df_info["TS"].values[0] * df_info["DOWN_SAMPLE"].values[0]),
        "Key list:",
        sep="\n",
    )
    for key in df_profiles.keys():
        print("\t", key)

    time = (
        np.arange(1, no_samples + 1)
        * df_info["DOWN_SAMPLE"].values[0]
        * df_info["TS"].values[0]
    )

    ax_list = []
    for i in range(0, no_traces, 6):
        ax_list += list(get_axis((1, 6)))

    for idx, key in enumerate(df_profiles.keys()):
        plot_it(
            ax_list[idx],
            key,
            O(
                [
                    (str(idx), df_profiles[key]),
                    # (str(idx), df_profiles[key]),
                ]
            ),
            time,
            font,
        )
        # print(idx,key)
    # ax_list[12].plot(time,df_profiles["rpm_mes"],color="red")
    # fm=plt.get_current_fig_manager()
    # fm.window.showMaximized()
    figs = plt.gcf()
    return figs
