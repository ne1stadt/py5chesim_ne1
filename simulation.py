"""This is the simulation script.
Simulation, cell and traffic profile parameters can be set here.
"""
import json
import os
import sys

import simpy

from Cell import *
from Results import *
from UE import *

# ------------------------------------------------------------------------------------------------------
#              Cell & Simulation parameters
# ------------------------------------------------------------------------------------------------------

with open('data.json') as file:
    data = json.load(file)

print(data)

bw = data["bandwidths"]

fr = data["frequency-range"]  # FR1 or FR2
"""String with frequency range (FR) to use. 'FR1' for FR1, or 'FR2' for FR2."""
band = data["band"]
"""String with used band for simulation. In TDD mode it is important to set correctly a band from the next list: n257, n258, n260, n261."""
tdd = data["is-tdd"]
"""Boolean indicating if the cell operates in TDD mode."""
buf = data["buffer-size"]  # 10240 #
"""Integer with the maximum Bytes the UE Bearer buffer can tolerate before dropping packets."""
schedulerInter = data["inter-scheduler"]  # RRp for improved Round Robin, PFXX for Proportional Fair
"""String indicating the Inter Slice Scheduler to use. For only one Slice simulations use ''.
If the simulation includes more than one slice, set '' for Round Robin, 'RRp' for Round Robin Plus,
or 'PFXY' for Proportional Fair with X=numExp and Y=denExp."""
#                   Simulation parameters
t_sim = data["simulation-time"] # (ms)
"""Simulation duration in milliseconds."""
debMode = data["debugging-mode"]  # to show queues information by TTI during simulation
"""Boolean indicating if debugging mode is active. In that case, an html log file will be generated with schedulers operation.
Note that in simulations with a high number of UEs this file can turn quite heavy."""
measInterv = data["measure-interval"]  # interval between meassures default 1000
"""Time interval (in milliseconds) between meassures for statistics reports."""
interSliceSchGr = data["inter-scheduling-granularity"]  # 3000.0 # interSlice scheduler time granularity
"""Inter slice scheduler time granularity in milliseconds."""

# -----------------------------------------------------------------
#              Simulation process activation
# -----------------------------------------------------------------

env = simpy.Environment()
"""Environment instance needed by simpy for runing PEM methods"""
cell1 = Cell(data["cell-id"], bw, fr, debMode, buf, tdd, interSliceSchGr, schedulerInter)

"""Cell instance for running the simulation"""
interSliceSche1 = cell1.interSliceSched
"""interSliceScheduler instance"""

UEgroups = []
for data_slice in data["slices"]:
    UEgroups.append(
        UEgroup(
            data_slice["downlink-num-users"],
            data_slice["uplink-num-users"],
            data_slice["downlink-packet-size"],
            data_slice["uplink-packet-size"],
            data_slice["downlink-arrival-rate"],
            data_slice["uplink-arrival-rate"],
            data_slice["time-start"],
            data_slice["time-end"],
            data_slice["downlink-distribution"],
            data_slice["uplink-distribution"],
            data_slice["label"],
            data_slice["delay-requirements"],
            data_slice["accessibility-requirements"],
            data_slice["intra-scheduler"],
            data_slice["mimo-mode"],
            data_slice["layers-for-mimo"],
            cell1,
            t_sim,
            measInterv,
            env,
            data_slice["sinr"]
        )
    )

"""Group of users with defined traffic profile, capabilities and service requirements for which the sumulation will run.

More than one can be instantiated in one simulation.
For each one of them, the UEgroup instance must be added in the UEgroups list.

UEgroupN = UEgroup(nuDL,nuUL,pszDL,pszUL,parrDL,parrUL, tstart, tend, distP, distA,
label,dly,avlty,schedulerType,mimo_mode,layers,cell,hdr,t_sim,measInterv,env,sinr):

label: must contain substring according to the type of service: eMBB, mMTC, URLLC\n
schedulerType: RR: Rounf Robin, PF: Proportional Fair (10, 11)\n
mimo_mode: SU, MU\n
layers: in SU-MIMO is the number of layers/UE, in MU-MIMO is the number of simultaneous UE to serve with the same resources\n
sinr: is a string starting starting with S if all ues have the same sinr or D if not. The value next will be the initial sinr of each ue or the maximum."""

"""UE group list for the configured simulation"""
#           Slices creation
for ueG in UEgroups:
    interSliceSche1.createSlice(
        ueG.req["reqDelay"],
        ueG.req["reqThroughputDL"],
        ueG.req["reqThroughputUL"],
        ueG.req["reqAvailability"],
        ueG.num_usersDL,
        ueG.num_usersUL,
        band,
        debMode,
        ueG.mmMd,
        ueG.lyrs,
        ueG.label,
        ueG.sch,
    )

#      Schedulers activation (inter/intra)

procCell = env.process(cell1.updateStsts(env, interv=measInterv, tSim=t_sim))
procInter = env.process(interSliceSche1.resAlloc(env))
for ueG in UEgroups:
    ueG.activateSliceScheds(interSliceSche1, env)

# ----------------------------------------------------------------
env.run(until=t_sim)
# ----------------------------------------------------------------

#      Closing statistic and debugging files

for slice in list(cell1.slicesStsts.keys()):
    cell1.slicesStsts[slice]["DL"].close()
    cell1.slicesStsts[slice]["UL"].close()
for slice in list(interSliceSche1.slices.keys()):
    interSliceSche1.slices[slice].schedulerDL.dbFile.close()
    if slice != "LTE":
        interSliceSche1.slices[slice].schedulerUL.dbFile.close()

# ----------------------------------------------------------------
#                          RESULTS
# ----------------------------------------------------------------
# Show average PLR and Throughput in any case simulation and plots
for UEg in UEgroups:
    print(
        Format.CBOLD
        + Format.CBLUE
        + "\n--------------------------------------------------"
        + Format.CEND
    )
    print(
        Format.CBOLD
        + Format.CBLUE
        + "                 SLICE: "
        + UEg.label
        + "                  "
        + Format.CEND
    )
    print(
        Format.CBOLD
        + Format.CBLUE
        + "--------------------------------------------------\n"
        + Format.CEND
    )
    UEg.printSliceResults(interSliceSche1, t_sim, bw, measInterv)
print(
    Format.CBOLD
    + Format.CBLUE
    + "\n--------------------------------------------------"
    + Format.CEND
)
