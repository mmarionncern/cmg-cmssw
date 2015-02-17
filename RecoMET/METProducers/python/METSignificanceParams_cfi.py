import FWCore.ParameterSet.Config as cms

METSignificanceParams = cms.PSet(

      # jet resolutions
      ptResFile    = cms.string('Spring10_PtResolution_AK5PF.txt'),
      phiResFile   = cms.string('Spring10_PhiResolution_AK5PF.txt'),
      jetThreshold = cms.double(20),
      
      #jet-lepton matching dR
      dRMatch = cms.double(0.4),

      # eta bins for jet resolution tuning
      jeta = cms.vdouble(0.5, 1.1, 1.7, 2.3),

      # tuning parameters
      jpar = cms.vdouble(1.15061, 1.07776, 1.04204, 1.12509, 1.56414),
      pjpar = cms.vdouble(0.0, 0.548758)

      )
