import utils as utl
import json 
import pickle
from datetime import datetime
from coffea import processor
#import TriggerEffWb as etwb
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak
import mplhep as hep
import pandas as pd
hep.style.use(hep.style.CMS)
import hist as hist2
import time
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
from coffea.nanoevents.methods import candidate, vector
from coffea.analysis_tools import Weights, PackedSelection

# we suppress ROOT warnings where our input ROOT tree has duplicate branches - these are handled correctly.
import warnings
import uproot
from coffea import processor
import warnings 
from datetime import datetime
import pickle

warnings.filterwarnings('ignore')
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVRun2LegacyAnalysis
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgHLTRunIISummary
#https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM

def transverse_mass(obj1, obj2):
    """invariant mass"""
    return np.sqrt(2 * obj1.pt * obj2.pt * (1- np.cos(obj1.delta_phi(obj2))))

class triggerEffWbProcessor(processor.ProcessorABC):
    def __init__(self,year):
        self.year=year
        print("YEAR:",self.year)
        self.make_output = lambda: {
            'sum' : 0.,
            'sum_trigger': 0.,
            'sum_muon': 0.,
            'sum_electron': 0,
            'sum_tau':0,
            'sum_met':0,
            'sum_b': 0.,            
            'sum_all' : 0.,             
            
            'pt_e_all': hist2.Hist(
                hist2.axis.Variable(
                    [30,60,90,120,150,180,210,240,300,500],  
                    name='pt_e_all'),
                ),
            
            'eta_e_all': hist2.Hist(
                hist2.axis.Regular(50,-2.4, 2.4, name='eta_e_all'),
                ),
            
            'phi_e_all': hist2.Hist(
                hist2.axis.Regular(50,-4.0, 4.0, name='phi_e_all'),
                ),
            
            'met_all': hist2.Hist(
                hist2.axis.Variable(
                    [50,75,100,125,150,175,200,300,500], 
                    name='met_all'),
                ),
            
            'met_phi_all': hist2.Hist(
                hist2.axis.Regular(50,-4.0, 4.0, name='met_phi_all'),
                ),             
           
            'pt_bjet_all': hist2.Hist(
                hist2.axis.Variable(
                    [30,60,90,120,150,180,210,240,300,500],
                    name='pt_bjet_all'),
                ),
            
             'phi_bjet_all': hist2.Hist(
                hist2.axis.Regular(50,-4.0, 4.0, name='phi_bjet_all'),
                ),
            
            'eta_bjet_all': hist2.Hist(
                hist2.axis.Regular(25, -2.1, 2.1, name='eta_bjet_all'),
                ),
            
            'transversemass_all': hist2.Hist(
                hist2.axis.Regular(100, 0, 200, name='transversemass_all'),
                )
        }
    @property 
    def accumulator(self):
        return self._accumulator

    def process(self, events):
        dataset = events.metadata['dataset']
        
        btagDeepFlavB={"2016":0.2598,"2017":0.3040,"2018":0.2783}
        
        selection = PackedSelection()
        
        output =self.make_output()
        
        output['sum'] = len(events)
        
        #b-jet
        b_jet=events.Jet[(events.Jet.jetId==6) & (events.Jet.puId==7) &(events.Jet.btagDeepFlavB>btagDeepFlavB[self.year])]
        events["bjet"]=b_jet
        
        events["transverse_mass"] = transverse_mass(events.Muon, events.MET)
        
        #trigger - para 2016 
        if self.year=="2016": 
            
            trigger_central=events.HLT.Ele27_WPTight_Gsf
        
        #trigger - para 2017 
        if self.year=="2017":

            trigger_central=events.HLT.Ele35_WPTight_Gsf
            
        #trigger - para 2018
        if self.year=="2018":

            trigger_central=events.HLT.Ele32_WPTight_Gsf
        
        #ID IDENTIFICADOR DE e y muon
        events["heeplecton"]=events.Electron[events.Electron.cutBased_HEEP] #mvaFall17V2Iso_WP90
        
        events["mediumIdmuon"]=events.Muon[events.Muon.tightId]
        
        events["Deeptau"]=events.Tau[(events.Tau.idDeepTau2017v2p1VSjet > 8 ) & (events.Tau.idDeepTau2017v2p1VSe > 1) &
                                   (events.Tau.idDeepTau2017v2p1VSmu > 1)]
                       

        #1 electron
        goodelectronselection = ((ak.sum(events.heeplecton.pt>0, axis=1)==1)
                &(((0<abs(events.heeplecton.eta)) & (abs(events.heeplecton.eta)<2.4))
                & ((1.57<abs(events.heeplecton.eta)) | (abs(events.heeplecton.eta)<1.4)))
               )

        events["electronselect"]=events.heeplecton[goodelectronselection]

        goodelectron=((ak.pad_none(events.electronselect.pt, 1)[:,0]>30))
        
        #Muon
        events["muonsid"]=events.Muon[(abs(events.mediumIdmuon.eta)<2.4) & (events.mediumIdmuon.pt>30)] 
        
        #0 muon-- NUEVA
        goodmuon=((ak.sum(events.muonsid.pt>0, axis=1)==0))

        #Tau
        
        events['tauid']=events.Tau[(abs(events.Deeptau.eta)<2.3)&(events.Deeptau.pt>20) & (events.Deeptau.dz< 0.2)]
        
        goodtau = ((ak.sum(events.tauid.pt>20, axis=1)==0))
        
        #2 b-jet - estado final - NUEVA
        
        goodbJets = ((ak.sum(events.bjet.pt>0, axis=1)==2)
            &(ak.firsts(events.bjet.pt)>20)
            &(abs(ak.firsts(events.bjet.eta))<2.1)
             )
        
        #met -NUEVA
        
        goodMet=events.MET.pt>50
        
        #seleccion
        
        
        selection.add("trigger_central",trigger_central)
        selection.add("electron",goodelectron)
        selection.add("muon",goodmuon)
        selection.add("tau", goodtau)
        selection.add("Met",goodMet)
        selection.add("bJet",goodbJets)

        
        #regions
        
        
        regions={"signal_trigger":["trigger_central"],
         "signal_e":["trigger_central","electron"],
         "signal_m":["trigger_central","electron","muon"],
         "signal_t": ["trigger_central","electron","muon","tau"],
         "signal_met":["trigger_central","electron","muon","tau","Met"],
         "signal_b":["trigger_central","electron","muon","tau","Met","bJet"],
         "signal_all":["trigger_central","electron","muon","tau","Met","bJet"],
                }
        
        #candidates
        
        events_trigger = events[selection.all(*regions["signal_trigger"])]
        events_electron = events[selection.all(*regions["signal_e"])]
        events_muon = events[selection.all(*regions["signal_m"])]
        events_tau = events[selection.all(*regions["signal_t"])]
        events_met = events[selection.all(*regions["signal_met"])]        
        events_b = events[selection.all(*regions["signal_b"])]
        events_all = events[selection.all(*regions["signal_all"])]
        

       
        output['sum_trigger'] = len(events_trigger)
        output['sum_electron'] = len(events_electron)
        output['sum_muon'] = len(events_muon)        
        output['sum_tau'] = len(events_tau)
        output['sum_met'] = len(events_met)
        output['sum_b'] = len(events_b)
        output['sum_all'] = len(events_all)
        
            
        #selection out
        # pt e
        
                
        #====ALL CUTS==============================
        
        output['pt_e_all'].fill(pt_e_all = ak.to_numpy(ak.firsts(events_all.heeplecton.pt)))
        
        #eta m
       
        output['eta_e_all'].fill(eta_e_all = ak.to_numpy(ak.firsts(events_all.heeplecton.eta)))
        
        #phi
        
        output['phi_e_all'].fill(phi_e_all = ak.to_numpy(ak.firsts(events_all.heeplecton.phi)))
        
        #Met
        
        output['met_all'].fill(met_all = ak.to_numpy(events_all.MET.pt))
        
        #phi MET
        
        output['met_phi_all'].fill(met_phi_all = ak.to_numpy(events_all.MET.phi))
        
        #pt bjet
        
        output['pt_bjet_all'].fill(pt_bjet_all = ak.to_numpy(ak.firsts(events_all.bjet.pt)))
        
        #pt bjet
        
        output['phi_bjet_all'].fill(phi_bjet_all = ak.to_numpy(ak.firsts(events_all.bjet.phi)))
        
        #eta bjet
        
        
        output['eta_bjet_all'].fill(eta_bjet_all = ak.to_numpy(ak.firsts(events_all.bjet.eta)))
        
        #Transverse mass
        
        output['transversemass_all'].fill(transversemass_all = ak.to_numpy(ak.firsts(events_all.transverse_mass), allow_missing = True))
        
        return {dataset: output}
            
    def postprocess(self, accumulator):
        return accumulator

