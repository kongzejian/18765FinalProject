if ( $?LM_LICENSE_FILE ) then
	setenv LM_LICENSE_FILE /afs/ece.cmu.edu/support/mgc/license.dat:$LM_LICENSE_FILE
else
	setenv LM_LICENSE_FILE /afs/ece.cmu.edu/support/mgc/license.dat
endif

setenv MGLS_LICENSE_FILE ${LM_LICENSE_FILE}
setenv SALT_LICENSE_SERVER="29000@siemens-lic.ece.local.cmu.edu;1717@siemens-lic.ece.local.cmu.edu"
set TESSENT="/afs/ece.cmu.edu/support/mgc/mgc.release/tessent_2023_3"
set AUSTEMPER="/afs/ece.cmu.edu/support/mgc/mgc.release/austemper_2023_tmp"
set FLEXTEST="/afs/ece.cmu.edu/support/mgc/mgc.release/tessent_2022_1"
setenv PATH "${PATH}:${TESSENT}/bin:${AUSTEMPER}/linux_x86_64/bin:${FLEXTEST}/bin"
