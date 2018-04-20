TOP=../..

include $(TOP)/configure/CONFIG

# -------------------------------
# Build an Diamond Support Module
# -------------------------------

LIBRARY_IOC += specsEBE

# xxxRecord.dbd will be installed into <top>/dbd
DBD += specsEBE.dbd

specsEBE_DBD += base.dbd
specsEBE_DBD += asyn.dbd
specsEBE_DBD += stream.dbd

# We need to link against the EPICS Base libraries
specsEBE_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
