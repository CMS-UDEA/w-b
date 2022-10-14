import GraphicWb as gw
import pickle
import warnings
import matplotlib.pyplot as plt
import utils as utl
warnings.filterwarnings('ignore')

year="2016"

#procesor without remove overlap
trigger_processor="triggerEffWbProcessor"
fecha="2022-05-05"

# luminosity
luminosity={"2016":"35.9","2017":"41.5","2018":"59.8"}


#weight without remove overlap
bc_dicc={"2016":{"tt":0.0695,"ST":0.0205,"WW":0.2711,"WZ":0.2204,"ZZ":0.5389,
                "WJ70to100":2.9832,"WJ100to200":3.0141,"WJ200to400":0.9535,
                 "WJ400to600":3.0919,"WJ600to800":0.2297,"WJ800to1200":0.1332,
                 "WJ1200to2500":0.0294,"WJ2500toinf":0.0012,"DY50to100":0.1316,
                 "DY100to250":0.0419,"DY250to400":0.0069,"DY400to650":0.0093,"DY650toinf":0.0009},
        "2017":{"tt":0.0358,"ST":0.0104,"WW":0.3100,"WZ":0.2475,"ZZ":0.2531,
               "WJ70to100":1.4835,"WJ100to200":1.4155,"WJ200to400":0.4258,
                 "WJ400to600":1.7657,"WJ600to800":0.1103,"WJ800to1200":0.0512,
                 "WJ1200to2500":0.0135,"WJ2500toinf":0.0014,"DY50to100":0.1536,
                 "DY100to250":0.0506,"DY250to400":0.0081,"DY400to650":0.0109,"DY650toinf":0.0010},
        "2018":{"tt":0.0372,"ST":0.0106,"WW":0.4532,"WZ":0.3531,"ZZ":0.2530,
               "WJ70to100":1.4388,"WJ100to200":1.4710,"WJ200to400":0.4458,
                 "WJ400to600":0.4693,"WJ600to800":0.1154,"WJ800to1200":0.0537,
                 "WJ1200to2500":0.0140,"WJ2500toinf":0.0011,"DY50to100":0.2233,
                 "DY100to250":0.0715,"DY250to400":0.0118,"DY400to650":0.0158,"DY650toinf":0.0015}}


print("Year:",year, "-Processor:",trigger_processor,"-Fecha:",fecha)

#MC
data1="SingleMuon"
data2="TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8"
data3="ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8"
data4="WW_TuneCP5_13TeV-pythia8"
data5="WZ_TuneCP5_13TeV-pythia8"
data6="ZZ_TuneCP5_13TeV-pythia8"


data7="WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8"
data8="WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8"
data9="WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8"
data10="WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8"
data11="WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8"
data12="WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8"
data13="WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8"
data14="WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8"



data15="DYJetsToLL_Pt-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8"
data16="DYJetsToLL_Pt-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8"
data17="DYJetsToLL_Pt-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8"
data18="DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8"
data19="DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8"

data20="signal_electron_1tev"
data21="signal_electron_2tev"

# archivo 1

url1=year+"-"+trigger_processor+"-"+data1+"-"+fecha#"triggerEffWbProcessor-SingleMuon-2022-03-28:04:12"
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url1+".pkl", 'rb') as handle:
    SingleMuon = pickle.load(handle)
# archivo 2

url2=year+"-"+trigger_processor+"-"+data2+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url2+".pkl", 'rb') as handle:
    tt_bar = pickle.load(handle)

# archivo 3

url3=year+"-"+trigger_processor+"-"+data3+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url3+".pkl", 'rb') as handle:
    st = pickle.load(handle)
# archivo 4

url4=year+"-"+trigger_processor+"-"+data4+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url4+".pkl", 'rb') as handle:
    ww = pickle.load(handle)

# archivo 5
url5=year+"-"+trigger_processor+"-"+data5+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url5+".pkl", 'rb') as handle:
    wz = pickle.load(handle)

# archivo 6
url6=year+"-"+trigger_processor+"-"+data6+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url6+".pkl", 'rb') as handle:
    zz = pickle.load(handle)
    
# archivo 7    
url7=year+"-"+trigger_processor+"-"+data7+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url7+".pkl", 'rb') as handle:
    wj70to100 = pickle.load(handle)

# archivo 8
url8=year+"-"+trigger_processor+"-"+data8+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url8+".pkl", 'rb') as handle:
    wj100to200 = pickle.load(handle)

# archivo 9
url9=year+"-"+trigger_processor+"-"+data9+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url9+".pkl", 'rb') as handle:
    wj200to400 = pickle.load(handle)

# archivo 10
url10=year+"-"+trigger_processor+"-"+data10+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url10+".pkl", 'rb') as handle:
    wj400to600 = pickle.load(handle)

# archivo 11
url11=year+"-"+trigger_processor+"-"+data11+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url11+".pkl", 'rb') as handle:
    wj600to800 = pickle.load(handle)

# archivo 12
url12=year+"-"+trigger_processor+"-"+data12+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url12+".pkl", 'rb') as handle:
    wj800to1200 = pickle.load(handle)

# archivo 13
url13=year+"-"+trigger_processor+"-"+data13+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url13+".pkl", 'rb') as handle:
    wj1200to2500 = pickle.load(handle)

# archivo 14
url14=year+"-"+trigger_processor+"-"+data14+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url14+".pkl", 'rb') as handle:
    wj2500toinf = pickle.load(handle)

# archivo 15
url15=year+"-"+trigger_processor+"-"+data15+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url15+".pkl", 'rb') as handle:
    dy50to100 = pickle.load(handle)

# archivo 16
url16=year+"-"+trigger_processor+"-"+data16+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url16+".pkl", 'rb') as handle:
    dy100to250 = pickle.load(handle)

# archivo 17
url17=year+"-"+trigger_processor+"-"+data17+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url17+".pkl", 'rb') as handle:
    dy250to400 = pickle.load(handle)

# archivo 18
url18=year+"-"+trigger_processor+"-"+data18+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url18+".pkl", 'rb') as handle:
    dy400to650 = pickle.load(handle)

# archivo 19
url19=year+"-"+trigger_processor+"-"+data19+"-"+fecha
with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url19+".pkl", 'rb') as handle:
    dy650toinf = pickle.load(handle)

if year=="2017":
    url20=year+"-"+trigger_processor+"-"+data20+"-"+fecha
    with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url20+".pkl", 'rb') as handle:
        wprime1tev = pickle.load(handle)
        
    url21=year+"-"+trigger_processor+"-"+data21+"-"+fecha
    with open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+url21+".pkl", 'rb') as handle:
        wprime2tev = pickle.load(handle)
    
#=========================================electron====================================

#------------pt------------------------
def pte(sm_pt_e_tc,sm_pt_e_tr,tt_pt_e_tc,tt_pt_e_tr):
    gw.plt_one_two_eficience(sm_pt_e_tc,sm_pt_e_tr,
                  tt_pt_e_tc,tt_pt_e_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="$\\bar{tt}$",
                  label1b="$SingleMuon$ - error",
                  label2b="$\\bar{tt}$ - error",
                  title1="Preliminary -"+year,
                  labeltx="${p}_{T}(e)$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_one_two/"+year+"_Efficiency_pt_e_singlemuon_ttbar.jpg"                  
                 )
    
