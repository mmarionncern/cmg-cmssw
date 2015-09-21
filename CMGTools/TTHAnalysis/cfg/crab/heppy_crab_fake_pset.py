import FWCore.ParameterSet.Config as cms
process = cms.Process('FAKE')
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
#process.output = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('tree.root'))
#process.output = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('output.log.tgz.root'))
#process.out = cms.EndPath(process.output)