fecha="2022-10-14"#datetime.now().strftime('%Y-%m-%d')

if __name__ == "__main__":

    from dask.distributed import Client
    
    inicio = time.time()
    utl.crear_carpetas(fecha,"out_ejecucion_alexis","out_plots_alexis")
    
    #import TriggerEffWb as etwb

    client = Client("tls://arualesb-2e1-40cern-2ech.dask.cmsaf-prod.flatiron.hollandhpc.org:8786")
    
    
    dic_data={"2017":["DYJetsToLL_Pt-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                      "DYJetsToLL_Pt-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                      "DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                      "DYJetsToLL_Pt-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                      "DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                      "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
                      "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
                      "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
                      "ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8",
                      "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8",
                      "WW_TuneCP5_13TeV-pythia8",
                      "WZ_TuneCP5_13TeV-pythia8",
                      "ZZ_TuneCP5_13TeV-pythia8",
                      "SingleElectron"]}
                
    
    for j in dic_data.keys():
        year=j
        archivos=dic_data[year]
        for i in archivos:
            f = open("./fileset/"+year+"/"+i+".txt")
            print("./fileset/"+year+"/"+i+".txt")

            # returns JSON object as
            # a dictionary
            load_data = json.load(f)
            datos=[]

            for k in range(len(load_data[i])):
                datos.append("root://xcache/"+load_data[i][k])
                
            print("DataSet:",len(datos))

            fileset={i:datos}
            #if year=="2018":
            out = processor.run_uproot_job(
                fileset,
                treename='Events',
                processor_instance=triggerEffWbProcessor(year=year),
                executor=processor.dask_executor,
                executor_args={"schema": processor.NanoAODSchema, "client":client}
            )

            procesador="triggerEffWbProcessor"
            name_archivo=year+"-"+procesador+"-"+i+"-"+fecha

            file = open("./out_ejecucion_alexis/"+fecha+"/"+year+"/"+name_archivo+".pkl",'wb')
            pickle.dump(out,file)
            file.close()
        fin = time.time()
        print("End")
        print("time execution= {} min ".format((fin-inicio)/60))