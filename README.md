# MiniAODNoMuonTrackProducer
## MiniAODProducer

  - Code to reproduce the vertex collection without the muons tracks in Z events
  - For Higgs to 2 photons vertex validation
  - this versions works on 2017 Data in CMSSW_9_2_X but can probably work in other releases


### Install the code
```
cmsrel CMSSW_9_2_13
cd CMSSW_9_2_8/src
cmsenv
git cms-init
git clone https://github.com/youyingli/MiniAODNoMuonTrackProducer
scram b -j 3
```
### Test code
```
cmsRun MiniAODNoMuonTrackProducer/MiniAODProducer/python/miniAOD-prod_PAT_DATA_AllVerticesCollFiltered.py
```
### Crab job 
After building your crab config file, please test your crab job by
```
source /cvmfs/cms.cern.ch/crab3/crab.sh
crab submit -c <crab config file> --dryrun
```
If not failed, it will show
```javascript=
Data.unitsPerJob = 79
```
which tells you a correct number should be set in your crab config file. Then, modify your config file and do
```
crab submit -c <crab config file>
```
