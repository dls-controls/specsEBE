TOP = ../..
ifdef EPICS_HOST_ARCH
include $(TOP)/configure/CONFIG

# Copy all protocol files into data directory
DATA += $(patsubst ../%, %, $(wildcard ../*.proto))

include $(TOP)/configure/RULES
endif
