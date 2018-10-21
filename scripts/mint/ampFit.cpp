// author: Jonas Rademacker (Jonas.Rademacker@bristol.ac.uk)
// status:  Mon 9 Feb 2009 19:18:01 GMT
#include "Mint/FitParameter.h"
#include "Mint/NamedParameter.h"
#include "Mint/Minimiser.h"
#include "Mint/Neg2LL.h"
#include "Mint/Neg2LLSum.h"
#include "Mint/DalitzEventList.h"

#include "Mint/CLHEPPhysicalConstants.h"


#include "Mint/PdfBase.h"
#include "Mint/DalitzPdfBase.h"
#include "Mint/DalitzPdfBaseFastInteg.h"
#include "Mint/DalitzSumPdf.h"

#include "Mint/FitAmplitude.h"
#include "Mint/FitAmpSum.h"
#include "Mint/FitAmpIncoherentSum.h"

#include "Mint/DalitzEvent.h"

#include "Mint/AmpRatios.h"

#include "Mint/IEventGenerator.h"
#include "Mint/DalitzBWBoxSet.h"
#include "Mint/DalitzBoxSet.h"

#include "Mint/SignalGenerator.h"
#include "Mint/FromFileGenerator.h"

#include "Mint/LASSO.h"

#include "TGraph.h"
#include "TFile.h"
#include "TCanvas.h"

#include "TRandom2.h"
#include "TRandom3.h"
#include <ctime>

#include <iostream>

#include "Mint/DalitzPdfNormChecker.h"
#include "Mint/DalitzPdfBaseFlexiFastInteg.h"


#include "Mint/Chi2Binning.h"

using namespace std;
using namespace MINT;

int ampFit(){
  time_t startTime = time(0);

  TRandom3 ranLux;
  NamedParameter<int> RandomSeed("RandomSeed", 0);
  ranLux.SetSeed((int)RandomSeed);
  gRandom = &ranLux;

  FitAmplitude::AutogenerateFitFile();

  NamedParameter<double>  lambda("lambda", 1.);

  NamedParameter<string> IntegratorEventFile("IntegratorEventFile"
					     , (std::string) "SignalIntegrationEvents"
					     , (char*) 0);
  string SgIntegratorEventFile1 = "Sg" + ((string)IntegratorEventFile) + "_1.root";

  NamedParameter<string> IntegratorInputFile("IntegratorInputFile"
					     , (std::string) "sgIntegrator"
					     , (char*) 0);
  NamedParameter<int>  Nevents("Nevents", 10000);
  NamedParameter<int>  doScan("doScan", 0);
  NamedParameter<std::string> integMethod("IntegMethod", (std::string) "efficient");
  NamedParameter<double> integPrecision("IntegPrecision", 1.e-4);

  NamedParameter<int> EventPattern("Event Pattern", 421, -321, 211, 211, -211);
  DalitzEventPattern pat(EventPattern.getVector());
  DalitzEventPattern cpPat(pat) ;
  cpPat[0].antiThis() ;

  SignalGenerator genD0(pat);
  SignalGenerator genD0bar(cpPat);

  NamedParameter<int> doNormCheck("doNormCheck", 0);
  NamedParameter<int> saveEvents("SaveEvents", 1);
  NamedParameter<int> doFinalStats("DoFinalStats", 1);
  NamedParameter<int> genTimeDependent("genTimeDependent", 0);
  cout << " got event pattern: " << pat << endl;


  DalitzEventList eventList1 ;

  cout << "Generating " << Nevents << " signal events (1)." << endl;
  list<int> tags ;
  list<double> taus ;
  int startTimeGen(time(0)) ;
  for(int i = 0 ; i < Nevents ; ++i){
    // Decide if it's a D0 or D0bar that's being generated.
    DalitzEventPattern* evtpat(&pat) ;
    SignalGenerator* gen(&genD0) ;
    int tag = 1 ;
    if(ranLux.Rndm() > 0.5){
      evtpat = &cpPat ;
      gen = &genD0bar ;
      tag = -1 ;
    }
    tags.push_back(tag) ;

    // Generate the decay time of the candidate.
    double lifetime = 0.4101 ; // ps
    double tau = ranLux.Exp(lifetime) ;
    taus.push_back(tau) ;

    cout << "Generating candidate " << i << " (" << (time(0)-startTimeGen)/float(i) << " s per candidate)" << endl ;
    if(genTimeDependent){
      // Make the amplitude model a combination of D0 and D0bar as a function of
      // the generated decay time.
      complex<double> coeffprod(1., 0.) ;
      complex<double> coeffmix(0., 0.) ;
      
      complex<double> ratio(coeffmix/coeffprod) ;
      SignalGenerator gentimedep(*evtpat,
				 sqrt(ratio.real()*ratio.real() + ratio.imag()*ratio.imag()), // magnitude.
				 ratio.real() != 0. ? atan(ratio.imag()/ratio.real()) : TMath::Pi()/2. // phase.
				 ) ;
      gentimedep.FillEventList(eventList1, 1);
    }
    else {
      gen->FillEventList(eventList1, 1);
    }
  }
  
  if((int) saveEvents){
    eventList1.save("pipipi0_1.root");
    TFile tuplefile("pipipi0_1.root", "update") ;
    TNtupleD* ntuple = (TNtupleD*)tuplefile.Get("DalitzEventList") ;
    int tag(0) ;
    double tau(0.) ;
    TBranch* tagbranch = ntuple->Branch("tag", &tag, "tag/I") ;
    TBranch* taubranch = ntuple->Branch("decaytime", &tau, "decaytime/D") ;
    list<int>::const_iterator itag = tags.begin() ;
    list<double>::const_iterator itau = taus.begin() ;
    for(int i = 0 ; i < Nevents ; ++i){
      tag = *itag ;
      tau = *itau ;
      tagbranch->Fill() ;
      taubranch->Fill() ;
      ++itag ;
      ++itau ;
    }
    ntuple->Write(ntuple->GetName(), TObject::kWriteDelete) ;
    tuplefile.Close() ;
  }
  
  DalitzHistoSet datH = eventList1.histoSet();
  datH.save("plotsFromEventList.root");

  cout << " ampFit done. Took " << (time(0) - startTime)/60. 
       << " min. Returning 0." << endl;
  return 0;
}


int main(){

  return ampFit();

}
//
