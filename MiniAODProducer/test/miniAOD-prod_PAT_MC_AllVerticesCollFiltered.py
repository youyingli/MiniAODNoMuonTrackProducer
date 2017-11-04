# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --filein /store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/00000/0033A97B-8707-E511-9D3B-008CFA1980B8.root --conditions MCRUN2_74_V9A -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc' , '')
process.load('PhysicsTools.PatAlgos.patSequences_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(  '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/00773447-C000-E611-B4E6-0CC47A4D761A.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/041D3A34-1000-E611-A66E-0CC47A4C8E16.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04415584-72FF-E511-A64A-90B11C050429.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/045FC740-A700-E611-8F91-A0000420FE80.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/06048F67-C600-E611-ADBE-0025905B85AA.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/063E1945-A700-E611-BD39-0025905B85D0.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/081E79F8-BDFE-E511-B483-14187741136B.root',
       '/store/mc/RunIISpring16DR80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A14F9F9-93FF-E511-A080-0CC47A4D7616.root'
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



from Validation.RecoVertex.myNoMuonTrackProducer_cfi import *
process.myNoMuonTrackProducerNoMu=myNoMuonTrackProducer.clone()
process.myNoMuonTrackProducerNoMu.doRemoveMuons=cms.untracked.bool(True)
process.myNoMuonTrackProducerNoMu.verbose=cms.untracked.bool(True)
process.myNoMuonTrackProducerNoMu.isData=cms.untracked.bool(False)

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.offlinePrimaryVerticesNoMu=offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesNoMu.TrackLabel = cms.InputTag("myNoMuonTrackProducerNoMu")


from Validation.RecoVertex.myNoMuonTrackProducer_cfi import *
process.myNoMuonTrackProducerWithMu=myNoMuonTrackProducer.clone()
process.myNoMuonTrackProducerWithMu.doRemoveMuons=cms.untracked.bool(False)
process.myNoMuonTrackProducerWithMu.verbose=cms.untracked.bool(False)
process.myNoMuonTrackProducerWithMu.isData=cms.untracked.bool(False)

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.offlinePrimaryVerticesWithMu=offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesWithMu.TrackLabel = cms.InputTag("myNoMuonTrackProducerWithMu")

from PhysicsTools.PatAlgos.selectionLayer1.countPatCandidates_cff import *
from PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *
 
process.myFilter = cms.EDFilter(
    "myNoLeptonFilter",
    allTrackTag=cms.InputTag('myNoMuonTrackProducerWithMu'),
    noLepTrackTag=cms.InputTag('myNoMuonTrackProducerNoMu')
    )


#Output definition
process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False), 
    fileName = cms.untracked.string('miniAOD-prod_PAT_MC25ns_AllVerticesCollFiltered.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('selectionNoLeptonFilter')
    )
)

process.MINIAODSIMoutput.outputCommands.append('keep *_offlinePrimaryVertices*_*_*')
process.MINIAODSIMoutput.outputCommands.append('keep *_myNoMuonTrackProducer*_*_*'),

process.selectionNoLeptonFilter = cms.Path((process.myNoMuonTrackProducerNoMu+process.myNoMuonTrackProducerWithMu)*process.myFilter)
process.vtxRefit=cms.Path(process.offlinePrimaryVerticesNoMu+process.offlinePrimaryVerticesWithMu)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9A', '') #50ns
#process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '') # 25ns
#process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_v12','')
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_v3','')                              
process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
process.offlinePrimaryVertices.verbose = cms.untracked.bool(False)


process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput) 

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)
