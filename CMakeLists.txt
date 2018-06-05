################################################################################
# Package: TemplateAnalysis
################################################################################
gaudi_subdir(TemplateAnalysis v0r1)

gaudi_depends_on_subdirs(
	GaudiConfUtils
	AnalysisUtils)

find_package(PythonLibs)
find_package(Boost COMPONENTS program_options REQUIRED)
find_package(ROOT COMPONENTS Core RIO Hist Graf Graf3d Postscript Gpad
                             RooFit RooFitCore Tree MathCore Foam Physics
                             Proof ProofBench ProofDraw ProofPlayer)

# override the genreflex call to wrap it in the right environment
# set(ROOT_genreflex_CMD ${env_cmd} --xml ${env_xml} ${ROOT_genreflex_CMD})

include_directories(${Boost_INCLUDE_DIRS} ${ROOT_INCLUDE_DIRS})
# gaudi_add_dictionary(TemplateAnalysis
#                      dict/TemplateAnalysisDict.h dict/TemplateAnalysisDict.xml
#                      SPLIT_CLASSDEF)

# gaudi_add_library(TemplateAnalysisLib
#                   src/*.cpp
#                   TemplateAnalysisDict_classdef.cpp
#                   PUBLIC_HEADERS TemplateAnalysis
#                   INCLUDE_DIRS Boost ROOT
#                   LINK_LIBRARIES Boost ROOT)

# # ensure that genreflex is not called twice (in parallel builds)
# add_dependencies(TemplateAnalysisLib TemplateAnalysisGen)

gaudi_install_python_modules()

#gaudi_add_test(QMTest QMTEST)
