from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'heppy_crab_fake_pset.py'
config.JobType.scriptExe = 'heppy_crab_script.sh'
# config.JobType.sendPythonFolder = True  #doesn't work, not supported yet? do it by hand
import os
os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python")
os.system("tar czf cmgdataset.tar.gz --directory $HOME .cmgdataset")
os.system("tar czf cafpython.tar.gz --directory /afs/cern.ch/cms/caf/ python")
config.JobType.inputFiles = ['FrameworkJobReport.xml','heppy_config.py','heppy_crab_script.py','cmgdataset.tar.gz', 'python.tar.gz', 'cafpython.tar.gz']
if "JSON" in os.environ:
    config.JobType.inputFiles.append( os.environ["JSON"] )

output_files=os.environ["OUTPUTFILES"].split(" ")[:-1]
config.JobType.outputFiles = output_files
#[ 'output.log.tgz'] 
# tree.root is automatically send because of the pset file 'SkimReport.pck',
config.JobType.disableAutomaticOutputCollection = True

config.section_("Data")
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.Data.outLFNDirBase = '/store/user/' + os.environ["USER"]
config.Data.publication = False
config.Data.unitsPerJob = 10

config.section_("Site")
#config.Site.whitelist = ["T2_CH_CSCS"]
config.Site.whitelist = ["T2_CH_CSCS", "T2_IT_Legnaro", "T2_UK_London_IC", "T2_UK_SGrid_Bristol", "T2_DE_DESY", "T2_ES_CIEMAT", "T2_IT_Rome", "T2_AT_Vienna","T2_DE_RWTH","T2_FR_GRIF_IRFU", "T2_HU_Budapest", "T2_FR_IPHC", "T2_BE_IIHE", "T2_IT_Pisa", "T2_ES_IFCA", "T2_UK_London_Brunel", "T2_US_Purdue", "T2_UA_KIPT", "T2_US_MIT", "T2_US_Wisconsin", "T2_US_UCSD", "T2_US_Vanderbilt", "T2_US_Caltech"]
config.Site.storageSite = "T2_CH_CERN"
#config.Data.ignoreLocality = True

