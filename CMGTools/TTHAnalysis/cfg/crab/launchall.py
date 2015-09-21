import imp, os

# datasets to run as defined from run_susyMT2.cfg
# number of jobs to run per dataset decided based on splitFactor and fineSplitFactor from cfg file
# in principle one only needs to modify the following two lines:
#production_label = "prod747data_Run2015B_golden_residual_all"
production_label = "testprod"
cmg_version = 'CMGTools-from-CMSSW_7_4_7'
config_file = '../run_susyMultilepton_cfg.py'
json_file="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-255031_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt"
output_files = ["output.log.tgz"]

useJSON= True

debug  = False
useAAA = False

#external commands for renaming
external_commands={}
#external_commands["Output/tree.root"]="tree.root"

#Global heppy options
global_heppy_options={}
global_heppy_options[ "test" ]='1'
global_heppy_options[ "nofetch" ]=True


#soft link locally the configuration file
os.system("ln -sf "+config_file+" heppy_config.py")

if useJSON: # if json file if needed, MM could be done in a better way
    os.system("cp "+json_file+" .")
    global_heppy_options[ "json" ]=json_file.split("/")[-1]

#needed in case people are changing the components in options
import PhysicsTools.HeppyCore.framework.heppy_loop as heppy
globOptStr=""
for opt in global_heppy_options:
    heppy._heppyGlobalOptions[ opt ] = global_heppy_options[ opt ]
    globOptStr += "-glob--"+opt+"="+str( global_heppy_options[ opt ] )+" "
    
#
extCmdStr=""
for ext in external_commands:
    extCmdStr += "-ext--"+ext+"="+external_commands(ext)

handle = open("heppy_config.py", 'r')
cfo = imp.load_source("heppy_config", "heppy_config.py", handle)
conf = cfo.config
handle.close()

os.system("scramv1 runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

os.environ["PROD_LABEL"]  = production_label
os.environ["CMG_VERSION"] = cmg_version
os.environ["DEBUG"]       = str(debug)
os.environ["USEAAA"]      = str(useAAA)
os.environ["GLOBAL"]      = globOptStr
os.environ["EXTERNAL"]    = extCmdStr
if useJSON:
    os.environ["JSON"]        = json_file.split("/")[-1]
os.environ["OUTPUTFILES"] = ""
for f in output_files:
    os.environ["OUTPUTFILES"] += f+" "

from PhysicsTools.HeppyCore.framework.heppy_loop import split
for comp in conf.components:
    # get splitting from config file according to splitFactor and fineSplitFactor (priority given to the latter)
    NJOBS = len(split([comp]))
    os.environ["NJOBS"] = str(NJOBS)
    os.environ["DATASET"] = str(comp.name)
    os.system("crab submit -c heppy_crab_config_env.py")

os.system("rm -f python.tar.gz")
os.system("rm -f cmgdataset.tar.gz")
os.system("rm -f cafpython.tar.gz")
