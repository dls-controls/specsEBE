TOP = ..
include $(TOP)/configure/CONFIG

ifeq ($(EPICS_HOST_ARCH), linux-x86_64)
    DIRS := $(wildcard example)
else
    DIRS = :=
endif

include $(TOP)/configure/RULES_TOP
