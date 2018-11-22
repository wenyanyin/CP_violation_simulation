
{
  gStyle->SetOptStat(0) ;
  TFile file0("pipipi0_1.root") ;
  TTree* tree = (TTree*)file0.Get("DalitzEventList") ;
  TCanvas c1 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2 : (_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2 >> histo", "tag==1", "colz") ;
  TH2F* histo = (TH2F*)gDirectory->Get("histo") ;
  histo->SetXTitle("m^{2}(#pi^{+}#pi^{0})") ;
  TCanvas c2 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2", "tag==-1") ;
}  
