
{
  gStyle->SetOptStat(0) ;
  TFile file0("pipipi0_1.root") ;
  TTree* tree = (TTree*)file0.Get("DalitzEventList") ;

  TCanvas c1 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2 : (_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2 >> histo1", "tag==1", "colz") ;
  TH2F* histo = (TH2F*)gDirectory->Get("histo1") ;
  histo->SetXTitle("m^{2}(#pi^{+}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{+}#pi^{-})") ;
  histo->SetTitle("D^{0}") ;


  TCanvas c2 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2 : (_2_pi~_E + _3_pi0_E)^2 - (_2_pi~_Px + _3_pi0_Px)^2 - (_2_pi~_Py + _3_pi0_Py)^2 - (_2_pi~_Pz + _3_pi0_Pz)^2 >> histo2", "tag==1", "colz") ;
  histo = (TH2F*)gDirectory->Get("histo2") ;
  histo->SetXTitle("m^{2}(#pi^{-}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{+}#pi^{-})") ;
  histo->SetTitle("D^{0}") ;

  

  TCanvas c3 ;
  tree->Draw("(_3_pi0_E + _2_pi~_E)^2 - (_3_pi0_Px + _2_pi~_Px)^2 - (_3_pi0_Py + _2_pi~_Py)^2 - (_3_pi0_Pz + _2_pi~_Pz)^2 : (_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2 >> histo3", "tag==1", "colz") ;
  histo = (TH2F*)gDirectory->Get("histo3") ;
  histo->SetXTitle("m^{2}(#pi^{+}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{-}#pi^{0})") ;
  histo->SetTitle("D^{0}") ;


  TCanvas c4 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2 : (_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2 >> histo4", "tag==-1", "colz") ;
  histo = (TH2F*)gDirectory->Get("histo4") ;
  histo->SetXTitle("m^{2}(#pi^{+}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{+}#pi^{-})") ;
  histo->SetTitle("bar{D}^{0}") ;


  TCanvas c5 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2 : (_2_pi~_E + _3_pi0_E)^2 - (_2_pi~_Px + _3_pi0_Px)^2 - (_2_pi~_Py + _3_pi0_Py)^2 - (_2_pi~_Pz + _3_pi0_Pz)^2 >> histo5", "tag==-1", "colz") ;
  histo = (TH2F*)gDirectory->Get("histo5") ;
  histo->SetXTitle("m^{2}(#pi^{-}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{+}#pi^{-})") ;
  histo->SetTitle("bar{D}^{0}") ;

  

  TCanvas c6 ;
  tree->Draw("(_3_pi0_E + _2_pi~_E)^2 - (_3_pi0_Px + _2_pi~_Px)^2 - (_3_pi0_Py + _2_pi~_Py)^2 - (_3_pi0_Pz + _2_pi~_Pz)^2 : (_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2 >> histo6", "tag==-1", "colz") ;
  histo = (TH2F*)gDirectory->Get("histo6") ;
  histo->SetXTitle("m^{2}(#pi^{+}#pi^{0})") ;
  histo->SetYTitle("m^{2}(#pi^{-}#pi^{0})") ;
  histo->SetTitle("bar{D}^{0}") ;


}  

