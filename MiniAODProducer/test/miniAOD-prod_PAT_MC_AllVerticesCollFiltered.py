# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --filein /store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v2/00000/0033A97B-8707-E511-9D3B-008CFA1980B8.root --conditions MCRUN2_74_V9A -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Input source
process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer17DRPremix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/92X_upgrade2017_realistic_v10_ext1-v2/10000/027E1441-3994-E711-BFBD-02163E01A6D8.root'
                            ),
)

from MiniAODNoMuonTrackProducer.MiniAODProducer.myNoMuonTrackProducer_cfi import *
process.myNoMuonTrackProducerNoMu                 = myNoMuonTrackProducer.clone()
process.myNoMuonTrackProducerNoMu.doRemoveMuons   = cms.untracked.bool(True)
process.myNoMuonTrackProducerNoMu.isData          = cms.untracked.bool(False)

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.offlinePrimaryVerticesNoMu                = offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesNoMu.TrackLabel     = cms.InputTag('myNoMuonTrackProducerNoMu')


from MiniAODNoMuonTrackProducer.MiniAODProducer.myNoMuonTrackProducer_cfi import *
process.myNoMuonTrackProducerWithMu               = myNoMuonTrackProducer.clone()
process.myNoMuonTrackProducerWithMu.doRemoveMuons = cms.untracked.bool(False)
process.myNoMuonTrackProducerWithMu.isData        = cms.untracked.bool(False)

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
process.offlinePrimaryVerticesWithMu              = offlinePrimaryVertices.clone()
process.offlinePrimaryVerticesWithMu.TrackLabel   = cms.InputTag('myNoMuonTrackProducerWithMu')

process.myFilter = cms.EDFilter('myNoLeptonFilter',
                                allTrackTag   = cms.InputTag('myNoMuonTrackProducerWithMu'),
                                noLepTrackTag = cms.InputTag('myNoMuonTrackProducerNoMu')
)

process.selectionNoLeptonFilter = cms.Path( (process.myNoMuonTrackProducerNoMu + process.myNoMuonTrackProducerWithMu) * process.myFilter )
process.vtxRefit = cms.Path( process.offlinePrimaryVerticesNoMu + process.offlinePrimaryVerticesWithMu )

#Output definition
process.MINIAODSIMoutput = cms.OutputModule('PoolOutputModule',
    compressionAlgorithm         = cms.untracked.string('LZMA'),
    compressionLevel             = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands               = process.MINIAODSIMEventContent.outputCommands,
    fileName                     = cms.untracked.string('miniAOD-prod_PAT_MC.root'),
    dropMetaData                 = cms.untracked.string('ALL'),
    fastCloning                  = cms.untracked.bool(False),
    splitLevel                   = cms.untracked.int32(0),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents                 = cms.untracked.PSet( SelectEvents = cms.vstring('selectionNoLeptonFilter') )
)

process.MINIAODSIMoutput.outputCommands.append('keep *_offlinePrimaryVertices*_*_*')
process.MINIAODSIMoutput.outputCommands.append('keep *_myNoMuonTrackProducer*_*_*'),

# Additional output definition
process.myNoMuonTrackProducerWithMu.verbose       = cms.untracked.bool(False)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v10','')

process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
process.offlinePrimaryVertices.verbose = cms.untracked.bool(False)


process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

process.schedule = cms.Schedule(process.selectionNoLeptonFilter,process.vtxRefit,process.MINIAODSIMoutput_step)

process.load('Configuration.StandardSequences.PATMC_cff')
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)
