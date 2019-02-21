{
  TFile file0("pipipi0_1.root") ;
  TTree* tree = (TTree*)file0.Get("DalitzEventList") ;

  TH1F hTimeD0("hTimeD0", "", 100, 0., 4.1) ;
  TH1F hTimeD0bar("hTimeD0bar", "", 100, 0., 4.1) ;
  TCanvas cD0 ;
  tree->Draw("decaytime >> hTimeD0", "tag == 1") ;
  TCanvas cD0bar ;
  tree->Draw("decaytime >> hTimeD0bar", "tag == -1") ;

  // Get the mean decay time and its uncertainty.
  double meanD0 = hTimeD0.GetMean() ;
  double meanErrorD0 = hTimeD0.GetMeanError() ;
  
  double meanD0bar = hTimeD0bar.GetMean() ;
  double meanErrorD0bar = hTimeD0bar.GetMeanError() ;

  // Add the calculation here.
  double aGamma = (meanD0bar - meanD0)/(meanD0bar + meanD0);
  //std:: cout<<"AGamma "<<aGamma<<endl;
  //output AGAMMA data in into a file
  ofstream outfile("../results.txt");
  std:: outfile<<" "<<aGamma<<" "<<endl;
  outfile.close();

  //relative uncertainty propagation mGamma/AGamma
  //double aGammaError = 2.0*meanD0/(meanD0bar*meanD0bar - meanD0*meanD0)*meanErrorD0bar - 2.0*meanD0bar/(meanD0bar*meanD0bar - meanD0*meanD0)*meanErrorD0 ;
  //absolute uncertainty propagation mGamma
  double aGammaError =sqrt(std::pow(2.0*meanD0/((meanD0bar+meanD0)*(meanD0bar+meanD0)), 2)*meanErrorD0bar*meanErrorD0bar + std::pow(2.0*meanD0bar/((meanD0bar+meanD0)*(meanD0bar+meanD0)), 2)*meanErrorD0*meanErrorD0) ;
  //std:: cout<<"AGamma uncertainty propagation "<<aGammaError<<endl;
  //output Variance in into a file
  ofstream outfile("../results.txt");
  std:: outfile<<" "<<aGammaError<<" "<<endl;
  outfile.close();


  TH1F hAsymmetry("hAsymmetry", "", 100, 0., 4.1) ;
  for(unsigned i = 1 ; i < hTimeD0.GetNbinsX() ; ++i){
    double nD0 = hTimeD0.GetBinContent(i) ;
    double nD0Error = hTimeD0.GetBinError(i) ;
    double nD0bar = hTimeD0bar.GetBinContent(i) ;
    double nD0barError = hTimeD0bar.GetBinError(i) ;

    if (nD0bar+nD0!=0){
    // Calculate the asymmetry and its error here.
    double asymmetry = (nD0bar - nD0)/(nD0bar + nD0);
    // relative uncertainty
    //double asymmetryError = 2.0*nD0/(nD0bar*nD0bar - nD0*nD0)*nD0barError - 2.0*nD0bar/(nD0bar*nD0bar - nD0*nD0)*nD0Error ;
    //absolute standard deviation
    double asymmetryError = sqrt(std::pow(2.0*nD0/((nD0bar+nD0)*(nD0bar+nD0)), 2)*nD0barError*nD0barError + std::pow(2.0*nD0bar/((nD0bar+nD0)*(nD0bar+nD0)), 2)*nD0Error*nD0Error) ;
  
    hAsymmetry.SetBinContent(i, asymmetry) ;
    hAsymmetry.SetBinError(i, asymmetryError) ;
  }

    else{
      double asymmetry=0.0;
      double asymmetryError=0.0;
  
    hAsymmetry.SetBinContent(i, asymmetry) ;
    hAsymmetry.SetBinError(i, asymmetryError) ;
    }

  }

  TCanvas cAsymmetry ;
  hAsymmetry.Draw() ;
}

