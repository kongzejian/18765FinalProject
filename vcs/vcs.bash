SYNOPSYS=/afs/ece/support/synopsys
export LM_LICENSE_FILE="$LM_LICENSE_FILE:${SYNOPSYS}/license.dat"
export VCS_HOME=$SYNOPSYS/synopsys.release/vcs-mx_vK-2015.09
export PATH=$VCS_HOME/bin:$PATH
export VCS_ARCH_OVERRIDE=linux
export VCS_MODE_FLAG=64
export MANPATH=$MANPATH:$VCS_HOME/doc/man
export VCS_LIC_EXPIRE_WARNING=0
