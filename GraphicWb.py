import pickle
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak
import mplhep as hep
import pandas as pd
from datetime import datetime
import pickle
from hist.intervals import clopper_pearson_interval
import os
import errno
import warnings

hep.style.use(hep.style.CMS)

def get_axis(den):
    return [den.axes.bin(i)[0][0] for i in range(len(den.values())+1)]

def error(num, den):
    try:
        return abs(
            clopper_pearson_interval(num.values(), den.values()) - num.values() / den.values()
        )
    except:
        return abs(
            clopper_pearson_interval(num, den) - num/ den
        )

def graph_hist(data,labels,namesave,save=False,xmin=0,xmax=600):
    plt.plot(igsize=(12, 4))
    hep.cms.lumitext("(13 TeV)")
    hep.cms.text("Work in Progress")
    hep.histplot(data.values(),bins=np.array(get_axis(data)),
                 color="black",density=True,label=labels)
    plt.xlim(xmin,xmax)
    plt.legend()
    plt.xlabel(labels)
    if save:
        plt.savefig(namesave)

def graf_eficience(num,den,labels,labelsx="",labelsy="",colorg="black",colorb="black",labelb="",
                   namesave="",bar_error=False,legenloc=2,fontsize_label=30,
                   save=False,ymin=0.8,ymax=1.1,xmin=0,xmax=600):
    #hep.cms.lumitext("(13 TeV)")
    #hep.cms.text("Work in Progress")
    eficience=np.array(num.values()/den.values())
    bines=np.array(get_axis(num))
    eficience[np.isnan(eficience)] = 0
    hep.histplot(eficience,bins=bines,label=labels,color = colorg,
                 linewidth=2)
    
    if bar_error:
        el_err = error(num, den)
        hep.histplot(eficience,bins=bines,yerr=el_err,histtype='errorbar',fmt="k",
             capsize=3,color=colorg,linewidth=1.5)    
    
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)
    plt.legend(loc = legenloc,fontsize=fontsize_label)
    plt.xlabel(labelsx)
    plt.ylabel(labelsy)
    if save:
        plt.savefig(namesave)
        
def plt_one_two_eficience(num1,den1,num2,den2,title1="",
                      text_lum="",
                      label1="",
                      label2="",
                      label1b="",
                      label2b="",
                      labeltx="",
                      labelty="",
                      namesave="",
                      xmin=0,xmax=0,ymin=0,
                      size=(12,12),save=False):
    plt.figure(figsize=size)
    hep.cms.lumitext(text_lum,fontsize=24)
    hep.cms.text(title1,fontsize=26)
    graf_eficience(num1,den1,bar_error=True,labelb=label1b,
                   labels=label1,colorg="mediumblue",
                  xmin=xmin,xmax=xmax,ymin=ymin)

    graf_eficience(num2,den2,bar_error=True,labelb=label2b,
                   labels=label2,colorg="green",colorb="crimson",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin)
    #save plot
    
    if save:
        plt.savefig(namesave)

def several_plot_eficience(list_data_graph,
                           list_label,
                           lista_color,
                           title1="",
                           text_lum="",                           
                           label1b="",
                           labeltx="",
                           labelty="",
                           namesave="",
                           xmin=0,xmax=0,ymin=0,ymax=1.1,legenloc=2,fontsize_label=30,
                           size=(12,12),save=False):
    plt.figure(figsize=size)
    hep.cms.lumitext(text_lum,fontsize=10)
    hep.cms.text(title1,fontsize=26)
    for i in range(len(list_data_graph)):
        num=list_data_graph[i][0]
        den=list_data_graph[i][1]
        label1=list_label[i]
        colorgraph=lista_color[i]
        graf_eficience(num,den,bar_error=True,labelb=label1b,legenloc=legenloc,
                   labels=label1,colorg=colorgraph,labelsx=labeltx,labelsy=labelty,
                   fontsize_label=fontsize_label,
                   xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
    if save:
        plt.savefig(namesave)

def eficience(num,den):
    try:
        eficience=np.array(num.values()/den.values())
    except:
        eficience=np.array(num/den)
        
    eficience[np.isnan(eficience)] = 0
    return eficience

def graf_scalefactor(num,den,labels,binx,labelsx="",labelsy="",
                     text_lum="",title1="",colorg="black",colorb="black",labelb="",
                     namesave="",bar_error=False,legenloc=2,fontsize_label=30,size=(12,12),
                     save=False,ymin=0.8,ymax=1.1,xmin=0,xmax=600):
    plt.figure(figsize=size)
    hep.cms.lumitext(text_lum,fontsize=24)    
    hep.cms.text(title1,fontsize=26)
    scalefactor=np.array(num/den)
    bines=np.array(get_axis(binx))
    scalefactor[np.isnan(scalefactor)] = 0
    hep.histplot(scalefactor,bins=bines,label=labels,color = colorg,
                 linewidth=2)
    
    if bar_error:
        el_err = error(num, den)
        hep.histplot(eficience,bins=bines,yerr=el_err,histtype='errorbar',fmt="k",
             capsize=3,color=colorg,linewidth=1.5)    
    
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)
    plt.xlabel(labelsx)
    plt.ylabel(labelsy)
    if save:
        plt.savefig(namesave)
        
