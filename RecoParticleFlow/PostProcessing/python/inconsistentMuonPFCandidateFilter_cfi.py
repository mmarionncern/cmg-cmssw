import FWCore.ParameterSet.Config as cms

inconsistentMuonPFCandidateFilter = cms.EDFilter(
    "InconsistentMuonPFCandidateFilterPF",
    PFCandidates  = cms.InputTag("particleFlow"),   # Collection to test
    ptMin         = cms.double(100.),               # Muons with pT below this are ignored (will not be checked)
    maxPTDiff     = cms.double(0.1),                # Muons with |pT(tracker)/pT(global) - 1| > maxPTDiff are flagged as "inconsistent"
    verbose       = cms.untracked.bool(False),
    taggingMode = cms.bool( False )
 )
