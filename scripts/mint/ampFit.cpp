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
#include <memory>

using namespace std;
using namespace MINT;

complex<double> amp_ratio(const int tag, const double decaytime, const double mass, const double width,
			  const double deltam, const double deltagamma, const double qoverp, const double phi) {
      complex<double> coeffprod(1., 0.) ;
      complex<double> coeffmix(0., 0.) ;
      // Placeholder so it builds without complaining about unused variables.
      coeffmix.real(tag * decaytime * mass * width * deltam * deltagamma * qoverp * phi) ;
      coeffmix.real(0.) ;

      complex<double> ratio(coeffmix/coeffprod) ;
      return ratio ;
}

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
  NamedParameter<double> mass("mass", 1864.84) ;
  NamedParameter<double> lifetime("lifetime", 0.4101) ;
  double width = 1./lifetime ;
  NamedParameter<double> x("x", 0.0039) ;
  double deltam = x * mass / 197.3e-12 * 0.2998 ; // convert MeV to ps^-1.
  NamedParameter<double> y("y", 0.0065) ;
  double deltagamma = y * width ;
  NamedParameter<double> qoverp("qoverp", 1.) ;
  NamedParameter<double> phi("phi", 0.) ;

  NamedParameter<double> tmax("tmax", 10.) ;
  NamedParameter<double> sampleinterval("sampleinterval", 0.1) ;

  typedef pair<double, unique_ptr<SignalGenerator> > GenPair ;
  typedef list<GenPair> GenList ;
  typedef map<int, GenList> GenMap ;
  DalitzEventPattern* patterns[2] = {&cpPat, &pat} ;
  GenMap generators ;
  if(genTimeDependent){
    for(int tag = -1 ; tag <= 1 ; tag += 2) {
      generators[tag] = GenList() ;
      DalitzEventPattern* evtpat = patterns[(tag+1)/2] ;
      for(double decaytime = 0. ; decaytime <= tmax ; decaytime += sampleinterval){
	complex<double> ratio = amp_ratio(tag, decaytime, mass, width, deltam, deltagamma, qoverp, phi) ;
	double mag = sqrt(ratio.real()*ratio.real() + ratio.imag()*ratio.imag()) ;
	double phase = ratio.real() != 0. ? atan(ratio.imag()/ratio.real()) : TMath::Pi()/2. ;
	cout << "Builder generator with tag " << tag << " at decay time " << decaytime 
	     << ". Ratio mag.: " << mag << ", phase: " << phase << endl ;
	SignalGenerator* gen = new SignalGenerator(*evtpat, mag, phase) ;
	generators[tag].push_back(GenPair(decaytime, gen)) ;
      }
    }
  }

  cout << " got event pattern: " << pat << endl;

  DalitzEventList eventList1 ;

  cout << "Generating " << Nevents << " signal events (1)." << endl;
  list<int> tags ;
  list<double> taus ;
  int startTimeGen(time(0)) ;
  for(int i = 0 ; i < Nevents ; ++i){
    // Decide if it's a D0 or D0bar that's being generated.
    SignalGenerator* gen(&genD0) ;
    int tag = 1 ;
    if(ranLux.Rndm() > 0.5){
      gen = &genD0bar ;
      tag = -1 ;
    }
    tags.push_back(tag) ;

    // Generate the decay time of the candidate.
    double decaytime = tmax + 1. ;
    while(decaytime > tmax)
      decaytime = ranLux.Exp(lifetime) ;
    taus.push_back(decaytime) ;

    cout << "Generating candidate " << i << " (" << (time(0)-startTimeGen)/float(i) << " s per candidate)" << endl ;
    if(genTimeDependent){
      // Find the generators either side of the generated decay time.
      GenList& genlist = generators[tag] ;
      GenList::iterator igen = genlist.begin() ;
      while(igen->first < decaytime && igen != genlist.end())
	++igen ;
      SignalGenerator* generator(0) ;
      // Unlikely, but best check (in case we're right at 0 or tmax)
      if(igen->first == decaytime)
	generator = igen->second.get() ;
      // Pick between the generators either side of the decay time according to how close they are to it.
      else{
	GenList::iterator igenprev(igen) ;
	--igenprev ;
	double gensel = ranLux.Rndm() ;
	if(gensel < 1. - (decaytime - igenprev->first)/sampleinterval)
	  generator = igenprev->second.get() ;
	else 
	  generator = igen->second.get() ;
      }
      generator->FillEventList(eventList1, 1);
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
