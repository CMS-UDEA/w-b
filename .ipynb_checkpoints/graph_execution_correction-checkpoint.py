import numpy as np
import matplotlib.pyplot as plt
#import awkward as ak
import mplhep as hep

import pickle

def get_axis(den):
    return [den.axes.bin(i)[0][0] for i in range(len(den.values())+1)]

BK = {   
      "data":["SingleElectron"],
      
      "tt":["TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8"]
     }

wbc_dicc={'data':[1],
          "tt":[0.0358]
        }

list_ghap=["pt_e_all","eta_e_all","phi_e_all","met_all","met_phi_all","pt_bjet_all","phi_bjet_all","eta_bjet_all",
          "transversemass_all"]


year="2017"
procesostrige="triggerEffWbProcessor"
fecha="2022-10-12"
url_salida="./out_ejecucion_alexis/"+fecha+"/"+year+"/"


dicc_out={}
dicc_bins={}

dicc_out_back={}
for i in BK.keys():
    with open(url_salida+year+"-"+procesostrige+"-"+BK[i][0]+"-"+fecha+".pkl", 'rb') as handle:
            list_pkl_value = pickle.load(handle)
    val_dic_binstwo={}
    listavalrestwo={}
    listavalrestwo_back={}
    for k in list_ghap:
        #print(k)
        listavalres=[0] * len(list_pkl_value[BK[i][0]][k].values())
        listavalres_back=[0] * len(list_pkl_value[BK[i][0]][k].values())
        for j in range(len(BK[i])):
            with open(url_salida+year+"-"+procesostrige+"-"+BK[i][j]+"-"+fecha+".pkl", 'rb') as handle:
                list_pkl = pickle.load(handle)

            ptmtrigger=list_pkl[BK[i][j]][k].values()*wbc_dicc[i][j]
            ptmtrigger_back=list_pkl[BK[i][j]][k].values()
            
            listavalres=listavalres+ptmtrigger
            listavalres_back=listavalres_back+ptmtrigger_back
            val_dicc_bins=np.array(get_axis(list_pkl[BK[i][j]][k]))
            
        val_dic_binstwo[k]=val_dicc_bins
        dicc_bins[i]=val_dic_binstwo
        listavalrestwo[k]=listavalres
        listavalrestwo_back[k]=listavalres_back
        dicc_out[i]=listavalrestwo
        dicc_out_back[i]=listavalrestwo_back
# make a nice ratio plot, adjusting some font sizes

def error(variableplot):
    a=np.sqrt(dicc_out['data'][variableplot])
    return a