def scale_factor_e(sm_pt_e_tc,sm_pt_e_tr,bcg_pt_e_tc,bcg_pt_e_tr):
    efism_pt_e=gw.eficience(sm_pt_e_tc,sm_pt_e_tr)
    efitt_pt_e=gw.eficience(bcg_pt_e_tc,bcg_pt_e_tr)
    gw.graf_scalefactor(efism_pt_e,efitt_pt_e,
                 labels="Scale_factor ${p}_{T}(e)$",
                 labelsx="${p}_{T}(e)$ [GeV]",
                 labelsy="Scale_factor",
                 text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                binx=sm_pt_e_tc,
                title1="Preliminary -"+year,
                xmin=0,xmax=550,ymin=0,
                bar_error=False,
                legenloc=8,colorg="b",fontsize_label=20,
                save=True,
                namesave="./out_plots_alexis/"+fecha+"/"+year+"/scalefactor/"+year+"_scalefactor_pt_e_singlemuon_ttbar.jpg")

def several_plot(list_pt_graph,list_label,lista_color):
    gw.several_plot_eficience(list_pt_graph,
                       list_label,
                       lista_color,
                       title1="Preliminary -" +year,
                       labeltx="${p}_{T}(e)$ [GeV]",
                       labelty="Efficiency",
                       text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                       legenloc=1,
                       fontsize_label=15,
                       xmin=0,xmax=550,ymin=0,ymax=1.3,
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_several/"+year+"_Efficiency_pt_e.jpg"
                      )