def sum_background(tt,st,ww,wz,zz,
                   wj70to100,wj100to200,wj200to400,wj400to600,wj600to800,
                   wj800to1200,wj1200to2500,wj2500toinf,dy50to100,dy100to250,
                   dy250to400,dy400to650,dy650toinf,bc_dicc):
    sum_bcg=tt.values()*bc_dicc["tt"]+st.values()*bc_dicc["ST"]+\
        ww.values()*bc_dicc["WW"]+wz.values()*bc_dicc["WZ"]+\
        zz.values()*bc_dicc["ZZ"]+wj70to100.values()*bc_dicc["WJ70to100"]+wj100to200.values()*bc_dicc["WJ100to200"]+\
        wj200to400.values()*bc_dicc["WJ200to400"]+wj400to600.values()*bc_dicc["WJ400to600"]+\
        wj600to800.values()*bc_dicc["WJ600to800"]+wj800to1200.values()*bc_dicc["WJ800to1200"]+\
        wj1200to2500.values()*bc_dicc["WJ1200to2500"]+wj2500toinf.values()*bc_dicc["WJ2500toinf"]+\
        dy50to100.values()*bc_dicc["DY50to100"]+dy100to250.values()*bc_dicc["DY100to250"]+\
        dy250to400.values()*bc_dicc["DY250to400"]+dy400to650.values()*bc_dicc["DY400to650"]+\
        dy650toinf.values()*bc_dicc["DY650toinf"]
    
    return sum_bcg

def graf_eficience_sum_back(num,den,num_axis,labels,labelsx="",labelsy="",colorg="black",colorb="black",labelb="",
                   namesave="",bar_error=False,legenloc=2,fontsize_label=30,
                   save=False,ymin=0.8,ymax=1.1,xmin=0,xmax=600):
    #hep.cms.lumitext("(13 TeV)")
    #hep.cms.text("Work in Progress")
    eficience=np.array(num/den)
    bines=np.array(get_axis(num_axis))
    eficience[np.isnan(eficience)] = 0
    hep.histplot(eficience,bins=bines,label=labels,color = colorg,
                 linewidth=2)
    
    if bar_error:
        el_err = error(num, den)
        hep.histplot(eficience,bins=bines,yerr=el_err,histtype='errorbar',fmt="k",
             capsize=3,color=colorg,linewidth=1.5)    
    
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)
    plt.legend(loc = legenloc,fontsize=fontsize_label)
    plt.xlabel(labelsx)
    plt.ylabel(labelsy)
    if save:
        plt.savefig(namesave)


def sum_back_senal(num1,den1,num2,den2,title1="",
                      text_lum="",
                      label1="",
                      label2="",
                      label1b="",
                      label2b="",
                      labeltx="",
                      labelty="",
                      namesave="",
                      xmin=0,xmax=0,ymin=0,ymax=1.1,
                      size=(12,12),save=False):
    plt.figure(figsize=size)
    hep.cms.lumitext(text_lum,fontsize=24)
    hep.cms.text(title1,fontsize=26)
    
    graf_eficience(num2,den2,bar_error=True,
                   labels=label1,colorg="mediumblue",colorb="crimson",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin)
    
    graf_eficience_sum_back(num1,den1,num2,bar_error=True,
                   labels=label2,colorg="green",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
    
    
    
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)

    if save:
        plt.savefig(namesave)

def sum_back_wprime(num1,den1,num2,den2,num3,den3,num4,den4,title1="",
                      text_lum="",
                      label1="",
                      label2="",
                      label3="",
                      label4="",
                      label1b="",
                      label2b="",
                      labeltx="",
                      labelty="",
                      namesave="",
                      xmin=0,xmax=0,ymin=0,ymax=1.1,
                      size=(12,12),save=False):
    plt.figure(figsize=size)
    hep.cms.lumitext(text_lum,fontsize=24)
    hep.cms.text(title1,fontsize=26)
    
    graf_eficience(num4,den4,bar_error=True,
                   labels=label4,colorg="dimgray",colorb="dimgray",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin)    
    
    graf_eficience(num3,den3,bar_error=True,
               labels=label3,colorg="orangered",colorb="orangered",
               labelsx=labeltx,
               labelsy=labelty,
              xmin=xmin,xmax=xmax,ymin=ymin)
    
    graf_eficience(num2,den2,bar_error=True,
                   labels=label1,colorg="mediumblue",colorb="crimson",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin)
    
    graf_eficience_sum_back(num1,den1,num2,bar_error=True,
                   labels=label2,colorg="green",
                   labelsx=labeltx,
                   labelsy=labelty,
                  xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
    
    
    plt.legend(loc = 2,fontsize=18)
    plt.ylim(ymin,ymax)
    plt.xlim(xmin,xmax)

    if save:
        plt.savefig(namesave)