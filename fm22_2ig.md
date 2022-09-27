---
title: |
    VA FileMan 22.2

    Installation, Back-Out, and Rollback Guide
---

![Department of Veterans Affairs official
seal](images/media/image1.jpg){width="2.375in" height="2.375in"}

August 2016

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

![Note](images/media/image2.png "Note"){width="0.3333333333333333in"
height="0.3333333333333333in"} **NOTE**: The revision history cycle
begins once changes or enhancements are requested after the
Installation, Back-Out, and Rollback Guide has been baselined.

+-----------------+-----------------+-----------------+-----------------+
| Date            | Version         | Description     | Author          |
+-----------------+-----------------+-----------------+-----------------+
| 08/03/2016      | 1.0             | Initial release | VA FileMan 22.2 |
|                 |                 | of VA FileMan   | Development     |
|                 |                 | 22.2            | Team            |
|                 |                 | Installation,   |                 |
|                 |                 | Back-Out, and   |                 |
|                 |                 | Rollback Guide. |                 |
|                 |                 |                 |                 |
|                 |                 | Based on the    |                 |
|                 |                 | ProPath         |                 |
|                 |                 | Installation,   |                 |
|                 |                 | Back-Out, and   |                 |
|                 |                 | Rollback Guide  |                 |
|                 |                 | template;       |                 |
|                 |                 | released        |                 |
|                 |                 | February 2016;  |                 |
|                 |                 | Version 2.1.    |                 |
+-----------------+-----------------+-----------------+-----------------+

Table of Contents