def sum_back_pt_e(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr):
    gw.sum_back_senal(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr,
                  xmin=0,xmax=550,ymin=0,ymax=1.15,
                    text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                      label1="$Data$",
                      label2="Total Back",
                      title1="Preliminary -"+year,
                      labeltx="${p}_{T}(e)$ [GeV]",
                      labelty="Efficiency",
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_pt_e_singlemuon_back.jpg" )
def sum_back_pt_e_wprime(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr,
                          wprime2tev_pt_e_tc,wprime2tev_pt_e_tr,
                          wprime1tev_pt_e_tc,wprime1tev_pt_e_tr):
    gw.sum_back_wprime(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr,
                        wprime2tev_pt_e_tc,wprime2tev_pt_e_tr,
                        wprime1tev_pt_e_tc,wprime1tev_pt_e_tr,
                       
                      xmin=0,xmax=550,ymin=0,ymax=1.15,
                      text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                      label1="SingleMuon",
                      label2="Total Back",
                      label3="$W'$- 2 TeV",
                      label4="$W'$- 1 TeV",
                      title1="Preliminary -"+year,
                      labeltx="${p}_{T}(e)$ [GeV]",
                      labelty="Efficiency",
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_pt_e_wprime_back.jpg")
#------------------eta----------------------------    
def etae(sm_eta_e_tc,sm_eta_e_tr,tt_eta_e_tc,tt_eta_e_tr):
    gw.plt_one_two_eficience(sm_eta_e_tc,sm_eta_e_tr,
                  tt_eta_e_tc,tt_eta_e_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="$\\bar{tt}$",
                  label1b="$SingleMuon$ - error",
                  label2b="$\\bar{tt}$ - error",
                  title1="Preliminary -" +year,
                  labeltx=" $\eta (e)$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_one_two/"+year+"_Efficiency_eta_e_singlemuon_ttbar.jpg"                  
                 )

def scale_factor_etae(sm_eta_e_tc,sm_eta_e_tr,tt_eta_e_tc,tt_eta_e_tr):
    efism_eta_e=gw.eficience(sm_eta_e_tc,sm_eta_e_tr)
    efitt_eta_e=gw.eficience(tt_eta_e_tc,tt_eta_e_tr)
    gw.graf_scalefactor(efism_eta_e,efitt_eta_e,
                 text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                 labels="Scale_factor $\eta (e)$",
                 labelsx="$\eta (e)$",
                 labelsy="Scale_factor",
                 title1="Preliminary -"+year,
                 binx=sm_eta_e_tc,
                 xmin=-3,xmax=3,ymin=0,
                 bar_error=False,
                 legenloc=8,colorg="b",fontsize_label=20,
                 save=True,
                 namesave="./out_plots_alexis/"+fecha+"/"+year+"/scalefactor/"+year+"_scalefactor_eta_e_singlemuon_ttbar.jpg")

def several_plot_etae(list_eta_graph,list_label,lista_color):
    gw.several_plot_eficience(list_eta_graph,
                       list_label,
                       lista_color,
                       text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                       title1="Preliminary -" +year,
                       labeltx=" $\eta (e)$",
                       labelty="Efficiency",
                       legenloc=1,
                       fontsize_label=15,
                       xmin=-3,xmax=3,ymin=0,ymax=1.3,
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_several/"+year+"_Efficiency_eta_e.jpg"
                      )
def sum_back_eta_e(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr):
    gw.sum_back_senal(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",
                  title1="Preliminary -" +year,
                  labeltx=" $\eta (e)$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_eta_e_singlemuon_back.jpg"                  
                 )
    
def sum_back_eta_e_wprime(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                              wprime2tev_eta_e_tc,wprime2tev_eta_e_tr,
                              wprime1tev_eta_e_tc,wprime1tev_eta_e_tr):
    gw.sum_back_wprime(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                              wprime2tev_eta_e_tc,wprime2tev_eta_e_tr,
                              wprime1tev_eta_e_tc,wprime1tev_eta_e_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",
                  label3="$W'$- 2 TeV",
                  label4="$W'$- 1 TeV",
                  title1="Preliminary -" +year,
                  labeltx=" $\eta (e)$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_eta_e_wprime_back.jpg"                  
                 )
                      
#============================================== MET ================================================
#------------pt------------------------    
def ptmet(sm_met_tc,sm_met_tr,tt_met_tc,tt_met_tr):
    gw.plt_one_two_eficience(sm_met_tc,sm_met_tr,
                  tt_met_tc,tt_met_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="$\\bar{tt}$",
                  label1b="$SingleMuon$ - error",
                  label2b="$\\bar{tt}$ - error",
                  title1="Preliminary -" +year,
                  labeltx="$MET$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_one_two/"+year+"_Efficiency_met_singlemuon_ttbar.jpg"                  
                 )
def scale_factor_met(sm_met_tc,sm_met_tr,tt_met_tc,tt_met_tr):
    efism_met=gw.eficience(sm_met_tc,sm_met_tr)
    efitt_met=gw.eficience(tt_met_tc,tt_met_tr)
    gw.graf_scalefactor(efism_met,efitt_met,
                 labels="Scale_factor $MET$",
                 labelsx="$MET$ [GeV]",
                 labelsy="Scale_factor",
                 text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                 title1="Preliminary -"+year,
                binx=sm_met_tc,
                xmin=0,xmax=550,ymin=0,ymax=1.3,
                bar_error=False,
                legenloc=8,colorg="b",fontsize_label=20,
                save=True,
                namesave="./out_plots_alexis/"+fecha+"/"+year+"/scalefactor/"+year+"_scalefactor_met_e_singlemuon_ttbar.jpg")

def several_plot_met(list_met_graph,list_label,lista_color):
    gw.several_plot_eficience(list_met_graph,
                       list_label,
                       lista_color,
                       text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                       title1="Preliminary -" +year,
                       labeltx="$MET$ [GeV]",
                       labelty="Efficiency",
                       legenloc=1,
                       fontsize_label=15,
                       xmin=0,xmax=550,ymin=0,
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_several/"+year+"_"+year+"_Efficiency_met.jpg"
                      )
def sum_back_pt_met(bcg_pt_met_tc,bcg_pt_met_tr,sm_met_tc,sm_met_tr):
    gw.sum_back_senal(bcg_pt_met_tc,bcg_pt_met_tr,
                             sm_met_tc,sm_met_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",
                  title1="Preliminary -" +year,
                  labeltx="$MET$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_met_singlemuon_back.jpg" 
                     )
    
def sum_back_pt_met_wprime(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                              wprime2tev_eta_e_tc,wprime2tev_eta_e_tr,
                              wprime1tev_eta_e_tc,wprime1tev_eta_e_tr):
    
    gw.sum_back_wprime(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                              wprime2tev_eta_e_tc,wprime2tev_eta_e_tr,
                              wprime1tev_eta_e_tc,wprime1tev_eta_e_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",                       
                  label3="$W'$- 2 TeV",
                  label4="$W'$- 1 TeV",
                  title1="Preliminary -" +year,
                  labeltx="$MET$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_met_wprime_back.jpg" 
                     )    

#===========================b jet=====================================================

#------------pt------------------------
def ptbjet(sm_pt_bjet_tc,sm_pt_bjet_tr,tt_pt_bjet_tc,tt_pt_bjet_tr):
    gw.plt_one_two_eficience(sm_pt_bjet_tc,sm_pt_bjet_tr,
                  tt_pt_bjet_tc,tt_pt_bjet_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="$\\bar{tt}$",
                  label1b="$SingleMuon$ - error",
                  label2b="$\\bar{tt}$ - error",
                  title1="Preliminary -" +year,
                  labeltx="${p}_{T}(b-jet)$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_one_two/"+year+"_Efficiency_pt_bjet_singlemuon_back.jpg"                  
                 )
def scale_factor_ptbjet(sm_pt_bjet_tc,sm_pt_bjet_tr,tt_pt_bjet_tc,tt_pt_bjet_tr):
    efism_pt_bjet=gw.eficience(sm_pt_bjet_tc,sm_pt_bjet_tr)
    efitt_pt_bjet=gw.eficience(tt_pt_bjet_tc,tt_pt_bjet_tr)
    gw.graf_scalefactor(efism_pt_bjet,efitt_pt_bjet,
                 labels="Scale_factor ${p}_{T}(b-jet)$",
                 labelsx="${p}_{T}(b-jet)$ [GeV]",
                 labelsy="Scale_factor",
                 text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                 title1="Preliminary -"+year,
                binx=sm_pt_bjet_tc,
                xmin=0,xmax=550,ymin=0,ymax=1.2,
                bar_error=False,
                legenloc=8,colorg="b",fontsize_label=20,
                save=True,
                namesave="./out_plots_alexis/"+fecha+"/"+year+"/scalefactor/"+year+"_scalefactor_ptbjet_e_singlemuon_ttbar.jpg")

def several_plot_pt_bjet(list_pt_bjet_graph,list_label,lista_color):
    gw.several_plot_eficience(list_pt_bjet_graph,
                       list_label,
                       lista_color,
                       text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                       title1="Preliminary -" +year,
                       labeltx="${p}_{T}(b-jet)$ [GeV]",
                       labelty="Efficiency",
                       legenloc=1,
                       fontsize_label=15,
                       xmin=0,xmax=550,ymin=0,
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_several/"+year+"_Efficiency_pt_bjet.jpg"
                      )
def sum_back_pt_bjet(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr):
    gw.sum_back_senal(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",
                  title1="Preliminary -" +year,
                  labeltx="${p}_{T}(b-jet)$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_pt_bjet_singlemuon_back.jpg"          
                 )

def sum_back_pt_bjet_wprime(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr,
                              wprime2tev_pt_bjet_tc,wprime2tev_pt_bjet_tr,
                              wprime1tev_pt_bjet_tc,wprime1tev_pt_bjet_tr
                              ):
    gw.sum_back_wprime(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr,
                              wprime2tev_pt_bjet_tc,wprime2tev_pt_bjet_tr,
                              wprime1tev_pt_bjet_tc,wprime1tev_pt_bjet_tr,
                  xmin=0,xmax=550,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",                       
                  label3="$W'$- 2 TeV",
                  label4="$W'$- 1 TeV",                  
                  title1="Preliminary -" +year,
                  labeltx="${p}_{T}(b-jet)$ [GeV]",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_pt_bjet_wprime_back.jpg"          
                 )
#------------------eta----------------------------  

def etabjet(sm_eta_bjet_tc,sm_eta_bjet_tr,tt_eta_bjet_tc,tt_eta_bjet_tr):
    gw.plt_one_two_eficience(sm_eta_bjet_tc,sm_eta_bjet_tr,
                  tt_eta_bjet_tc,tt_eta_bjet_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="$\\bar{tt}$",
                  label1b="$SingleMuon$ - error",
                  label2b="$\\bar{tt}$ - error",
                  title1="Preliminary -" +year,
                  labeltx="${\eta}_{(b-jet)}$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_one_two/"+year+"_Efficiency_eta_bjet_singlemuon_ttbar.jpg"                  
                 )
    
def scale_factor_etabjet(sm_eta_bjet_tc,sm_eta_bjet_tr,tt_eta_bjet_tc,tt_eta_bjet_tr):
    efism_eta_bjet=gw.eficience(sm_eta_bjet_tc,sm_eta_bjet_tr)
    efitt_eta_bjet=gw.eficience(tt_eta_bjet_tc,tt_eta_bjet_tr)
    gw.graf_scalefactor(efism_eta_bjet,efitt_eta_bjet,
                 labels="Scale_factor ${\eta}_{(bjet)}$",
                 labelsx="${\eta}_{(b-jet)}$",
                 labelsy="Scale_factor",
                 title1="Preliminary -"+year,
                 text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                binx=sm_eta_bjet_tc,
                xmin=-3,xmax=3,ymin=0,ymax=1.2,
                bar_error=False,
                legenloc=8,colorg="b",fontsize_label=20,
                save=True,
                namesave="./out_plots_alexis/"+fecha+"/"+year+"/scalefactor/"+year+"_scalefactor_etabjet_e_singlemuon_ttbar.jpg")
    
def several_plot_etabjet(list_pt_bjet_graph,list_label,lista_color):
    gw.several_plot_eficience(list_pt_bjet_graph,
                       list_label,
                       lista_color,
                       text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                       title1="Preliminary -" +year,
                       labeltx="${\eta}_{(b-jet)}$",
                       labelty="Efficiency",
                       legenloc=1,
                       fontsize_label=15,
                       xmin=-3,xmax=3,ymin=0,
                      save=True,
                      namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_several/"+year+"_Efficiency_eta_bjet.jpg"
                      )
    
def sum_back_eta_bjet(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr):    
        gw.sum_back_senal(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",
                  title1="Preliminary -" +year,
                  labeltx="${\eta}_{(b-jet)}$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_eta_bjet_singlemuon_back.jpg"                  
                 )


def sum_back_eta_bjet_wprime(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr,
                              wprime2tev_eta_bjet_tc,wprime2tev_eta_bjet_tr,
                              wprime1tev_eta_bjet_tc,wprime1tev_eta_bjet_tr
                              ):    
        gw.sum_back_wprime(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr,
                              wprime2tev_eta_bjet_tc,wprime2tev_eta_bjet_tr,
                              wprime1tev_eta_bjet_tc,wprime1tev_eta_bjet_tr,
                  xmin=-3,xmax=3,ymin=0,
                  text_lum="("+luminosity[str(year)]+" ${fb}^{-1}$"+",13 TeV)",
                  label1="$Data$",
                  label2="Total Back",                       
                  label3="$W'$- 2 TeV",
                  label4="$W'$- 1 TeV",
                  title1="Preliminary -" +year,
                  labeltx="${\eta}_{(b-jet)}$",
                  labelty="Efficiency",
                  save=True,
                  namesave="./out_plots_alexis/"+fecha+"/"+year+"/plots_sum_back/"+year+"_Efficiency_eta_bjet_wprime_back.jpg"                  
                 )
        
if __name__ == "__main__":
    #crear carpeta
    utl.crear_carpetas(fecha)
    #=========================================electron====================================

    #------------pt------------------------
    sm_pt_e_tc=SingleMuon[data1]["pt_e_tc"]
    sm_pt_e_tr=SingleMuon[data1]["pt_e_tr"]
    
    tt_pt_e_tc=tt_bar[data2]["pt_e_tc"]
    tt_pt_e_tr=tt_bar[data2]["pt_e_tr"]
    
    st_pt_e_tc=st[data3]["pt_e_tc"]
    st_pt_e_tr=st[data3]["pt_e_tr"]
    
    ww_pt_e_tc=ww[data4]["pt_e_tc"]
    ww_pt_e_tr=ww[data4]["pt_e_tr"]
        
    wz_pt_e_tc=wz[data5]["pt_e_tc"]
    wz_pt_e_tr=wz[data5]["pt_e_tr"]
    
    zz_pt_e_tc=zz[data6]["pt_e_tc"]
    zz_pt_e_tr=zz[data6]["pt_e_tr"]   
    
    wj70to100_pt_e_tc= wj70to100[data7]["pt_e_tc"]
    wj70to100_pt_e_tr= wj70to100[data7]["pt_e_tr"]
    
    wj100to200_pt_e_tc= wj100to200[data8]["pt_e_tc"]
    wj100to200_pt_e_tr=wj100to200[data8]["pt_e_tr"]
    
    wj200to400_pt_e_tc= wj200to400[data9]["pt_e_tc"]
    wj200to400_pt_e_tr= wj200to400[data9]["pt_e_tr"]
    
    wj400to600_pt_e_tc= wj400to600[data10]["pt_e_tc"]
    wj400to600_pt_e_tr= wj400to600[data10]["pt_e_tr"]
    
    wj600to800_pt_e_tc= wj600to800[data11]["pt_e_tc"]
    wj600to800_pt_e_tr= wj600to800[data11]["pt_e_tr"]
    
    wj800to1200_pt_e_tc= wj800to1200[data12]["pt_e_tc"]
    wj800to1200_pt_e_tr= wj800to1200[data12]["pt_e_tr"]
    
    wj1200to2500_pt_e_tc= wj1200to2500[data13]["pt_e_tc"]
    wj1200to2500_pt_e_tr= wj1200to2500[data13]["pt_e_tr"]
    
    wj2500toinf_pt_e_tc= wj2500toinf[data14]["pt_e_tc"]
    wj2500toinf_pt_e_tr= wj2500toinf[data14]["pt_e_tr"]
    
    dy50to100_pt_e_tc= dy50to100[data15]["pt_e_tc"]
    dy50to100_pt_e_tr= dy50to100[data15]["pt_e_tr"]
    
    dy100to250_pt_e_tc= dy100to250[data16]["pt_e_tc"]
    dy100to250_pt_e_tr= dy100to250[data16]["pt_e_tr"]
    
    dy250to400_pt_e_tc= dy250to400[data17]["pt_e_tc"]
    dy250to400_pt_e_tr= dy250to400[data17]["pt_e_tr"]
    
    dy400to650_pt_e_tc= dy400to650[data18]["pt_e_tc"]
    dy400to650_pt_e_tr= dy400to650[data18]["pt_e_tr"]
    
    dy650toinf_pt_e_tc= dy650toinf[data19]["pt_e_tc"]
    dy650toinf_pt_e_tr= dy650toinf[data19]["pt_e_tr"]
    try:
        if year=="2017":
            wprime1tev_pt_e_tc=wprime1tev[data20]["pt_e_tc"]
            wprime1tev_pt_e_tr=wprime1tev[data20]["pt_e_tr"]

            wprime2tev_pt_e_tc=wprime2tev[data21]["pt_e_tc"]
            wprime2tev_pt_e_tr=wprime2tev[data21]["pt_e_tr"]
    except:
        pass
    
    list_pt_graph=[[sm_pt_e_tc,sm_pt_e_tr],
                [tt_pt_e_tc,tt_pt_e_tr],
                 [st_pt_e_tc,st_pt_e_tr],
                [ww_pt_e_tc,ww_pt_e_tr],
                
                ]
    list_label=["$SingleMuon$","$\\bar{tt}$","$ST$","$WW$","$WZ$"]
    lista_color=["mediumblue","green","orangered","black","m"]
    plt.figure()
    pte(sm_pt_e_tc,sm_pt_e_tr,tt_pt_e_tc,tt_pt_e_tr)
    

    plt.figure()
    several_plot(list_pt_graph,list_label,lista_color)
    
    #--------------sum back pt_e
    
    plt.figure()
    bcg_pt_e_tr=gw.sum_background(tt_pt_e_tr,st_pt_e_tr,
                                  ww_pt_e_tr,wz_pt_e_tr,zz_pt_e_tr,
                                  wj70to100_pt_e_tr,wj100to200_pt_e_tr,
                                  wj200to400_pt_e_tr,wj400to600_pt_e_tr,
                                  wj600to800_pt_e_tr,wj800to1200_pt_e_tr,
                                  wj1200to2500_pt_e_tr,wj2500toinf_pt_e_tr,
                                  dy50to100_pt_e_tr,dy100to250_pt_e_tr,
                                  dy250to400_pt_e_tr,dy400to650_pt_e_tr,
                                  dy650toinf_pt_e_tr,bc_dicc[year])

    bcg_pt_e_tc=gw.sum_background(tt_pt_e_tc,st_pt_e_tc,
                                  ww_pt_e_tc,wz_pt_e_tc,zz_pt_e_tc,
                                  wj70to100_pt_e_tc,wj100to200_pt_e_tc,
                                  wj200to400_pt_e_tc,wj400to600_pt_e_tc,
                                  wj600to800_pt_e_tc,wj800to1200_pt_e_tc,
                                  wj1200to2500_pt_e_tc,wj2500toinf_pt_e_tc,
                                  dy50to100_pt_e_tc,dy100to250_pt_e_tc,
                                  dy250to400_pt_e_tc,dy400to650_pt_e_tc,
                                  dy650toinf_pt_e_tc,bc_dicc[year])
    
    #---------------scale_factor pt_e ---------------------
    plt.figure()
    scale_factor_e(sm_pt_e_tc,sm_pt_e_tr,bcg_pt_e_tc,bcg_pt_e_tr)
    
    #----------sum back graound-----------------
    
    sum_back_pt_e(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr)
    try:
        if year=="2017":
            sum_back_pt_e_wprime(bcg_pt_e_tc,bcg_pt_e_tr,sm_pt_e_tc,sm_pt_e_tr,
                              wprime2tev_pt_e_tc,wprime2tev_pt_e_tr,
                              wprime1tev_pt_e_tc,wprime1tev_pt_e_tr)
    except:
        pass
    
    #---------------eta e
    
    sm_eta_e_tc=SingleMuon[data1]["eta_e_tc"]
    sm_eta_e_tr=SingleMuon[data1]["eta_e_tr"]

    tt_eta_e_tc=tt_bar[data2]["eta_e_tc"]
    tt_eta_e_tr=tt_bar[data2]["eta_e_tr"]

    st_eta_e_tc=st[data3]["eta_e_tc"]
    st_eta_e_tr=st[data3]["eta_e_tr"]

    ww_eta_e_tc=ww[data4]["eta_e_tc"]
    ww_eta_e_tr=ww[data4]["eta_e_tr"]
    
    
    wz_eta_e_tc=wz[data5]["eta_e_tc"]
    wz_eta_e_tr=wz[data5]["eta_e_tr"]

    zz_eta_e_tc=zz[data6]["eta_e_tc"]
    zz_eta_e_tr=zz[data6]["eta_e_tr"]
    
    
    wj70to100_eta_e_tc= wj70to100[data7]["eta_e_tc"]
    wj70to100_eta_e_tr= wj70to100[data7]["eta_e_tr"]
    
    wj100to200_eta_e_tc= wj100to200[data8]["eta_e_tc"]
    wj100to200_eta_e_tr= wj100to200[data8]["eta_e_tr"]
    
    wj200to400_eta_e_tc= wj200to400[data9]["eta_e_tc"]
    wj200to400_eta_e_tr= wj200to400[data9]["eta_e_tr"]
    
    wj400to600_eta_e_tc= wj400to600[data10]["eta_e_tc"]
    wj400to600_eta_e_tr= wj400to600[data10]["eta_e_tr"]
    
    wj600to800_eta_e_tc= wj600to800[data11]["eta_e_tc"]
    wj600to800_eta_e_tr= wj600to800[data11]["eta_e_tr"]
    
    wj800to1200_eta_e_tc= wj800to1200[data12]["eta_e_tc"]
    wj800to1200_eta_e_tr= wj800to1200[data12]["eta_e_tr"]
    
    wj1200to2500_eta_e_tc= wj1200to2500[data13]["eta_e_tc"]
    wj1200to2500_eta_e_tr= wj1200to2500[data13]["eta_e_tr"]
    
    wj2500toinf_eta_e_tc= wj2500toinf[data14]["eta_e_tc"]
    wj2500toinf_eta_e_tr= wj2500toinf[data14]["eta_e_tr"]
    
    dy50to100_eta_e_tc= dy50to100[data15]["eta_e_tc"]
    dy50to100_eta_e_tr= dy50to100[data15]["eta_e_tr"]
    
    dy100to250_eta_e_tc= dy100to250[data16]["eta_e_tc"]
    dy100to250_eta_e_tr= dy100to250[data16]["eta_e_tr"]
    
    dy250to400_eta_e_tc= dy250to400[data17]["eta_e_tc"]
    dy250to400_eta_e_tr= dy250to400[data17]["eta_e_tr"]
    
    dy400to650_eta_e_tc= dy400to650[data18]["eta_e_tc"]
    dy400to650_eta_e_tr= dy400to650[data18]["eta_e_tr"]
    
    dy650toinf_eta_e_tc= dy650toinf[data19]["eta_e_tc"]
    dy650toinf_eta_e_tr= dy650toinf[data19]["eta_e_tr"]
    try:
        if year=="2017":
            wprime1tev_eta_e_tc=wprime1tev[data20]["eta_e_tc"]
            wprime1tev_eta_e_tr=wprime1tev[data20]["eta_e_tr"]

            wprime2tev_eta_e_tc=wprime2tev[data21]["eta_e_tc"]
            wprime2tev_eta_e_tr=wprime2tev[data21]["eta_e_tr"]
    except:
        pass

    
    list_eta_graph=[[sm_eta_e_tc,sm_eta_e_tr],
                [tt_eta_e_tc,tt_eta_e_tr],
                [st_eta_e_tc,st_eta_e_tr],
               [ww_eta_e_tc,ww_eta_e_tr]]
    
    plt.figure()
    etae(sm_eta_e_tc,sm_eta_e_tr,tt_eta_e_tc,tt_eta_e_tr)

    plt.figure()
    several_plot_etae(list_eta_graph,list_label,lista_color)
    
    #--------------sum back eta_e
    plt.figure()
    bcg_eta_e_tr=gw.sum_background(tt_eta_e_tr,st_eta_e_tr,
                                   ww_eta_e_tr,wz_eta_e_tr,zz_eta_e_tr,
                                  wj70to100_eta_e_tr,wj100to200_eta_e_tr,
                                  wj200to400_eta_e_tr,wj400to600_eta_e_tr,
                                  wj600to800_eta_e_tr,wj800to1200_eta_e_tr,
                                  wj1200to2500_eta_e_tr,wj2500toinf_eta_e_tr,
                                  dy50to100_eta_e_tr,dy100to250_eta_e_tr,
                                  dy250to400_eta_e_tr,dy400to650_eta_e_tr,
                                  dy650toinf_eta_e_tr,bc_dicc[year])

    bcg_eta_e_tc=gw.sum_background(tt_eta_e_tc,st_eta_e_tc,
                                   ww_eta_e_tc,wz_eta_e_tc,zz_eta_e_tc,
                                  wj70to100_eta_e_tc,wj100to200_eta_e_tc,
                                  wj200to400_eta_e_tc,wj400to600_eta_e_tc,
                                  wj600to800_eta_e_tc,wj800to1200_eta_e_tc,
                                  wj1200to2500_eta_e_tc,wj2500toinf_eta_e_tc,
                                  dy50to100_eta_e_tc,dy100to250_eta_e_tc,
                                  dy250to400_eta_e_tc,dy400to650_eta_e_tc,
                                  dy650toinf_eta_e_tc,bc_dicc[year])
    
    plt.figure()
    scale_factor_etae(sm_eta_e_tc,sm_eta_e_tr,bcg_eta_e_tc,bcg_eta_e_tr)
    
    sum_back_eta_e(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr)
    try:
        if year=="2017":
            sum_back_eta_e_wprime(bcg_eta_e_tc,bcg_eta_e_tr,sm_eta_e_tc,sm_eta_e_tr,
                                  wprime2tev_eta_e_tc,wprime2tev_eta_e_tr,
                                  wprime1tev_eta_e_tc,wprime1tev_eta_e_tr
                                  )
    except:
        pass

    
    #============================MET=====================
    sm_met_tc=SingleMuon[data1]["met_tc"]
    sm_met_tr=SingleMuon[data1]["met_tr"]

    tt_met_tc=tt_bar[data2]["met_tc"]
    tt_met_tr=tt_bar[data2]["met_tr"]

    st_met_tc=st[data3]["met_tc"]
    st_met_tr=st[data3]["met_tr"]

    ww_met_tc=ww[data4]["met_tc"]
    ww_met_tr=ww[data4]["met_tr"]
    
    wz_met_tc=wz[data5]["met_tc"]
    wz_met_tr=wz[data5]["met_tr"]

    zz_met_tc=zz[data6]["met_tc"]
    zz_met_tr=zz[data6]["met_tr"]
    
    wj70to100_met_tc= wj70to100[data7]["met_tc"]
    wj70to100_met_tr= wj70to100[data7]["met_tr"]
    
    wj100to200_met_tc= wj100to200[data8]["met_tc"]
    wj100to200_met_tr= wj100to200[data8]["met_tr"]
    
    wj200to400_met_tc= wj200to400[data9]["met_tc"]
    wj200to400_met_tr= wj200to400[data9]["met_tr"]
    
    wj400to600_met_tc= wj400to600[data10]["met_tc"]
    wj400to600_met_tr= wj400to600[data10]["met_tr"]
    
    wj600to800_met_tc= wj600to800[data11]["met_tc"]
    wj600to800_met_tr= wj600to800[data11]["met_tr"]
    
    wj800to1200_met_tc= wj800to1200[data12]["met_tc"]
    wj800to1200_met_tr= wj800to1200[data12]["met_tr"]
    
    wj1200to2500_met_tc= wj1200to2500[data13]["met_tc"]
    wj1200to2500_met_tr= wj1200to2500[data13]["met_tr"]
    
    wj2500toinf_met_tc= wj2500toinf[data14]["met_tc"]
    wj2500toinf_met_tr= wj2500toinf[data14]["met_tr"]
    
    dy50to100_met_tc= dy50to100[data15]["met_tc"]
    dy50to100_met_tr= dy50to100[data15]["met_tr"]
    
    dy100to250_met_tc= dy100to250[data16]["met_tc"]
    dy100to250_met_tr= dy100to250[data16]["met_tr"]
    
    dy250to400_met_tc= dy250to400[data17]["met_tc"]
    dy250to400_met_tr= dy250to400[data17]["met_tr"]
    
    dy400to650_met_tc= dy400to650[data18]["met_tc"]
    dy400to650_met_tr= dy400to650[data18]["met_tr"]
    
    dy650toinf_met_tc= dy650toinf[data19]["met_tc"]
    dy650toinf_met_tr= dy650toinf[data19]["met_tr"]
    try:
        if year=="2017":
            wprime1tev_met_tc=wprime1tev[data20]["met_tc"]
            wprime1tev_met_tr=wprime1tev[data20]["met_tr"]

            wprime2tev_met_tc=wprime2tev[data21]["met_tc"]
            wprime2tev_met_tr=wprime2tev[data21]["met_tr"]
    except:
        pass
    
    
    list_met_graph=[[sm_met_tc,sm_met_tr],
                [tt_met_tc,tt_met_tr],
                [st_met_tc,st_met_tr],
               [ww_met_tc,ww_met_tr]]
    
    plt.figure()
    ptmet(sm_met_tc,sm_met_tr,tt_met_tc,tt_met_tr)

    plt.figure()
    several_plot_met(list_met_graph,list_label,lista_color)
    
    #--------------sum back met
    
    plt.figure()
    bcg_pt_met_tr=gw.sum_background(tt_met_tr,st_met_tr,
                                    ww_met_tr,wz_met_tr,zz_met_tr,
                                  wj70to100_met_tr,wj100to200_met_tr,
                                  wj200to400_met_tr,wj400to600_met_tr,
                                  wj600to800_met_tr,wj800to1200_met_tr,
                                  wj1200to2500_met_tr,wj2500toinf_met_tr,
                                  dy50to100_met_tr,dy100to250_met_tr,
                                  dy250to400_met_tr,dy400to650_met_tr,
                                  dy650toinf_met_tr,bc_dicc[year])

    bcg_pt_met_tc=gw.sum_background(tt_met_tc,st_met_tc,
                                    ww_met_tc,wz_met_tc,zz_met_tc,
                                  wj70to100_met_tc,wj100to200_met_tc,
                                  wj200to400_met_tc,wj400to600_met_tc,
                                  wj600to800_met_tc,wj800to1200_met_tc,
                                  wj1200to2500_met_tc,wj2500toinf_met_tc,
                                  dy50to100_met_tc,dy100to250_met_tc,
                                  dy250to400_met_tc,dy400to650_met_tc,
                                  dy650toinf_met_tc,bc_dicc[year])
    
    plt.figure()
    scale_factor_met(sm_met_tc,sm_met_tr,bcg_pt_met_tc,bcg_pt_met_tr)
    
    sum_back_pt_met(bcg_pt_met_tc,bcg_pt_met_tr,sm_met_tc,sm_met_tr)
    
    try:
        if year=="2017":
            sum_back_pt_met_wprime(bcg_pt_met_tc,bcg_pt_met_tr,sm_met_tc,sm_met_tr,
                                  wprime2tev_met_tc,wprime2tev_met_tr,
                                  wprime1tev_met_tc,wprime1tev_met_tr
                                  )
    except:
        pass
    
    #===============bjet====================
    #-------------ptbjet-----------------
    sm_pt_bjet_tc=SingleMuon[data1]["pt_bjet_tc"]
    sm_pt_bjet_tr=SingleMuon[data1]["pt_bjet_tr"]

    tt_pt_bjet_tc=tt_bar[data2]["pt_bjet_tc"]
    tt_pt_bjet_tr=tt_bar[data2]["pt_bjet_tr"]

    st_pt_bjet_tc=st[data3]["pt_bjet_tc"]
    st_pt_bjet_tr=st[data3]["pt_bjet_tr"]

    ww_pt_bjet_tc=ww[data4]["pt_bjet_tc"]
    ww_pt_bjet_tr=ww[data4]["pt_bjet_tr"]
    
    wz_pt_bjet_tc=wz[data5]["pt_bjet_tc"]
    wz_pt_bjet_tr=wz[data5]["pt_bjet_tr"]

    zz_pt_bjet_tc=zz[data6]["pt_bjet_tc"]
    zz_pt_bjet_tr=zz[data6]["pt_bjet_tr"]
    
    wj70to100_pt_bjet_tc= wj70to100[data7]["pt_bjet_tc"]
    wj70to100_pt_bjet_tr= wj70to100[data7]["pt_bjet_tr"]
    
    wj100to200_pt_bjet_tc= wj100to200[data8]["pt_bjet_tc"]
    wj100to200_pt_bjet_tr=wj100to200[data8]["pt_bjet_tr"]
    
    wj200to400_pt_bjet_tc= wj200to400[data9]["pt_bjet_tc"]
    wj200to400_pt_bjet_tr= wj200to400[data9]["pt_bjet_tr"]
    
    wj400to600_pt_bjet_tc= wj400to600[data10]["pt_bjet_tc"]
    wj400to600_pt_bjet_tr= wj400to600[data10]["pt_bjet_tr"]
    
    wj600to800_pt_bjet_tc= wj600to800[data11]["pt_bjet_tc"]
    wj600to800_pt_bjet_tr= wj600to800[data11]["pt_bjet_tr"]
    
    wj800to1200_pt_bjet_tc= wj800to1200[data12]["pt_bjet_tc"]
    wj800to1200_pt_bjet_tr= wj800to1200[data12]["pt_bjet_tr"]
    
    wj1200to2500_pt_bjet_tc= wj1200to2500[data13]["pt_bjet_tc"]
    wj1200to2500_pt_bjet_tr= wj1200to2500[data13]["pt_bjet_tr"]
    
    wj2500toinf_pt_bjet_tc= wj2500toinf[data14]["pt_bjet_tc"]
    wj2500toinf_pt_bjet_tr= wj2500toinf[data14]["pt_bjet_tr"]
    
    dy50to100_pt_bjet_tc= dy50to100[data15]["pt_bjet_tc"]
    dy50to100_pt_bjet_tr= dy50to100[data15]["pt_bjet_tr"]
    
    dy100to250_pt_bjet_tc= dy100to250[data16]["pt_bjet_tc"]
    dy100to250_pt_bjet_tr= dy100to250[data16]["pt_bjet_tr"]
    
    dy250to400_pt_bjet_tc= dy250to400[data17]["pt_bjet_tc"]
    dy250to400_pt_bjet_tr= dy250to400[data17]["pt_bjet_tr"]
    
    dy400to650_pt_bjet_tc= dy400to650[data18]["pt_bjet_tc"]
    dy400to650_pt_bjet_tr= dy400to650[data18]["pt_bjet_tr"]
    
    dy650toinf_pt_bjet_tc= dy650toinf[data19]["pt_bjet_tc"]
    dy650toinf_pt_bjet_tr= dy650toinf[data19]["pt_bjet_tr"]
    
    try:
        if year=="2017":
            wprime1tev_pt_bjet_tc=wprime1tev[data20]["pt_bjet_tc"]
            wprime1tev_pt_bjet_tr=wprime1tev[data20]["pt_bjet_tr"]

            wprime2tev_pt_bjet_tc=wprime2tev[data21]["pt_bjet_tc"]
            wprime2tev_pt_bjet_tr=wprime2tev[data21]["pt_bjet_tr"]
    except:
        pass
    
    list_pt_bjet_graph=[[sm_pt_bjet_tc,sm_pt_bjet_tr],
                [tt_pt_bjet_tc,tt_pt_bjet_tr],
                [st_pt_bjet_tc,st_pt_bjet_tr],
               [ww_pt_bjet_tc,ww_pt_bjet_tr]]
    plt.figure()
    ptbjet(sm_pt_bjet_tc,sm_pt_bjet_tr,tt_pt_bjet_tc,tt_pt_bjet_tr)

    plt.figure()
    several_plot_pt_bjet(list_pt_bjet_graph,list_label,lista_color)
    
    #--------------sum back pt bjet
    plt.figure()
    bcg_pt_bjet_tr=gw.sum_background(tt_pt_bjet_tr,st_pt_bjet_tr,
                                     ww_pt_bjet_tr,wz_pt_bjet_tr,zz_pt_bjet_tr,
                                  wj70to100_pt_bjet_tr,wj100to200_pt_bjet_tr,
                                  wj200to400_pt_bjet_tr,wj400to600_pt_bjet_tr,
                                  wj600to800_pt_bjet_tr,wj800to1200_pt_bjet_tr,
                                  wj1200to2500_pt_bjet_tr,wj2500toinf_pt_bjet_tr,
                                  dy50to100_pt_bjet_tr,dy100to250_pt_bjet_tr,
                                  dy250to400_pt_bjet_tr,dy400to650_pt_bjet_tr,
                                  dy650toinf_pt_bjet_tr,bc_dicc[year])

    bcg_pt_bjet_tc=gw.sum_background(tt_pt_bjet_tc,st_pt_bjet_tc,
                                     ww_pt_bjet_tc,wz_pt_bjet_tc,zz_pt_bjet_tc,
                                  wj70to100_pt_bjet_tc,wj100to200_pt_bjet_tc,
                                  wj200to400_pt_bjet_tc,wj400to600_pt_bjet_tc,
                                  wj600to800_pt_bjet_tc,wj800to1200_pt_bjet_tc,
                                  wj1200to2500_pt_bjet_tc,wj2500toinf_pt_bjet_tc,
                                  dy50to100_pt_bjet_tc,dy100to250_pt_bjet_tc,
                                  dy250to400_pt_bjet_tc,dy400to650_pt_bjet_tc,
                                  dy650toinf_pt_bjet_tc,bc_dicc[year])
    
    plt.figure()
    scale_factor_ptbjet(sm_pt_bjet_tc,sm_pt_bjet_tr,bcg_pt_bjet_tc,bcg_pt_bjet_tr)
    
    sum_back_pt_bjet(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr)
    try:
        if year=="2017":
            sum_back_pt_bjet_wprime(bcg_pt_bjet_tc,bcg_pt_bjet_tr,sm_pt_bjet_tc,sm_pt_bjet_tr,
                                  wprime2tev_pt_bjet_tc,wprime2tev_pt_bjet_tr,
                                  wprime1tev_pt_bjet_tc,wprime1tev_pt_bjet_tr
                                  )
    except:
        pass
    
    #-----------eta_bjet
    
    sm_eta_bjet_tc=SingleMuon[data1]["eta_bjet_tc"]
    sm_eta_bjet_tr=SingleMuon[data1]["eta_bjet_tr"]

    tt_eta_bjet_tc=tt_bar[data2]["eta_bjet_tc"]
    tt_eta_bjet_tr=tt_bar[data2]["eta_bjet_tr"]

    st_eta_bjet_tc=st[data3]["eta_bjet_tc"]
    st_eta_bjet_tr=st[data3]["eta_bjet_tr"]

    ww_eta_bjet_tc=ww[data4]["eta_bjet_tc"]
    ww_eta_bjet_tr=ww[data4]["eta_bjet_tr"]
    
    wz_eta_bjet_tc=wz[data5]["eta_bjet_tc"]
    wz_eta_bjet_tr=wz[data5]["eta_bjet_tr"]

    zz_eta_bjet_tc=zz[data6]["eta_bjet_tr"]
    zz_eta_bjet_tr=zz[data6]["eta_bjet_tr"]
    
    
    wj70to100_eta_bjet_tc= wj70to100[data7]["eta_bjet_tc"]
    wj70to100_eta_bjet_tr= wj70to100[data7]["eta_bjet_tr"]
    
    wj100to200_eta_bjet_tc= wj100to200[data8]["eta_bjet_tc"]
    wj100to200_eta_bjet_tr= wj100to200[data8]["eta_bjet_tr"]
    
    wj200to400_eta_bjet_tc= wj200to400[data9]["eta_bjet_tc"]
    wj200to400_eta_bjet_tr= wj200to400[data9]["eta_bjet_tr"]
    
    wj400to600_eta_bjet_tc= wj400to600[data10]["eta_bjet_tc"]
    wj400to600_eta_bjet_tr= wj400to600[data10]["eta_bjet_tr"]
    
    wj600to800_eta_bjet_tc= wj600to800[data11]["eta_bjet_tc"]
    wj600to800_eta_bjet_tr= wj600to800[data11]["eta_bjet_tr"]
    
    wj800to1200_eta_bjet_tc= wj800to1200[data12]["eta_bjet_tc"]
    wj800to1200_eta_bjet_tr= wj800to1200[data12]["eta_bjet_tr"]
    
    wj1200to2500_eta_bjet_tc= wj1200to2500[data13]["eta_bjet_tc"]
    wj1200to2500_eta_bjet_tr= wj1200to2500[data13]["eta_bjet_tr"]
    
    wj2500toinf_eta_bjet_tc= wj2500toinf[data14]["eta_bjet_tc"]
    wj2500toinf_eta_bjet_tr= wj2500toinf[data14]["eta_bjet_tr"]
    
    dy50to100_eta_bjet_tc= dy50to100[data15]["eta_bjet_tc"]
    dy50to100_eta_bjet_tr= dy50to100[data15]["eta_bjet_tr"]
    
    dy100to250_eta_bjet_tc= dy100to250[data16]["eta_bjet_tc"]
    dy100to250_eta_bjet_tr= dy100to250[data16]["eta_bjet_tr"]
    
    dy250to400_eta_bjet_tc= dy250to400[data17]["eta_bjet_tc"]
    dy250to400_eta_bjet_tr= dy250to400[data17]["eta_bjet_tr"]
    
    dy400to650_eta_bjet_tc= dy400to650[data18]["eta_bjet_tc"]
    dy400to650_eta_bjet_tr= dy400to650[data18]["eta_bjet_tr"]
    
    dy650toinf_eta_bjet_tc= dy650toinf[data19]["eta_bjet_tc"]
    dy650toinf_eta_bjet_tr= dy650toinf[data19]["eta_bjet_tr"]
    try:
        if year=="2017":
            wprime1tev_eta_bjet_tc=wprime1tev[data20]["eta_bjet_tc"]
            wprime1tev_eta_bjet_tr=wprime1tev[data20]["eta_bjet_tr"]

            wprime2tev_eta_bjet_tc=wprime2tev[data21]["eta_bjet_tc"]
            wprime2tev_eta_bjet_tr=wprime2tev[data21]["eta_bjet_tr"]
    except:
        pass
    
    
    list_pt_bjet_graph=[[sm_eta_bjet_tc,sm_eta_bjet_tr],
                [tt_eta_bjet_tc,tt_eta_bjet_tr],
                [st_eta_bjet_tc,st_eta_bjet_tr],
               [ww_eta_bjet_tc,ww_eta_bjet_tr]]
    
    plt.figure()
    etabjet(sm_eta_bjet_tc,sm_eta_bjet_tr,tt_eta_bjet_tc,tt_eta_bjet_tr)

    plt.figure()
    several_plot_etabjet(list_pt_bjet_graph,list_label,lista_color)

    #--------------sum back etabjet
    plt.figure()
    bcg_eta_bjet_tr=gw.sum_background(tt_eta_bjet_tr,st_eta_bjet_tr,
                                      ww_eta_bjet_tr,wz_eta_bjet_tr,zz_eta_bjet_tr,
                                  wj70to100_eta_bjet_tr,wj100to200_eta_bjet_tr,
                                  wj200to400_eta_bjet_tr,wj400to600_eta_bjet_tr,
                                  wj600to800_eta_bjet_tr,wj800to1200_eta_bjet_tr,
                                  wj1200to2500_eta_bjet_tr,wj2500toinf_eta_bjet_tr,
                                  dy50to100_eta_bjet_tr,dy100to250_eta_bjet_tr,
                                  dy250to400_eta_bjet_tr,dy400to650_eta_bjet_tr,
                                  dy650toinf_eta_bjet_tr,bc_dicc[year])

    bcg_eta_bjet_tc=gw.sum_background(tt_eta_bjet_tc,st_eta_bjet_tc,
                                      ww_eta_bjet_tc,wz_eta_bjet_tc,zz_eta_bjet_tc,
                                  wj70to100_eta_bjet_tc,wj100to200_eta_bjet_tc,
                                  wj200to400_eta_bjet_tc,wj400to600_eta_bjet_tc,
                                  wj600to800_eta_bjet_tc,wj800to1200_eta_bjet_tc,
                                  wj1200to2500_eta_bjet_tc,wj2500toinf_eta_bjet_tc,
                                  dy50to100_eta_bjet_tc,dy100to250_eta_bjet_tc,
                                  dy250to400_eta_bjet_tc,dy400to650_eta_bjet_tc,
                                  dy650toinf_eta_bjet_tc,bc_dicc[year])

    plt.figure()
    scale_factor_etabjet(sm_eta_bjet_tc,sm_eta_bjet_tr,bcg_eta_bjet_tc,bcg_eta_bjet_tr)
    
    sum_back_eta_bjet(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr)
    try:
        if year=="2017":
            sum_back_eta_bjet_wprime(bcg_eta_bjet_tc,bcg_eta_bjet_tr,sm_eta_bjet_tc,sm_eta_bjet_tr,
                                     wprime2tev_eta_bjet_tc,wprime2tev_eta_bjet_tr,
                                     wprime1tev_eta_bjet_tc,wprime1tev_eta_bjet_tr
                                    )   
    except:
        pass
    
    print("End")

