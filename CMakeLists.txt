cmake_minimum_required(VERSION 3.5)
project(specsEBE)

set(SUPPORT "/dls_sw/prod/R3.14.12.3/support")
set(EPICS_BASE "/dls_sw/epics/R3.14.12.3/base")
set(ASYN "${SUPPORT}/asyn/4-31")
set(TEMPLATE_TOP "${EPICS_BASE}/templates/makeBaseApp/top")
set(STREAM "${SUPPORT}/streamDevice/2-5dls5")

include_directories(
    ${ASYN}/include
    ${TEMPLATE_TOP}/include
    ${STREAM}/include
    ${SUPPORT}/include
    ${EPICS_BASE}/include
    ${EPICS_BASE}/include/os/Linux)

set(SPECSEBE_SOURCE_FILES
        ebeApp/src/ebeMain.cpp
)

add_library(specsEBE_source ${SPECSEBE_SOURCE_FILES})
add_custom_target(specsEBE_build
    COMMAND $(MAKE) -C /scratch/work/R3.14.12.3/support/specsEBE
    SOURCES ${SPECSEBE_SOURCE_FILES})