[1 Introduction 1](#introduction)

[1.1 MUMPS OPERATING SYSTEM File Considerations
1](#mumps-operating-system-file-considerations)

[2 Pre-installation and System Requirements
3](#pre-installation-and-system-requirements)

[2.1 Back Up System 3](#back-up-system)

[2.2 Platform Installation and Preparation
3](#platform-installation-and-preparation)

[2.3 Download and Extract Files 3](#download-and-extract-files)

[2.3.1 Software 3](#software)

[2.3.2 Documentation 3](#documentation)

[2.4 Installation Scripts 4](#installation-scripts)

[2.5 Cron Scripts 4](#cron-scripts)

[2.6 Access Requirements and Skills Needed for the Installation
4](#access-requirements-and-skills-needed-for-the-installation)

[3 Installation Procedure 5](#_Toc458001716)

[3.1 Log onto the System 5](#log-onto-the-system)

[3.2 Check the Current VA FileMan Version
5](#check-the-current-va-fileman-version)

[3.3 Production Environment: Shut Down System
5](#production-environment-shut-down-system)

[3.4 Production Environment: Restart System
5](#production-environment-restart-system)

[3.5 Production Environment: Inhibit Logons for Each Volume Set
5](#production-environment-inhibit-logons-for-each-volume-set)

[3.6 Environment Check 6](#environment-check)

[3.7 Production Environment: Load the VA FileMan 22.2 Distribution
6](#production-environment-load-the-va-fileman-22.2-distribution)

[3.8 Install the VA FileMan 22.2 Package
8](#install-the-va-fileman-22.2-package)

[3.9 Post-Install TaskMan Procedures
11](#post-install-taskman-procedures)

[3.10 Production Environment: Enable Logons
11](#production-environment-enable-logons)

[4 Implementation Procedure 12](#_Toc458001727)

[4.1 Database Tuning 12](#database-tuning)

[4.2 Verify Installation 12](#verify-installation)

[5 Back-Out Plan 12](#back-out-plan)

[5.1 Back-Out Strategy 12](#back-out-strategy)

[5.2 Back-Out Considerations 12](#back-out-considerations)

[5.2.1 Load Testing 12](#load-testing)

[5.2.2 User Acceptance Testing 12](#user-acceptance-testing)

[5.3 Back-Out Criteria 12](#back-out-criteria)

[5.4 Back-Out Risks 12](#back-out-risks)

[5.5 Authority for Back-Out 13](#authority-for-back-out)

[5.6 Back-Out Procedure 13](#back-out-procedure)

[6 Rollback Plan 13](#rollback-plan)

[6.1 Rollback Considerations 13](#rollback-considerations)

[6.2 Rollback Criteria 13](#rollback-criteria)

[6.3 Rollback Risks 13](#rollback-risks)

[6.4 Authority for Rollback 13](#authority-for-rollback)

[6.5 Rollback Procedure 13](#rollback-procedure)

List of Figures

[Figure 1: Check the Current VA FileMan Version 5](#_Toc458001745)

[Figure 2: Inhibit Logons for Each Volume Set 6](#_Toc458001746)

[Figure 3: load the VA FileMan 22.2 distribution file 7](#_Toc458001747)

[Figure 4: Sample installation dialogue 8](#_Toc458001748)

[Figure 5: Enable Logons 11](#_Toc458001749)

List of Tables

[Table 1: VA FileMan 22.2 Documentation 3](#_Toc457395538)

Introduction
============

This guide provides instructions for installing Department of Veterans
Affairs (VA) FileMan 22.2. VA FileMan is designed to be used either with
the Kernel or as a standalone application; however, these installation
instructions are provided only for sites running Kernel 8.0. Since
Kernel is dependent on VA FileMan 22.0, that version of VA FileMan is
already installed on your system.

This guide is written specifically for the Caché Operating System (OS).
It does not contain OS-specific instructions for other OSs, such as
routing mapping and manually moving %routines into the Manager account.

![Note](images/media/image2.png "Note"){width="0.3333333333333333in"
height="0.3333333333333333in"} **REF:** For identifying other OSs to VA
FileMan and Kernel, see Section [1.1]{.underline}.

This installation is significantly different from previous versions. You
no longer must manually move the new VA FileMan routines into the
account. The routines are present in the Kernel Installation &
Distribution System (KIDS) build and are loaded as part of the install.
DINIT is run *non*-interactively during the KIDS pre-install to update
the VA FileMan files.

After this installation, the current version of the VA FileMan files
will be installed and updated with data as appropriate.

![Caution](images/media/image3.png "Caution"){width="0.4479166666666667in"
height="0.4479166666666667in"} CAUTION: Do *not* run DINIT to update the
VA FileMan files after the install is complete. Running DINIT from the
Command line at any time will cause data corruption.

MUMPS OPERATING SYSTEM File Considerations
------------------------------------------

This Install, Back-Out, and Rollback Guide assumes an install on Caché.
You are not asked to identify your OS during the install.

VA FileMan 22.2 populates the MUMPS OPERATING SYSTEM file (\#.7) with
values for the following operating systems:

-   CACHE/OpenM

-   DSM for OpenVMS

-   DTM-PC

-   GT.M(UNIX)

-   GT.M(VAX)

-   MSM

-   OTHER---This placeholder is for a user defined OS

In order to notify VA FileMan that you are using an OS other than Cache
after the install completes enter the following command to identify your
OS:

\>**D OS\^DINIT**

In order to complete the identification to Kernel that you are running
an OS other than Cache, run the appropriate routine from the following
list:

ZOSFGTM            GTM on VMS

ZOSFGUX            GTM on Unix

ZOSFONT            Cache

ZOSFVXD            DSM on VMS

Pre-installation and System Requirements
========================================

Back Up System
--------------

Back up your system as a safeguard *before* the installation. In order
to back out the VA FileMan 22.2 installation, restore your back up (see
the "[Back-Out Plan]{.underline}" section).

Platform Installation and Preparation
-------------------------------------

VA FileMan 22.2 requires pre-existing Kernel 8.0 software.

Patches DI\*22.2\*1 *and* HL7\*1.6\*167 resolve a known VA FileMan (FM)
22.2 issue, SDM I9259370. User cannot select HL7 messages directly from
the list in the HL View Transmission Log option. For ease of
installation, sites may delay installing FM 22.2 until release of
patches DI\*22.2\*1 and HL7\*1.6\*167; both patches will be released
shortly. Although the two patches can be installed while users are on
the system, installing both patches right after installing FM 22.2,
before allowing users back on the system, is more efficient and will
eliminate any possible errors.

Download and Extract Files
--------------------------

Software being released as a Kernel Installation and Distribution System
(KIDS) file and documentation describing the new functionality
introduced by this patch is available.

### Software

Software can be downloaded from the **Product** Support (PS) Anonymous
Directories via Secure File Transfer Protocol (SFTP).

Download the VA\_FILEMAN\_22\_2.KID file from the appropriate server to
a directory on your system.

### Documentation

Documentation can be downloaded from the **Product** Support (PS)
Anonymous Directories via Secure File Transfer Protocol (SFTP).

Documentation can also be found on the VA Software Document Library
(VDL) at: <http://www.va.gov/vdl/application.asp?appid=5>

[]{#_Toc457395538 .anchor}Table 1: VA FileMan 22.2 Documentation

  File Name        FTP Mode   Description
  ---------------- ---------- ------------------------------------------------------------
  fm22\_2um1.pdf   Binary     VA FileMan 22.2 User Manual
  fm22\_2um2.pdf   Binary     VA FileMan 22.2 Advanced User Manual
  fm22\_2dg.pdf    Binary     VA FileMan 22.2 Developer's Guide
  fm22\_2ig.pdf    Binary     VA FileMan 22.2 Installation, Back-Out, and Rollback Guide
  fm22\_2tm.pdf    Binary     VA FileMan 22.2 Technical Manual
  fm22\_2rn.pdf    Binary     VA FileMan 22.2 Release Notes

  : VSM Documentation

Installation Scripts
--------------------

There are no installation scripts for VA FileMan 22.2.

Cron Scripts
------------

There are no cron scripts for the VA FileMan 22.2.

Access Requirements and Skills Needed for the Installation
----------------------------------------------------------

Only those with system management knowledge and access should install VA
FileMan 22.2.

![Note](images/media/image2.png "Note"){width="0.3333333333333333in"
height="0.3333333333333333in"} **REF:** For instructions on performing
OS-level tasks, see your OS system management documentation.

The installer needs to know how to do the following:

-   Obtain Veterans Health Information Systems and Technology
    Architecture (VistA) software from FORUM and Secure File Transfer
    Protocol (SFTP) download sites (i.e., Product Support Anonymous
    Directories).

-   Run a Kernel Installation and Distribution System (KIDS)
    installation.

-   Logging onto the system and getting to the M prompt (Programmer
    Mode).

-   Execute commands in Programmer mode when given VistA Programmer
    Access.

-   Running system status reports.

-   Terminating processes.

-   Accessing host files (i.e., KIDS build file).

-   Inhibiting Logons.

-   Stopping TaskMan.

Installation Procedure
======================

Log onto the System
-------------------

Log onto the Production account.

Check the Current VA FileMan Version
------------------------------------

Check that current version in the PACKAGE FILE (\#9.4) is set to
**22.0**.

[]{#_Toc458001745 .anchor}Figure 1: Check the Current VA FileMan Version

\>**D P\^DI**

VA FileMan 22.2

Select OPTION: **1 \<Enter\>** ENTER OR EDIT FILE ENTRIES

Input to what File: DEVICE// **PACKAGE**

1 PACKAGE (294 entries)

2 PACKAGE INTERFACE (128 entries)

3 PACKAGE SIZE (5182 entries)

4 PACKAGE TYPE (529 entries)

CHOOSE 1-4: **1 \<Enter\>** PACKAGE (294 entries)

EDIT WHICH FIELD: ALL// **CURRENT VERSION**

THEN EDIT FIELD: **\<Enter\>**

Select PACKAGE NAME: **VA FILEMAN \<Enter\>** DI

CURRENT VERSION: 22.2// **22.0**

Select PACKAGE NAME:

Production Environment: Shut Down System
----------------------------------------

In Production, shut down Caché/system using your regular shutdown
procedures.

Production Environment: Restart System
--------------------------------------

In Production, restart Caché/system using your regular startup
procedures.

-   Do not restart TaskMan or any background filers.

-   Do not allow any users back on the system.

Production Environment: Inhibit Logons for Each Volume Set
----------------------------------------------------------

You can use the operating system (OS) command to prevent logons. Using
the OS command does not cause a problem and allows you to work within
the menu system as needed during the installation. Caché/OpenM sites can
stop the LAT and TELNET services.

Use VA FileMan to edit the VOLUME SET file (\#14.5).

[]{#_Toc458001746 .anchor}Figure 2: Inhibit Logons for Each Volume Set

\>**D Q\^DI**

VA FileMan 22.0

Select OPTION: **ENTER OR EDIT FILE ENTRIES**

INPUT TO WHAT FILE: VOLUME SET// **14.5**

EDIT WHICH FIELD: ALL// **INHIBIT LOGONS ?**

THEN EDIT FIELD: **\<Enter\>**

Select VOLUME SET: ***\<Production Account\>***

INHIBIT LOGONS?: NO// **YES**

Environment Check
-----------------

The VA FileMan 22.2 distribution includes an Environment Check routine
(DI222ENV). It is run automatically during the Install. Also, you are
asked if you want to run it during the Load of the distribution. Answer
"**YES.**"

The Environment Check examines the status of your system to verify that
TaskMan is stopped and that Logons are inhibited (see steps above). If
the install is stopped because your system is not in the proper state,
stop TaskMan and inhibit Logons. Then proceed with the install.

The Environment Check also validates the integrity of File \#1 (the File
of Files) on your system. If a zero node for an entry in File \#1 is
missing, you are notified of the offending entry and the install is
stopped. The problem *must* be resolved before proceeding with the
install.

Production Environment: Load the VA FileMan 22.2 Distribution
-------------------------------------------------------------

You are now ready to Load the Kernel Installation and Distribution
System (KIDS) build and Install VA FileMan 22.2.

1.  Use the \^XUP and Q\^DI entry points to set your DUZ and set DUZ(0)
    to \"**@**\".

<!-- -->

a.  To set DUZ when responding to the Access code prompt. Press
    **Enter** at the OPTION prompt.

\>**D \^XUP**

b.  To set DUZ(0)=\"**@**\"

\>**D Q\^DI**

1.  **[IMPORTANT:]{.underline}** Invoke the **\^XPDKRN** menu and select
    the LOAD A DISTRIBUTION option. Enter the appropriate Host file name
    to load the VA FileMan 22.2 distribution file (FM22\_0.KID).

[]{#_Toc458001747 .anchor}Figure 3: load the VA FileMan 22.2
distribution file

\>**D \^XPDKRN**

KIDS 8.0

Select KIDS OPTION: **1 \<Enter\>** LOAD A DISTRIBUTION

Enter a Host File: **/nfsftp/FLM22/sqakids/VA\_FILEMAN\_22\_2.KID**

KIDS Distribution saved on Mar 18, 2016\@16:57:48

Comment: VA FileMan 22.2 KIDS Build

This Distribution contains Transport Globals for the following
Package(s):

   VA FILEMAN 22.2

Distribution OK!

Want to Continue with Load? YES// **\<Enter\>**

Loading Distribution\...

Build VA FILEMAN 22.2 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// **\<Enter\>**

VA FILEMAN 22.2

Will first run the Environment Check Routine, DI222ENV

Use INSTALL NAME: VA FILEMAN 22.2 to install this Distribution.

Install the VA FileMan 22.2 Package
-----------------------------------

Invoke the \^XPDKRN menu again and select the INSTALL PACKAGE(S) option.
Select VA FILEMAN 22.2 as the package you want to install.

The VA FileMan 22.2 installation takes approximately 10 minutes.

[]{#_Toc458001748 .anchor}Figure 4: Sample installation dialogue

\>**D \^XPDKRN**

KIDS 8.0

Select KIDS OPTION: **6 \<Enter\>** INSTALL PACKAGE(S)

Select INSTALL NAME: **VA FILEMAN 22.2 \<Enter\>** 2/18/16\@11:51:17

=\> VA FileMan 22.2 KIDS build ;Created on Feb 18, 2016\@11:34

This Distribution was loaded on Feb 18, 2016\@11:51:17 with header of

VA FileMan 22.2 KIDS build ;Created on Feb 18, 2016\@11:34

It consisted of the following Install(s):

VA FILEMAN 22.2

Checking Install for Package VA FILEMAN 22.2

Will first run the Environment Check Routine, DI222ENV

Install Questions for VA FILEMAN 22.2

Incoming Files:

.85 LANGUAGE (including data)

Note: You already have the \'LANGUAGE\' File.

I will OVERWRITE your data with mine.

.9 META DATA DICTIONARY

Note: You already have the \'META DATA DICTIONARY\' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//
**\<Enter\>**

Want KIDS to INHIBIT LOGONs during the install? NO**// \<Enter\>**

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//
**\<Enter\>**

Enter the Device you want to print the Install messages.

Enter a \'\^\' to abort the install.

DEVICE: HOME// **\<Enter\>** TELNET

Install Started for VA FILEMAN 22.2 :

Feb 18, 2016\@11:51:32

Build Distribution Date: Feb 18, 2016

Installing Routines:

Feb 18, 2016\@11:51:33

Running Pre-Install Routine: EN\^DI222PRE

Initializing FileMan version 22.2\...

\...\...\...\...\...\...\...\...\...\...\...\.....

Now loading DIALOG and LANGUAGE
Files\...\...\...\...\...\...\...\...\...\...\...\...\...\....

\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....

\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....

\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\...\.....

\...\...\...\...\...\...\...\...\...\...\...\...\.....

\...\...\....

The following files have been installed:

.11 INDEX

.2 DESTINATION

.31 KEY

.4 PRINT TEMPLATE

.401 SORT TEMPLATE

.402 INPUT TEMPLATE

.403 FORM

.404 BLOCK

.44 FOREIGN FORMAT

.46 IMPORT TEMPLATE

.5 FUNCTION

.6 DD AUDIT

.7 MUMPS OPERATING SYSTEM

.81 DATA TYPE

.83 COMPILED ROUTINE

.84 DIALOG

.85 LANGUAGE

.9 META DATA DICTIONARY

1 FILE

1.1 AUDIT

1.11 ARCHIVAL ACTIVITY

1.12 FILEGRAM HISTORY

1.13 FILEGRAM ERROR LOG

1.2 ALTERNATE EDITOR

1.521 SQLI\_SCHEMA

1.52101 SQLI\_KEY\_WORD

1.5211 SQLI\_DATA\_TYPE

1.5212 SQLI\_DOMAIN

1.5213 SQLI\_KEY\_FORMAT

1.5214 SQLI\_OUTPUT\_FORMAT

1.5215 SQLI\_TABLE

1.5216 SQLI\_TABLE\_ELEMENT

1.5217 SQLI\_COLUMN

1.5218 SQLI\_PRIMARY\_KEY

1.5219 SQLI\_FOREIGN\_KEY

1.52191 SQLI\_ERROR\_TEXT

1.52192 SQLI\_ERROR\_LOG

Re-indexing entries in the DIALOG file\...\...\...\...\...\...\...\.....

Compiling all forms \...

DICATT (\#.001)

DIPTED (\#.1001)

DIKC EDIT (\#.1101)

DIKC EDIT UI (\#.1102)

DIKK EDIT (\#.3101)

DIBTED (\#.40001)

DIETED (\#.40101)

DIEDIT (\#.40201)

DDGF BLOCK EDIT (\#.40301)

DDGF PAGE ADD (\#.40302)

DDGF PAGE EDIT (\#.40303)

DDGF PAGE SELECT (\#.40304)

DDGF FORM EDIT (\#.40305)

DDGF HEADER BLOCK EDIT (\#.40306)

DDGF FIELD ADD (\#.40401)

DDGF FIELD CAPTION ONLY (\#.40402)

DDGF FIELD DD (\#.40403)

DDGF FIELD FORM ONLY (\#.40404)

DDGF FIELD COMPUTED (\#.40405)

DDGF BLOCK ADD (\#.40406)

DDGF BLOCK DELETE (\#.40407)

DDGF HEADER BLOCK SELECT (\#.40408)

DDXP FF FORM1 (\#.441)

DDMP SPECIFY IMPORT (\#.461)

XUEDIT CHARACTERISTICS (\#1)

XUEXISTING USER (\#2)

.

.

.

INITIALIZATION COMPLETED IN 3 SECONDS.

Initialization of FileMan version 22.2 has been completed.

Installing Data Dictionaries:

Feb 18, 2016\@11:51:36

Installing Data:

Feb 18, 2016\@11:51:36

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY \....

Installing REMOTE PROCEDURE \...\...\...\....

Installing OPTION \...\...\...\...\...\...\...\...\...\.....

Feb 18, 2016\@11:51:37

Running Post-Install Routine: POST\^DI222POS

Saving Routine: DIDT, As: %DT

Saving Routine: DIDTC, As: %DTC

Saving Routine: DIRCR, As: %RCR

Routine: DIDT Loaded, Saved as %DT

Routine: DIDTC Loaded, Saved as %DTC

Routine: DIRCR Loaded, Saved as %RCR

DIDT ;SFISC/GFT-DATE/TIME UTILITY ;2014-12-26 12:32 PM

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

DIDTC ;SFISC/XAK-DATE/TIME OPERATIONS ;3JAN2011

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

DIRCR ;SFISC/GFT-DELETE THIS LINE AND SAVE AS \'%RCR\'\*\*\* ;13DEC2012

;;22.2;VA FileMan;;Jan 05, 2016;Build 32

Updating Routine file\...

Updating KIDS files\...

VA FILEMAN 22.2 Installed.

Feb 18, 2016\@11:51:38

Not a production UCI

NO Install Message sent

Call MENU rebuild

Starting Menu Rebuild: Feb 18, 2016\@11:51:40

Collecting primary menus in the New Person file\...

Primary menus found in the New Person file

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

.

.

.

Building secondary menu trees\....

Merging\.... done.

Install Completed

Post-Install TaskMan Procedures
-------------------------------

TaskMan should have started when you rebooted or restarted the system.
If TaskMan is not running, start TaskMan.

\>**D \^ZTMB**

Production Environment: Enable Logons
-------------------------------------

Use VA FileMan to edit the Inhibit Logon field in the VOLUME SET file
(\#14.5) for each volume set. This allows TaskMan to start tasks.

[]{#_Toc458001749 .anchor}Figure 5: Enable Logons

\>**D Q\^DI**

VA FileMan 22.2

Select OPTION: **ENTER OR EDIT FILE ENTRIES**

INPUT TO WHAT FILE: **VOLUME SET**

EDIT WHICH FIELD: ALL// **INHIBIT LOGONS ?**

THEN EDIT FIELD: **\<Enter\>**

Select VOLUME SET: ***\<Production Account\>***

INHIBIT LOGONS?: YES// **NO**

**\*\*\*\* You have now completed the installation of VA FileMan.
\*\*\*\***

2.  Implementation Procedure
    ========================

    1.  Database Tuning
        ---------------

There are no special database tuning requirements for VA FileMan 22.2.

Verify Installation
-------------------

Verify the installation. Use KIDS option Install File Print, under the
Utilities menu, and enter VA FILEMAN 22.2.  Confirm that the STATUS
field is "Install Complete".

Back-Out Plan
=============

Back-out pertains to a return to the last known good operational state
of the software and appropriate platform settings.

The method of backing out the VA FileMan (FM) 22.2 patch is to restore
from the backup that was taken in the "[Back Up System]{.underline}"
section. Due to the fact that FM 22.2 is a change to the system
infrastructure, this is the only way to put the system back to the pre
FM 22.2 state.

Back-Out Strategy
-----------------

The need for a back-out would be determined by all affected
organizations. This would primarily include representatives from
Veterans Health Administration (VHA) and Enterprise Program Management
(EPMO). In the case of the initial release a back-out would include
removal of data, files and routines. In the case of future patches and
releases the back-out strategy would be dependent on the contents of the
released functionality and could include restoration of file
definitions, routines or data.

Back-Out Considerations
-----------------------

Back-out considerations would include impact on production VistA
end-users and impact on Wide Area Network.

### Load Testing

Not applicable for FM 22.2.

### User Acceptance Testing

FM 22.2 User Acceptance Testing (UAT) is performed during VistA patch
testing at test sites.

Back-Out Criteria
-----------------

The FM 22.2 back-out criteria follow existing VistA back-out procedures.

Back-Out Risks
--------------

The FM 22.2 back-out risks are the same risks established with existing
VistA back-out procedures.

Authority for Back-Out
----------------------

The authority for the need of back-out would reside with VHA and EPMO
representatives.

Back-Out Procedure
------------------

To back out FM 22.2, do the following:

-   Restore backup to reset the system to the pre FM 22.2 state.

-   You will lose everything that has happened since the install.

![Caution](images/media/image3.png "Caution"){width="0.4479166666666667in"
height="0.4479166666666667in"} CAUTION: Once the system has been
restarted, the backout procedure is no longer possible.

Rollback Plan
=============

Rollback pertains to data.

VA FileMan (FM) 22.2 does *not* export any data.

Rollback Considerations
-----------------------

N/A. FM 22.2 does not export any data.

Rollback Criteria
-----------------

N/A. FM 22.2 does not export any data.

Rollback Risks
--------------

N/A. FM 22.2 does not export any data.

Authority for Rollback
----------------------

Rollback *can* be authorized by system administrators once a problem has
been identified. Enterprise Program Management Office (EPMO) should be
informed immediately *via a MailMan message sent to:*

REDACTED

Rollback Procedure
------------------

N/A. FM 22.2 does not export any data.