def plot_cms(variableplot,labels):
    plt.rcParams.update({
        'font.size': 14,
        'axes.titlesize': 18,
        'axes.labelsize': 18,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12
    })




    fig, (ax, rax) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=(7,7),
        gridspec_kw={"height_ratios": (3, 1)},
        sharex=True
    )


    fig.subplots_adjust(hspace=.07)
    # plot the MC first

    # Here is an example of setting up a color cycler to color the various fill patches
    # We get the colors from this useful utility: http://colorbrewer2.org/#type=qualitative&scheme=Paired&n=6
    from cycler import cycler
    colors = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c']
    ax.set_prop_cycle(cycler(color=colors))

    fill_opts = {
        'edgecolor': (0,0,0,0.3),
        'alpha': 0.8
    }
    error_opts = {
        'label': 'Stat. Unc.',
        'hatch': '///',
        'facecolor': 'none',
        'edgecolor': (0,0,0,.5),
        'linewidth': 0
    }
    data_err_opts = {
        'linestyle': 'none',
        'marker': '.',
        'markersize': 10.,
        'color': 'k',
        'elinewidth': 1,
    }

    plt.plot(igsize=(12, 4))

    #hep.cms.text("Preliminary",ax=ax)
    hep.histplot(dicc_out['data'][variableplot],bins=dicc_bins['data'][variableplot],
             yerr=error(variableplot),
             histtype='errorbar',
             #fmt=".",
            color ="black",
             ax=ax,
             label="$Data$",
             capsize=3,
             linewidth=1.5)   

    #ttbar

    hep.histplot(dicc_out['tt'][variableplot],bins=dicc_bins['tt'][variableplot],
                color='#40E0D0',
                ax=ax,
                label="$\\bar{tt}$",
                histtype="fill",
                edgecolor= (0,0,0,0.3),
                alpha= 1,
                stack=True)


    #W+jets

    """ hep.histplot(dicc_out['WJ'][variableplot],bins=dicc_bins['WJ'][variableplot],
                color='#b2df8a',
                ax=ax,
                label="W+Jets",
                histtype="fill",
                edgecolor= (0,0,0,0.3),
                alpha= 1,
                stack=True)

    #DY
    hep.histplot(dicc_out["DY"][variableplot],bins=dicc_bins["DY"][variableplot],
                color='#a6cee3',
                ax=ax,
                label="DY",
                histtype="fill",
                edgecolor= (0,0,0,0.3),
                alpha= 1,
                stack=True)"""

    # ST

    """hep.histplot(dicc_out['ST'][variableplot],bins=dicc_bins['ST'][variableplot],
                color='#e31a1c',
                ax=ax,
                label="ST",
                histtype="fill",
                edgecolor= (0,0,0,0.3),
                alpha= 1,
                stack=True)"""
    # VV



    """hep.histplot(dicc_out['VV'][variableplot],bins=dicc_bins['VV'][variableplot],
                color='#33a02c',
                ax=ax,
                label="VV",
                histtype="fill",
                edgecolor= (0,0,0,0.3),
                alpha= 1,
                stack=True)"""


    #Background
    #background=dicc_out["DY"][variableplot]+\
    #dicc_out["WJ"][variableplot]+\
    #dicc_out["ST"][variableplot]+\
   # dicc_out["VV"][variableplot]+\
    #dicc_out["tt"][variableplot]
   # hep.histplot(background,bins=dicc_bins['VV'][variableplot],
              #  color='black',
               # ax=ax,
               # label="TOT_BACK",
               # histtype='fill',
                #alpha= 1,
               # stack=True)

    #data
    
    """hep.histplot(dicc_out['data']["pt_e_bjets"],bins=dicc_bins['data']["pt_e_bjets"],
                color='b',
                ax=ax,
                label="BACK",
                histtype='errorbar',
                alpha= 1,
                stack=True)"""

    #ax.autoscale(axis='y', tight=True)
    #ax.autoscale(axis='x', tight=True)
    ax.set_ylim(0, None)
    ax.set_xlabel(None)
    leg = ax.legend()

    # now we build the ratio plot
    #ratio=dicc_out['data'][variableplot]/background
    #bins_dicc=dicc_bins['data'][variableplot]
   # print(len(ratio))
   # print(len(bins_dicc))
    
    
    
    ratio_new=[]
    binns_new=[]
    #coffea.hist.plotratio(dicc_out['data'][variableplot], background, 
    #                      ax=rax)
    #print(background)
    """try:
        hep.histplot(ratio_new,bins=bins_dicc,
                    color='black',
                    ax=rax,
                    histtype='errorbar',
                    yerr=[0]*len(ratio_new))
    except:
        pass"""

 

    rax.set_ylabel('DATA/MC')
    rax.set_ylim(0,2)

    #rax.hlines(y=1, xmin=min(dicc_bins["DY"][variableplot]), xmax=max(dicc_bins["DY"][variableplot]),color="black",linestyles="--")
    
    
    if "$p_{T}" in labels or "M_{T}" in labels:
        plt.xlabel("{} [GeV]".format(labels),loc='right')
    else:
        plt.xlabel("{}".format(labels),loc='right')

    ax.set_ylabel('Events',loc='top')

    lumi = plt.text(1., 1., r"41.48 fb$^{-1}$ (13 TeV)",
                    fontsize=16, 
                    horizontalalignment='right', 
                    verticalalignment='bottom', 
                    transform=ax.transAxes
                   )
   # plt.savefig("./out_plots_alexis/"+fecha+"/"+year+"/rc/"+variableplot+".png",bbox_inches="tight")