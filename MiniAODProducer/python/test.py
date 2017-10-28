# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: miniAOD-prod -s PAT --eventcontent MINIAOD --runUnscheduled --data --filein /store/data/Run2015B/DoubleMuon/AOD/PromptReco-v1/000/251/162/00000/F6A6BB6F-4227-E511-BAAF-02163E014343.root --conditions 74X_dataRun2_Prompt_v1 -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data' , '')

process.GlobalTag = GlobalTag(process.GlobalTag,'92X_dataRun2_Prompt_v4','')

process.load('PhysicsTools.PatAlgos.patSequences_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
       fileNames = cms.untracked.vstring(  
        'root://cms-xrd-global.cern.ch//store/data/Run2017A/DoubleMuon/AOD/PromptReco-v2/000/296/172/00000/4AAD2027-544C-E711-802C-02163E01A515.root'
#/store/data/Run2017D/DoubleMuon/AOD/PromptReco-v1/000/302/031/00000/02367FB0-4C8F-E711-A7D0-02163E0135EB.root'
),

    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('miniAOD-prod nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

#from Validation.RecoVertex.myNoMuonTrackProducer_cfi import *
#process.myNoMuonTrackProducerNoMu=myNoMuonTrackProducer.clone()
#process.myNoMuonTrackProducerNoMu.doRemoveMuons=cms.untracked.bool(True)
#process.myNoMuonTrackProducerNoMu.verbose=cms.untracked.bool(True)
#process.myNoMuonTrackProducerNoMu.isData=cms.untracked.bool(True)

#from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
#process.offlinePrimaryVerticesNoMu=offlinePrimaryVertices.clone()
#process.offlinePrimaryVerticesNoMu.TrackLabel = cms.InputTag("myNoMuonTrackProducerNoMu")


#from Validation.RecoVertex.myNoMuonTrackProducer_cfi import *
#process.myNoMuonTrackProducerWithMu=myNoMuonTrackProducer.clone()
#process.myNoMuonTrackProducerWithMu.doRemoveMuons=cms.untracked.bool(False)
#process.myNoMuonTrackProducerWithMu.verbose=cms.untracked.bool(False)
#process.myNoMuonTrackProducerWithMu.isData=cms.untracked.bool(True)

#from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
#process.offlinePrimaryVerticesWithMu=offlinePrimaryVertices.clone()
#process.offlinePrimaryVerticesWithMu.TrackLabel = cms.InputTag("myNoMuonTrackProducerWithMu")

from PhysicsTools.PatAlgos.selectionLayer1.countPatCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
 


#process.myFilter = cms.EDFilter(
#    "myNoLeptonFilter",
#    allTrackTag=cms.InputTag('myNoMuonTrackProducerWithMu'),
#    noLepTrackTag=cms.InputTag('myNoMuonTrackProducerNoMu')
#    )

#process.selectionNoLeptonFilter = cms.Path((process.myNoMuonTrackProducerNoMu+process.myNoMuonTrackProducerWithMu)*process.myFilter)
#process.vtxRefit=cms.Path(process.offlinePrimaryVerticesNoMu+process.offlinePrimaryVerticesWithMu)
    

# Output definition

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('miniAOD-prod_PAT_DATA25ns_AllVerticesCollFiltered_test.root'),
    outputCommands = process.MINIAODEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
#    SelectEvents = cms.untracked.PSet(
#        SelectEvents = cms.vstring('selectionNoLeptonFilter')
#    )
)

process.MINIAODoutput.outputCommands.append('keep *_offlinePrimaryVertices*_*_*')
#process.MINIAODoutput.outputCommands.append('keep *_myNoMuonTrackProducer*_*_*'),
process.MINIAODoutput.outputCommands.append('keep patPackedCandidates_packedPFCandidates_*_*'),

# Additional output definition

# Other statements
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v4', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '76X_dataRun2_v15', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v8', '')
#process.GlobalTag.globaltag = 'auto:run2'
# Path and EndPath definitions

                                     
process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
process.offlinePrimaryVertices.verbose = cms.untracked.bool(False)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput) 


# Schedule definition
#process.schedule = cms.Schedule(process.endjob_step,process.MINIAODoutput_step) # JM: try comment this
# THIS WAS COMMENTED FOR THE FILTER TO WORK...

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PAT_cff')
#from FWCore.ParameterSet.Utilities import cleanUnscheduled
#process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions
