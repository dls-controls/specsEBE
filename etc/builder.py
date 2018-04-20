from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol


class EBE4(AutoSubstitution, AutoProtocol):

    # Parse this template file for macros
    # This is a *.db rather than a *.template because the src build generates ebe4.db from the
    # ebe4.substitutions file that has a lot of macros that will never change
    TemplateFile = "ebe4.db"

    # This is the streamDevice protocol file to use
    ProtocolFiles = ["ebe4.proto"]
