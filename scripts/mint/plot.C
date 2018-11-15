
{
  TFile file0("pipipi0_1.root") ;
  TTree* tree = (TTree*)file0.Get("DalitzEventList") ;
  TCanvas c1 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2", "tag==1") ;
  TCanvas c2 ;
  tree->Draw("(_1_pi#_E + _2_pi~_E)^2 - (_1_pi#_Px + _2_pi~_Px)^2 - (_1_pi#_Py + _2_pi~_Py)^2 - (_1_pi#_Pz + _2_pi~_Pz)^2", "tag==-1") ;
}  
