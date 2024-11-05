SYNOPSYS=/afs/ece/support/synopsys
if ( $?LM_LICENSE_FILE ) then
    setenv LM_LICENSE_FILE "$LM_LICENSE_FILE:${SYNOPSYS}/license.dat"
else
    setenv LM_LICENSE_FILE "${SYNOPSYS}/license.dat"
endif

setenv VCS_HOME "$SYNOPSYS/synopsys.release/vcs-mx_vK-2015.09"
setenv PATH "$VCS_HOME/bin:$PATH"
setenv VCS_ARCH_OVERRIDE "linux"
setenv VCS_MODE_FLAG 64
setenv MANPATH "$MANPATH:$VCS_HOME/doc/man"
setenv VCS_LIC_EXPIRE_WARNING 0
